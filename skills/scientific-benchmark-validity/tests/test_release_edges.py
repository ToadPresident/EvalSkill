"""Synthetic release regressions: preserve missingness and check real artifacts."""
import csv
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mt, ev = load("measurement_tools"), load("verify_evidence")


class ReleaseEdges(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.csv = self.root / "responses.csv"
        self.rows = [
            {"system": s, "item": i, "score": "1", "status": "graded", "condition": "c1"}
            for s in ("A", "B") for i in ("t1", "t2")
        ]
        self.profile = {
            "schema_version": 1, "data_origin": "synthetic",
            "benchmark": {"name": "Synthetic fixture", "version": "v1"},
            "columns": {k: k for k in self.rows[0]},
            "units": {"system": "fixture system", "item": "fixture task", "score": "single binary outcome"},
            "score_scale": {"kind": "binary"},
            "resampling": {"unit": "item", "justification": "Synthetic independent tasks"},
        }
        self.source = self.root / "source.txt"
        self.source.write_text("Synthetic observation only.\n", encoding="utf-8")
        self.registry = {
            "sources": [{"id": "S1", "version": "fixture", "locator": "line 1", "path": "source.txt",
                         "sha256": hashlib.sha256(self.source.read_bytes()).hexdigest()}],
            "evidence": [{"id": "E1", "source_id": "S1", "locator": "line 1", "kind": "simulation",
                          "observation": "A synthetic observation"}],
            "report_evidence_ids": ["E1"],
        }

    def audit(self):
        with self.csv.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(self.rows[0]))
            writer.writeheader()
            writer.writerows(self.rows)
        return mt.inspect(self.csv, self.profile)

    def diagnose(self):
        audit, rows = self.audit()
        return mt.diagnose(audit, rows, self.profile, draws=100, allow_demo=True)

    def test_all_ungraded_system_stays_visible(self):
        for row in self.rows:
            if row["system"] == "B":
                row.update(score="", status="ungraded")
        out = self.diagnose()
        systems = {r["system"]: r for r in out["per_system"]}
        self.assertIn("B", systems)
        self.assertEqual(systems["B"]["attempted_trials"], 2)
        self.assertEqual(systems["B"]["ungraded_trials"], 2)
        self.assertIsNone(systems["B"]["mean_over_observed_trials"])
        self.assertEqual(systems["B"]["score_status"], "no_graded_responses")
        self.assertEqual(out["paired_comparisons"], [])

    def test_fully_ungraded_data_keep_counts_without_invented_scores(self):
        for row in self.rows:
            row.update(score="", status="ungraded")
        out = self.diagnose()
        self.assertEqual(len(out["per_system"]), 2)
        self.assertTrue(all(r["mean_over_observed_trials"] is None for r in out["per_system"]))
        self.assertTrue(all(r["mean_over_system_cell_means"] is None for r in out["per_item"]))
        self.assertEqual(out["paired_comparisons"], [])

    def test_constant_condition_conflict_rejected(self):
        self.profile["condition"] = "c2"
        self.assertEqual(self.audit()[0]["status"], "failed")

    def test_matching_constant_condition_accepted(self):
        self.profile["condition"] = "c1"
        self.assertEqual(self.audit()[0]["status"], "passed")

    def test_malformed_profiles_write_failure_records(self):
        self.audit()
        for bad in ([], {**self.profile, "benchmark": []}, {**self.profile, "columns": []},
                    {**self.profile, "source": []}, {**self.profile, "resampling": []}):
            with self.subTest(profile=bad):
                profile = self.root / "profile.json"
                profile.write_text(json.dumps(bad), encoding="utf-8")
                result_path = self.root / "failed.json"
                result_path.unlink(missing_ok=True)
                run = subprocess.run([sys.executable, str(SCRIPTS / "measurement_tools.py"), "audit",
                                      "--csv", str(self.csv), "--profile", str(profile), "--output", str(result_path)],
                                     capture_output=True, text=True)
                self.assertNotEqual(run.returncode, 0)
                self.assertTrue(result_path.is_file(), run.stderr)
                self.assertEqual(json.loads(result_path.read_text())["computation_status"], "failed")
                self.assertNotIn("Traceback", run.stderr)

    def inventory(self, ids):
        self.profile["item_inventory"] = {"ids": ids, "version": "v1", "source_locator": "Synthetic task manifest"}

    def test_inventory_reveals_entirely_absent_item(self):
        self.inventory(["t1", "t2", "t3"])
        audit, _ = self.audit()
        group = audit["groups"][0]
        self.assertEqual(group["unobserved_expected_items"], ["t3"])
        self.assertEqual(group["unavailable_system_item_cells"], 2)
        self.assertFalse(group["complete_balanced_graded_panel"])
        out = self.diagnose()
        missing = next(row for row in out["per_item"] if row["item"] == "t3")
        self.assertEqual(missing["attempted_systems"], 0)
        self.assertIsNone(missing["mean_over_system_cell_means"])
        self.assertEqual(out["paired_comparisons"], [])

    def test_observed_panel_does_not_claim_expected_coverage(self):
        group = self.audit()[0]["groups"][0]
        self.assertEqual(group["coverage_basis"], "observed_items_only")
        self.assertIsNone(group["complete_expected_item_coverage"])

    def test_unexpected_item_is_identity_error(self):
        self.inventory(["t1"])
        self.assertEqual(self.audit()[0]["status"], "failed")

    def test_inventory_version_and_duplicates_rejected(self):
        self.inventory(["t1", "t1"])
        with self.assertRaises(ValueError):
            self.audit()
        self.inventory(["t1", "t2"])
        self.profile["item_inventory"]["version"] = "v2"
        with self.assertRaises(ValueError):
            self.audit()

    def report(self, text):
        path = self.root / "report.md"
        path.write_text(text, encoding="utf-8")
        return ev.verify(self.registry, self.root, report=path)

    def test_actual_unknown_report_reference_fails(self):
        result = self.report("An unsupported statement [E99].")
        self.assertEqual(result["status"], "failed")
        self.assertIn("E99", " ".join(result["errors"]))

    def test_actual_report_is_hashed_and_scanned(self):
        result = self.report("A synthetic result [E1].")
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["report"]["evidence_ids"], ["E1"])
        self.assertEqual(result["report"]["sha256"], hashlib.sha256((self.root / "report.md").read_bytes()).hexdigest())

    def test_empty_or_unsupported_reference_syntax_is_not_success(self):
        for body in ("No explicit citations.", "A range [E1–E3]."):
            with self.subTest(body=body):
                self.assertEqual(self.report(body)["status"], "failed")

    def test_combined_ids_and_legacy_list_disagreement(self):
        self.registry["evidence"].append({**self.registry["evidence"][0], "id": "E2"})
        self.assertEqual(self.report("Two observations [E1, E2].")["status"], "failed")
        self.registry.pop("report_evidence_ids")
        self.assertEqual(self.report("Two observations [E1, E2].")["status"], "passed")

    def test_omitted_report_explicitly_not_checked(self):
        result = ev.verify(self.registry, self.root)
        self.assertEqual(result["report"]["status"], "not_checked")

    def test_bad_registry_writes_failure_record(self):
        registry = self.root / "registry.json"
        out = self.root / "check.json"
        registry.write_text("[]", encoding="utf-8")
        run = subprocess.run([sys.executable, str(SCRIPTS / "verify_evidence.py"), "--registry", str(registry),
                              "--output", str(out)], capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0)
        self.assertTrue(out.is_file(), run.stderr)
        self.assertEqual(json.loads(out.read_text())["status"], "failed")
        self.assertNotIn("Traceback", run.stderr)


if __name__ == "__main__":
    unittest.main()
