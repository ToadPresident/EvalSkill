#!/usr/bin/env python3
"""Check the real Skills CLI install path in a disposable project, without model calls."""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

NAME = "scientific-benchmark-validity"
CLI_VERSION = "1.7.2"
ROOTS = {
    "codex": ".agents/skills", "claude-code": ".claude/skills",
    "cursor": ".agents/skills", "gemini-cli": ".agents/skills",
    "github-copilot": ".agents/skills", "opencode": ".agents/skills",
}


def manifest(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()
            and "__pycache__" not in p.parts and p.suffix != ".pyc" and p.name != ".DS_Store"}


def main():
    repo = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=str(repo), help="Local repository or a pinned GitHub tree URL")
    parser.add_argument("--output", help="Optional JSON result file outside the disposable project")
    args = parser.parse_args()
    npx = shutil.which("npx")
    if not npx:
        parser.error("This installation check needs Node.js 22.20+ with npx, and Git; manual folder copying does not")
    expected = manifest(repo / "skills" / NAME)
    result = {"status": "failed", "skills_cli": CLI_VERSION, "targets": list(ROOTS),
              "scope": "Project installation, byte identity and helper loading; no model inference or native-host discovery"}
    try:
        with tempfile.TemporaryDirectory(prefix="evalskill-install-") as temporary:
            project = Path(temporary)
            command = [npx, "--yes", f"skills@{CLI_VERSION}", "add", args.source,
                       "--skill", NAME, "--agent", *ROOTS, "--copy", "--yes"]
            env = {**os.environ, "DO_NOT_TRACK": "1"}
            install = subprocess.run(command, cwd=project, env=env, capture_output=True, text=True,
                                     encoding="utf-8", errors="replace", timeout=180)
            if install.returncode:
                raise ValueError(f"Skills CLI failed ({install.returncode}): {install.stdout}\n{install.stderr}")
            checks = []
            for agent, relative in ROOTS.items():
                installed = project / relative / NAME
                actual = manifest(installed)
                if actual != expected:
                    raise ValueError(f"{agent}: installed file manifest differs from the source package")
                checks.append({"agent": agent, "project_path": f"{relative}/{NAME}",
                               "files": len(actual), "sha256_match": True})
            for relative in sorted(set(ROOTS.values())):
                for helper in ("measurement_tools.py", "verify_evidence.py"):
                    subprocess.run([sys.executable, str(project / relative / NAME / "scripts" / helper), "--help"],
                                   cwd=project, check=True, capture_output=True, timeout=20)
            result.update(status="passed", checks=checks, installed_helpers_load=True,
                          note="Five targets share the documented .agents/skills root; Claude Code also receives its native copy.")
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        result["error"] = str(exc)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
