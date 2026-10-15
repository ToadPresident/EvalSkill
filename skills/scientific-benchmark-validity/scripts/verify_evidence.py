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


def verify(registry, base):
    errors, checks, seen = [], [], set()
    sources = {}
    for source in registry.get("sources", []):
        sid = source.get("id")
        if not sid or sid in sources:
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
        if not eid or eid in seen:
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
            errors.append(f"Report refers to unknown evidence ID {reference}")
    return {"status": "failed" if errors else "passed", "errors": errors, "checks": checks,
            "scope": "Integrity only. A matching excerpt is not verification of its stated page, factual qualifiers, independence or inference. Review statuses are declarations, not automated certification. Zero extracted evidence is not proof of absence."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True)
    parser.add_argument("--base-dir", help="Defaults to the registry directory")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        path = Path(args.registry)
        result = verify(json.loads(path.read_text()), Path(args.base_dir) if args.base_dir else path.parent)
        result["registry_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    except (ValueError, OSError, TypeError, KeyError) as exc:
        result = {"status": "failed", "errors": [str(exc)]}
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n")
    print(json.dumps({"output": args.output, "status": result["status"]}))
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
