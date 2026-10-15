#!/usr/bin/env python3
"""Audit an explicit CSV measurement contract; run bounded response diagnostics.

Standard-library only. No downloading, imputation, model fitting, or validity score.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n")


def require_profile(profile):
    if profile.get("schema_version") != 1:
        raise ValueError("profile.schema_version must be 1")
    if profile.get("data_origin") not in {"observed", "synthetic"}:
        raise ValueError("Declare data_origin as observed or synthetic; never infer it from successful execution")
    for key in ("name", "version"):
        if not str(profile.get("benchmark", {}).get(key, "")).strip():
            raise ValueError(f"benchmark.{key} is required")
    for key in ("system", "item", "score"):
        if not str(profile.get("columns", {}).get(key, "")).strip():
            raise ValueError(f"columns.{key} is required")
        if not str(profile.get("units", {}).get(key, "")).strip():
            raise ValueError(f"units.{key} must describe what is measured")
    if not profile.get("condition") and not profile["columns"].get("condition"):
        raise ValueError("Declare a constant condition or a condition column")
    scale = profile.get("score_scale", {})
    if scale.get("kind") not in {"binary", "interval", "discrete"}:
        raise ValueError("score_scale.kind must be binary, interval or discrete")
    if scale["kind"] == "interval":
        if not all(isinstance(scale.get(k), (int, float)) and math.isfinite(scale[k]) for k in ("min", "max")):
            raise ValueError("An interval scale needs finite min and max")
        if scale["min"] >= scale["max"]:
            raise ValueError("score_scale.min must be smaller than max")
    if scale["kind"] == "discrete":
        vals = scale.get("values", [])
        if not vals or not all(isinstance(v, (int, float)) and math.isfinite(v) for v in vals):
            raise ValueError("A discrete scale needs finite values")
    if not isinstance(profile.get("filters", {}), dict):
        raise ValueError("filters must be an object")
    sampling = profile.get("resampling", {"unit": "none"})
    if sampling.get("unit") not in {"none", "item", "cluster"}:
        raise ValueError("resampling.unit must be none, item or cluster")
    if sampling.get("unit") != "none" and not sampling.get("justification", "").strip():
        raise ValueError("Resampling requires a scientific justification")
    if sampling.get("unit") == "cluster" and not profile["columns"].get("cluster"):
        raise ValueError("Cluster resampling requires columns.cluster")


def inspect(csv_path, profile):
    """Return machine audit and parsed rows; source semantics remain analyst-reviewed."""
    require_profile(profile)
    columns = profile["columns"]
    scale = profile["score_scale"]
    errors, warnings, records = [], [], []
    with Path(csv_path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        required = set(columns.values()) | set(profile.get("filters", {}))
        if missing := sorted(required - set(headers)):
            raise ValueError("Missing CSV columns: " + ", ".join(missing))
        if len(headers) != len(set(headers)):
            raise ValueError("Duplicate CSV header names")
        raw = list(reader)
    if not raw:
        errors.append("CSV contains no rows")
    expected_hash = profile.get("source", {}).get("sha256")
    actual_hash = digest(csv_path)
    if expected_hash and expected_hash != actual_hash:
        errors.append("Source SHA256 differs from the declared frozen input")
    selected = []
    for row_number, row in enumerate(raw, 2):
        if all(row.get(k) in ([v] if not isinstance(v, list) else v) for k, v in profile.get("filters", {}).items()):
            selected.append((row_number, row))
    if not selected:
        errors.append("No rows match the declared filters")
    keys, clusters = set(), {}
    for line, row in selected:
        prefix = f"CSV row {line}: "
        if None in row or any(row.get(c) is None for c in required):
            errors.append(prefix + "malformed row width")
            continue
        ids = {k: row[columns[k]].strip() for k in ("system", "item")}
        if not all(ids.values()):
            errors.append(prefix + "empty system or item identifier")
            continue
        trial = row[columns["trial"]].strip() if columns.get("trial") else "single"
        condition = row[columns["condition"]].strip() if columns.get("condition") else profile["condition"]
        version = row[columns["version"]].strip() if columns.get("version") else profile["benchmark"]["version"]
        cluster = row[columns["cluster"]].strip() if columns.get("cluster") else ids["item"]
        if not all((trial, condition, version, cluster)):
            errors.append(prefix + "empty trial, condition, version or cluster identity")
            continue
        if columns.get("version") and version != profile["benchmark"]["version"]:
            errors.append(prefix + "version differs from the declared benchmark version")
        key = (version, condition, ids["system"], ids["item"], trial)
        if key in keys:
            errors.append(prefix + "duplicate logical observation (version, condition, system, item, trial)")
        keys.add(key)
        item_key = (version, condition, ids["item"])
        if item_key in clusters and clusters[item_key] != cluster:
            errors.append(prefix + "one item maps to multiple clusters")
        clusters[item_key] = cluster
        token = row[columns["score"]].strip()
        status = row[columns["status"]].strip() if columns.get("status") else "graded"
        if status not in {"graded", "ungraded"}:
            errors.append(prefix + "status must be graded or ungraded; document source-status conversion explicitly")
        value = None
        if token == "":
            if status != "ungraded":
                errors.append(prefix + "blank score requires explicit status=ungraded")
        elif status == "ungraded":
            errors.append(prefix + "ungraded attempt has a nonempty score")
        else:
            try:
                value = float(profile.get("score_mapping", {}).get(token, token))
                if not math.isfinite(value):
                    raise ValueError("score is not finite")
                if scale["kind"] == "binary" and value not in (0, 1):
                    raise ValueError("score is not a single binary outcome")
                if scale["kind"] == "interval" and not scale["min"] <= value <= scale["max"]:
                    raise ValueError("score is outside the declared interval")
                if scale["kind"] == "discrete" and value not in scale["values"]:
                    raise ValueError("score is outside the declared discrete values")
            except (ValueError, TypeError) as exc:
                errors.append(prefix + str(exc))
                value = None
        records.append(dict(**ids, trial=trial, condition=condition, version=version, cluster=cluster, score=value, line=line))
    conditions = sorted({r["condition"] for r in records})
    versions = sorted({r["version"] for r in records})
    if len(conditions) > 1:
        warnings.append("Multiple conditions: inspect separately; diagnostics require an explicit single-condition filter")
    if profile["data_origin"] == "synthetic":
        warnings.append("Synthetic data: outputs are demonstrations, not empirical benchmark evidence")
    if scale["kind"] != "binary":
        warnings.append("This diagnostic helper handles binary outcomes only; no thresholding is performed")
    groups = []
    for version, condition in sorted({(r["version"], r["condition"]) for r in records}):
        rows = [r for r in records if (r["version"], r["condition"]) == (version, condition)]
        systems, items = sorted({r["system"] for r in rows}), sorted({r["item"] for r in rows})
        attempted = Counter((r["system"], r["item"]) for r in rows)
        graded = Counter((r["system"], r["item"]) for r in rows if r["score"] is not None)
        counts = [graded[(s, i)] for s in systems for i in items]
        groups.append({"version": version, "condition": condition, "systems": len(systems), "items": len(items),
                       "attempted_rows": len(rows), "graded_rows": sum(graded.values()),
                       "ungraded_attempts": sum(r["score"] is None for r in rows),
                       "unavailable_system_item_cells": len(systems) * len(items) - len(attempted),
                       "cells_without_graded_response": sum(n == 0 for n in counts),
                       "min_graded_repeats": min(counts, default=0), "max_graded_repeats": max(counts, default=0),
                       "complete_balanced_graded_panel": bool(counts) and min(counts) > 0 and len(set(counts)) == 1})
    return {"schema_version": 1, "status": "failed" if errors else "passed", "errors": errors, "warnings": warnings,
            "source": {"path": str(Path(csv_path).resolve()), "sha256": actual_hash}, "raw_rows": len(raw),
            "selected_rows": len(selected), "data_origin": profile["data_origin"], "filters": profile.get("filters", {}),
            "units": profile["units"], "groups": groups,
            "binary_diagnostics_eligible": not errors and scale["kind"] == "binary" and len(conditions) == len(versions) == 1,
            "semantic_review": "Required: column meaning, provenance, scientific scope and design are declarations, not verified by this audit"}, records


def quantile(values, p):
    ordered = sorted(values)
    at = (len(ordered) - 1) * p
    lo, hi = math.floor(at), math.ceil(at)
    return ordered[lo] + (ordered[hi] - ordered[lo]) * (at - lo)


def diagnose(audit, records, profile, draws=2000, seed=17, allow_demo=False):
    if not audit["binary_diagnostics_eligible"]:
        raise ValueError("Audit does not permit binary diagnostics; resolve errors and filter one condition/version")
    if profile["data_origin"] == "synthetic" and not allow_demo:
        raise ValueError("Synthetic input requires --allow-demo and cannot become empirical evidence")
    if draws < 100 or draws > 100000:
        raise ValueError("bootstrap draws must be between 100 and 100000")
    cells = defaultdict(list)
    for row in records:
        if row["score"] is not None:
            cells[(row["system"], row["item"])].append((row["trial"], row["score"]))
    if not cells:
        raise ValueError("No graded responses to diagnose")
    cells = {k: [v for _, v in sorted(vals)] for k, vals in sorted(cells.items())}
    systems = sorted({s for s, _ in cells})
    items = sorted({i for _, i in cells})
    per_system = []
    for system in systems:
        groups = {i: cells[(system, i)] for i in items if (system, i) in cells}
        vals = [v for scores in groups.values() for v in scores]
        repeats = {len(v) for v in groups.values()}
        result = {"system": system, "graded_items": len(groups), "graded_trials": len(vals),
                  "mean_over_observed_trials": statistics.mean(vals),
                  "mean_over_observed_item_means": statistics.mean(statistics.mean(v) for v in groups.values()),
                  "repeat_count_uniform_within_system": len(repeats) == 1}
        if len(repeats) == 1:
            k = next(iter(repeats))
            result.update({"k": k, "empirical_any_success_in_k": statistics.mean(any(v) for v in groups.values()),
                           "empirical_all_success_in_k": statistics.mean(all(v) for v in groups.values()),
                           "empirical_mixed_outcome_fraction": statistics.mean(0 < sum(v) < k for v in groups.values())})
        per_system.append(result)
    per_item = [{"item": i, "systems_observed": sum((s, i) in cells for s in systems),
                 "mean_over_system_cell_means": statistics.mean(statistics.mean(cells[(s, i)]) for s in systems if (s, i) in cells)} for i in items]
    sampling = profile.get("resampling", {"unit": "none"})
    panel_complete = audit["groups"][0]["complete_balanced_graded_panel"]
    if not panel_complete:
        reason = "No intervals: incomplete or unequal-repeat panel; this helper does not model its missingness/weighting"
    elif sampling.get("unit") == "none":
        reason = "No intervals: no justified resampling unit declared"
    else:
        reason = None
    pairs = []
    if reason is None:
        item_clusters = {r["item"]: r["cluster"] for r in records}
        blocks = defaultdict(list)
        for item in items:
            blocks[item_clusters[item] if sampling["unit"] == "cluster" else item].append(item)
        block_ids = sorted(blocks)
        if len(block_ids) < 2:
            reason = "No intervals: fewer than two independent resampling units"
        else:
            rng = random.Random(seed)
            selections = [[item for block in rng.choices(block_ids, k=len(block_ids)) for item in blocks[block]] for _ in range(draws)]
            for left_index, left in enumerate(systems):
                for right in systems[left_index + 1:]:
                    differences = {i: statistics.mean(cells[(left, i)]) - statistics.mean(cells[(right, i)]) for i in items}
                    boot = [statistics.mean(differences[i] for i in selection) for selection in selections]
                    pairs.append({"left": left, "right": right, "difference_left_minus_right": statistics.mean(differences.values()),
                                  "percentile_95_interval": [quantile(boot, .025), quantile(boot, .975)],
                                  "items": len(items), "resampling_units": len(block_ids)})
    return {"schema_version": 1, "computation_status": "completed", "data_origin": profile["data_origin"],
            "evidence_kind": "simulation" if profile["data_origin"] == "synthetic" else "computed_from_existing_observations",
            "source": audit["source"], "filters": audit["filters"], "per_system": per_system, "per_item": per_item,
            "paired_comparisons": pairs, "interval_status": reason or "Computed conditional task/cluster bootstrap intervals",
            "bootstrap": {"draws": draws, "seed": seed, **sampling},
            "limits": ["Describes the declared frozen systems, tasks and scoring conditions; no new benchmark run was performed",
                       "Empirical any/all success across observed repeats is not an independent deployment probability",
                       "Intervals resample declared task units, holding observed within-task trials fixed; they do not include every uncertainty source",
                       "Paired intervals are unadjusted for multiplicity; zero-width intervals at a ceiling do not establish no uncertainty",
                       "These statistics do not establish content coverage, construct meaning, execution fidelity or real-world benefit",
                       "No latent model, variance decomposition or validity rating is computed"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["audit", "diagnose"])
    parser.add_argument("--csv", required=True)
    parser.add_argument("--profile", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--bootstrap", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--allow-demo", action="store_true")
    args = parser.parse_args()
    try:
        profile = json.loads(Path(args.profile).read_text())
        audit, rows = inspect(args.csv, profile)
        result = audit if args.action == "audit" else diagnose(audit, rows, profile, args.bootstrap, args.seed, args.allow_demo)
        result["execution"] = {"command": sys.argv, "python": sys.version.split()[0], "script_sha256": digest(__file__),
                               "profile_sha256": digest(args.profile)}
        write_json(args.output, result)
        print(json.dumps({"output": args.output, "status": result.get("status", result.get("computation_status"))}))
        return 1 if audit["status"] == "failed" else 0
    except (ValueError, KeyError, TypeError, OSError) as exc:
        write_json(args.output, {"computation_status": "failed", "error": str(exc), "command": sys.argv})
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
