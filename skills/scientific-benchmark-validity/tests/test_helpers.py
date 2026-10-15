"""Small synthetic invariants; these are software tests, not benchmark results."""
import copy
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


def module(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / (name + ".py"))
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


mt, ev = module("measurement_tools"), module("verify_evidence")


class Measurements(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / "data.csv"
        self.rows = []
        for system, values in {"A": [[1, 1], [1, 0], [0, 0]], "B": [[1, 0], [0, 0], [0, 0]]}.items():
            for task, scores in enumerate(values, 1):
                for trial, score in enumerate(scores):
                    self.rows.append(dict(system=system, item=f"t{task}", trial=str(trial), score=str(score), condition="c1", version="v1", status="graded", cluster="p1" if task < 3 else "p2"))
        self.profile = {"schema_version": 1, "benchmark": {"name": "Synthetic test", "version": "v1"},
                        "data_origin": "synthetic", "units": {"system": "test system", "item": "synthetic task", "score": "binary single trial"},
                        "columns": {k: k for k in ("system", "item", "trial", "score", "condition", "version", "status")},
                        "score_scale": {"kind": "binary"}, "resampling": {"unit": "item", "justification": "Synthetic independent tasks for a software invariant"}}

    def run_audit(self):
        with self.path.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(self.rows[0]))
            writer.writeheader()
            writer.writerows(self.rows)
        return mt.inspect(self.path, self.profile)

    def result(self):
        audit, rows = self.run_audit()
        return mt.diagnose(audit, rows, self.profile, draws=1000, seed=7, allow_demo=True)

    def test_hand_computed_repeat_summaries(self):
        result = self.result()
        a, b = result["per_system"]
        self.assertEqual(a["mean_over_observed_trials"], .5)
        self.assertEqual(a["empirical_any_success_in_k"], 2 / 3)
        self.assertEqual(a["empirical_all_success_in_k"], 1 / 3)
        self.assertEqual(a["empirical_mixed_outcome_fraction"], 1 / 3)
        self.assertEqual(b["mean_over_observed_trials"], 1 / 6)
        self.assertEqual(result["paired_comparisons"][0]["difference_left_minus_right"], 1 / 3)
        self.assertEqual(result["evidence_kind"], "simulation")

    def test_permutation_invariance(self):
        first = self.result()
        self.rows.reverse()
        second = self.result()
        for key in ("per_system", "per_item", "paired_comparisons"):
            self.assertEqual(first[key], second[key])

    def test_nonfinite_and_out_of_scale_rejected(self):
        for value in ("NaN", "inf", "-inf", "2", "0.5", "text"):
            with self.subTest(value=value):
                self.rows[0]["score"] = value
                audit, rows = self.run_audit()
                self.assertEqual(audit["status"], "failed")
                with self.assertRaises(ValueError):
                    mt.diagnose(audit, rows, self.profile, allow_demo=True)

    def test_duplicate_rejected(self):
        self.rows.append(self.rows[0].copy())
        self.assertIn("duplicate logical", " ".join(self.run_audit()[0]["errors"]))

    def test_version_mixing_rejected(self):
        self.rows[0]["version"] = "v2"
        self.assertEqual(self.run_audit()[0]["status"], "failed")

    def test_condition_mixing_requires_filter(self):
        self.rows[0]["condition"] = "c2"
        audit, rows = self.run_audit()
        self.assertFalse(audit["binary_diagnostics_eligible"])
        self.profile["filters"] = {"condition": "c1"}
        self.assertTrue(self.run_audit()[0]["binary_diagnostics_eligible"])

    def test_missing_is_not_failure(self):
        self.rows = [r for r in self.rows if not (r["system"] == "B" and r["item"] == "t3")]
        audit, rows = self.run_audit()
        self.assertEqual(audit["groups"][0]["unavailable_system_item_cells"], 1)
        self.assertFalse(audit["groups"][0]["complete_balanced_graded_panel"])
        out = mt.diagnose(audit, rows, self.profile, allow_demo=True)
        self.assertEqual(out["per_system"][1]["graded_items"], 2)
        self.assertEqual(out["paired_comparisons"], [])

    def test_blank_requires_explicit_ungraded_status(self):
        self.rows[0]["score"] = ""
        self.assertEqual(self.run_audit()[0]["status"], "failed")
        self.rows[0]["status"] = "ungraded"
        audit, _ = self.run_audit()
        self.assertEqual(audit["status"], "passed")
        self.assertEqual(audit["groups"][0]["ungraded_attempts"], 1)
        self.assertEqual(audit["groups"][0]["unavailable_system_item_cells"], 0)

    def test_unknown_status_rejected(self):
        self.rows[0]["status"] = "scorer_crashed"
        self.assertEqual(self.run_audit()[0]["status"], "failed")

    def test_synthetic_requires_explicit_demo_mode(self):
        audit, rows = self.run_audit()
        with self.assertRaisesRegex(ValueError, "Synthetic"):
            mt.diagnose(audit, rows, self.profile)

    def test_continuous_audit_without_binary_thresholding(self):
        self.profile["score_scale"] = {"kind": "interval", "min": 0, "max": 1}
        self.rows[0]["score"] = ".5"
        audit, _ = self.run_audit()
        self.assertEqual(audit["status"], "passed")
        self.assertFalse(audit["binary_diagnostics_eligible"])

    def test_unknown_resampling_no_intervals(self):
        self.profile["resampling"] = {"unit": "none"}
        self.assertEqual(self.result()["paired_comparisons"], [])

    def test_cluster_unit_is_preserved(self):
        self.profile["columns"]["cluster"] = "cluster"
        self.profile["resampling"]["unit"] = "cluster"
        out = self.result()
        self.assertEqual(out["paired_comparisons"][0]["resampling_units"], 2)

    def test_single_cluster_blocks_intervals(self):
        self.profile["columns"]["cluster"] = "cluster"
        self.profile["resampling"]["unit"] = "cluster"
        for row in self.rows:
            row["cluster"] = "one"
        self.assertEqual(self.result()["paired_comparisons"], [])

    def test_unequal_repeats_do_not_hide_weighting(self):
        self.rows.pop(0)
        out = self.result()
        self.assertFalse(out["per_system"][0]["repeat_count_uniform_within_system"])
        self.assertNotEqual(out["per_system"][0]["mean_over_observed_trials"], out["per_system"][0]["mean_over_observed_item_means"])
        self.assertNotIn("empirical_all_success_in_k", out["per_system"][0])
        self.assertEqual(out["paired_comparisons"], [])

    def test_wrong_source_hash_rejected(self):
        self.profile["source"] = {"sha256": "0" * 64}
        self.assertEqual(self.run_audit()[0]["status"], "failed")

    def test_cli_failure_has_nonzero_exit_and_failure_record(self):
        self.run_audit()
        profile_path = self.root / "profile.json"
        profile_path.write_text(json.dumps(self.profile))
        out = self.root / "result.json"
        result = subprocess.run([sys.executable, str(SCRIPTS / "measurement_tools.py"), "diagnose", "--csv", str(self.path), "--profile", str(profile_path), "--output", str(out)], capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(json.loads(out.read_text())["computation_status"], "failed")


class Evidence(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source.txt"
        self.source.write_text("A synthetic source says: five repeated trials.\nNo other conclusion is stated.\n")
        self.registry = {"sources": [{"id": "S1", "version": "test", "locator": "synthetic fixture", "path": "source.txt", "sha256": hashlib.sha256(self.source.read_bytes()).hexdigest()}],
                         "evidence": [{"id": "E1", "source_id": "S1", "locator": "line 1", "kind": "simulation", "observation": "Five repetitions in a synthetic fixture", "excerpt": "five repeated trials."}],
                         "report_evidence_ids": ["E1"]}

    def test_match_does_not_certify_semantics(self):
        result = ev.verify(self.registry, self.root)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["checks"][1]["fact_review"], "not_recorded")
        self.assertEqual(result["checks"][1]["relevance_review"], "not_recorded")

    def test_fabricated_excerpt_detected(self):
        self.registry["evidence"][0]["excerpt"] = "universal scientific ability"
        self.assertEqual(ev.verify(self.registry, self.root)["status"], "failed")

    def test_source_changed_after_pin_detected(self):
        self.source.write_text("changed")
        self.assertEqual(ev.verify(self.registry, self.root)["status"], "failed")

    def test_unknown_reference_detected(self):
        self.registry["report_evidence_ids"].append("E99")
        self.assertEqual(ev.verify(self.registry, self.root)["status"], "failed")

    def test_review_claim_requires_basis(self):
        self.registry["evidence"][0]["review"] = {"fact": {"status": "checked"}}
        self.assertEqual(ev.verify(self.registry, self.root)["status"], "failed")


if __name__ == "__main__":
    unittest.main()
