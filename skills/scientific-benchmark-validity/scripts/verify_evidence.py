#!/usr/bin/env python3
"""Check evidence-record integrity, not factual or inferential validity."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


def normal(text):
    return re.sub(r"\s+", " ", text).strip()


def verify(registry, base, report=None):
    if not isinstance(registry, dict):
        raise ValueError("registry must be a JSON object")
    for key in ("sources", "evidence"):
        if not isinstance(registry.get(key), list) or not all(isinstance(v, dict) for v in registry[key]):
            raise ValueError(f"registry.{key} must be a list of objects")
    if "report_evidence_ids" in registry and (not isinstance(registry["report_evidence_ids"], list)
            or not all(isinstance(v, str) for v in registry["report_evidence_ids"])):
        raise ValueError("report_evidence_ids must be a list of strings")
    errors, checks, seen = [], [], set()
    sources = {}
    for source in registry.get("sources", []):
        sid = source.get("id")
        if not isinstance(sid, str) or not sid or sid in sources:
            errors.append("Missing or duplicate source ID")
            continue
        sources[sid] = source
        if not source.get("version") or not source.get("locator"):
            errors.append(f"{sid}: source version and locator required")
        if source.get("path"):
            path = (base / source["path"]).resolve()
            if not path.is_file():
                errors.append(f"{sid}: source file unavailable")
            elif not source.get("sha256"):
                errors.append(f"{sid}: local sources require a pinned sha256")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != source["sha256"]:
                errors.append(f"{sid}: source hash mismatch")
            else:
                checks.append({"id": sid, "file_integrity": "matched"})
    if not sources:
        errors.append("No sources registered")
    for entry in registry.get("evidence", []):
        eid = entry.get("id")
        if not isinstance(eid, str) or not eid or eid in seen:
            errors.append("Missing or duplicate evidence ID")
            continue
        seen.add(eid)
        source = sources.get(entry.get("source_id"))
        if source is None:
            errors.append(f"{eid}: unknown source ID")
            continue
        if not entry.get("locator") or not entry.get("observation"):
            errors.append(f"{eid}: locator and observation required")
        if entry.get("kind") not in {"author_claim", "reported_result", "protocol", "computed_result", "simulation", "analyst_inference", "proposed_study"}:
            errors.append(f"{eid}: unknown evidence kind")
        snippet_status = "not_requested"
        if entry.get("excerpt"):
            if not source.get("path"):
                snippet_status = "unavailable_local_text"
            else:
                path = (base / source["path"]).resolve()
                if path.suffix.lower() not in {".txt", ".md", ".csv", ".json", ".py", ".rmd", ".yaml", ".html"}:
                    snippet_status = "requires_visual_or_specialized_check"
                elif path.is_file():
                    found = normal(entry["excerpt"]) in normal(path.read_text(encoding="utf-8"))
                    snippet_status = "matched_in_file" if found else "not_found"
                    if not found:
                        errors.append(f"{eid}: excerpt not found in declared source text")
        review = entry.get("review", {})
        if not isinstance(review, dict) or not all(isinstance(review.get(key, {}), dict) for key in ("fact", "relevance")):
            raise ValueError(f"{eid}: review and its fact/relevance records must be objects")
        for key in ("fact", "relevance"):
            if review.get(key, {}).get("status") == "checked" and not review[key].get("basis"):
                errors.append(f"{eid}: checked {key} review lacks its basis")
        checks.append({"id": eid, "excerpt_integrity": snippet_status,
                       "fact_review": review.get("fact", {}).get("status", "not_recorded"),
                       "relevance_review": review.get("relevance", {}).get("status", "not_recorded")})
    if not seen:
        errors.append("No evidence entries registered")
    for reference in registry.get("report_evidence_ids", []):
        if reference not in seen:
            errors.append(f"Declared report list refers to unknown evidence ID {reference}")
    report_check = {"status": "not_checked", "reason": "No actual report supplied; a declared ID list is not a report scan"}
    if report is not None:
        report = Path(report)
        raw = report.read_bytes()
        body = raw.decode("utf-8-sig")
        used = set()
        malformed = []
        for bracket in re.findall(r"\[([^\]\n]+)\]", body):
            if re.match(r"\s*E\d", bracket):
                if not re.fullmatch(r"\s*E\d+(?:\s*[,;]\s*E\d+)*\s*", bracket):
                    malformed.append(bracket)
                else:
                    used.update(re.findall(r"E\d+", bracket))
        unknown = sorted(used - seen)
        if unknown:
            errors.append("Actual report refers to unknown evidence IDs: " + ", ".join(unknown))
        if malformed:
            errors.append("Unsupported evidence markers; use [E1] or [E1, E2], without ranges: " + "; ".join(malformed))
        if not used:
            errors.append("No explicit evidence markers found in actual report; this is not a successful citation check")
        mismatch = "report_evidence_ids" in registry and set(registry["report_evidence_ids"]) != used
        if mismatch:
            errors.append("Declared report_evidence_ids do not match the actual report markers")
        report_check = {"status": "failed" if unknown or malformed or not used or mismatch else "passed",
                        "path": str(report.resolve()), "sha256": hashlib.sha256(raw).hexdigest(),
                        "evidence_ids": sorted(used), "unknown_ids": unknown,
                        "scope": "Explicit [E1] / [E1, E2] markers anywhere in the file, including its index; not prose entailment or citation completeness"}
    return {"status": "failed" if errors else "passed", "errors": errors, "checks": checks,
            "report": report_check,
            "scope": "Integrity only. A matching excerpt is not verification of its stated page, factual qualifiers, independence or inference. Review statuses are declarations, not automated certification. Zero extracted evidence is not proof of absence."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True)
    parser.add_argument("--base-dir", help="Defaults to the registry directory")
    parser.add_argument("--report", help="Actual UTF-8 report with explicit [E1] or [E1, E2] evidence markers")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        path = Path(args.registry)
        result = verify(json.loads(path.read_text(encoding="utf-8")), Path(args.base_dir) if args.base_dir else path.parent,
                        report=Path(args.report) if args.report else None)
        result["registry_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    except (ValueError, OSError, TypeError, KeyError) as exc:
        result = {"status": "failed", "errors": [str(exc)]}
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": args.output, "status": result["status"]}))
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
