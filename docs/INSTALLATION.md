# Install and use EvalSkill

The package follows the [Agent Skills specification](https://agentskills.io/specification). The same English `SKILL.md`, references and helpers are used across hosts. `agents/openai.yaml` is optional Codex presentation metadata, not a dependency of the method.

## One installation command

Open a terminal in the project where you will analyze benchmarks:

```sh
npx skills@1.7.2 add ToadPresident/EvalSkill --skill scientific-benchmark-validity
```

The installer lets you choose an agent and installation options. It may detect that it is itself running inside an agent and install non-interactively. Use an explicit target when you want a predictable demonstration:

```sh
npx skills@1.7.2 add ToadPresident/EvalSkill --skill scientific-benchmark-validity --agent codex
```

Replace `codex` with the relevant target below. Omit `--global` for project scope; add `--global` for all your projects. `--copy` avoids symlinks. `--yes` skips installer questions; it does not change the host agent's execution permissions. Git and Node.js 22.20+ are required by the tested Skills CLI version, not by the analysis instructions.

| Host | Skills CLI target | Manual project folder | Official discovery reference |
|---|---|---|---|
| Codex | `codex` | `.agents/skills/` | [OpenAI](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) |
| Claude Code | `claude-code` | `.claude/skills/` | [Anthropic](https://code.claude.com/docs/en/skills) |
| Cursor | `cursor` | `.agents/skills/` or `.cursor/skills/` | [Cursor](https://cursor.com/docs/skills) |
| Gemini CLI | `gemini-cli` | `.agents/skills/` or `.gemini/skills/` | [Google](https://geminicli.com/docs/cli/skills/) |
| GitHub Copilot | `github-copilot` | `.agents/skills/` or `.github/skills/` | [GitHub](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| OpenCode | `opencode` | `.agents/skills/` or `.opencode/skills/` | [OpenCode](https://opencode.ai/docs/skills/) |

These paths are documented for current skill-capable releases, checked on 15 October 2026. Several hosts share `.agents/skills`; six supported targets do not require six different implementations. Remote/cloud agents need the skill inside their own project or supported synced environment; copying a folder on your laptop does not deploy it remotely.

## Manual installation, without Node.js

Download the repository ZIP from GitHub or clone it. Copy the **entire** `skills/scientific-benchmark-validity` folder into the project folder in the table. For example, the final Codex layout is:

```text
your-project/
  .agents/skills/scientific-benchmark-validity/
    SKILL.md
    references/
    scripts/
    agents/
    tests/
```

Keep the bundled files together. Copying only `SKILL.md`, or merely cloning EvalSkill elsewhere, is insufficient for normal discovery. The same folder-copy procedure works on Windows, macOS and Linux. No Python package installation is required; optional helpers use only Python's standard library.

## First use

Open a new agent session in the project and ask:

> Use scientific-benchmark-validity to analyze GPQA in one complete English M2M report. Explain what the score measures, which claims it can support, the evidence and gaps in each dimension, and the basis for each judgment.

Codex CLI/IDE can explicitly select `$scientific-benchmark-validity`; Claude Code can use `/scientific-benchmark-validity`. In other hosts, select the installed skill or name it in the request. Confirm the host actually loads the entrypoint; installation alone does not prove activation.

Add `Write the report in Chinese` or `Provide a bilingual report` when needed. Supply a paper/PDF or evidence folder if the agent cannot retrieve sources. It should identify the missing access rather than fabricate a source-based report. A missing Python runtime blocks optional helper calculations, not the document-based path.

## Repeatable demo or research setup

Pin the source release instead of using the changing default branch:

```sh
npx skills@1.7.2 add https://github.com/ToadPresident/EvalSkill/tree/v5.1.0/skills/scientific-benchmark-validity --agent codex --copy --yes
```

Use `v5.0.0` or `v4.0.0` to reproduce an earlier package. Record the actual model, host version, source packet and invocation when comparing analytical outputs; identical installation does not control those variables.

## Inspect, update and remove

```sh
npx skills@1.7.2 list
npx skills@1.7.2 remove scientific-benchmark-validity --agent codex
```

Use the same scope as the installation (`--global` when applicable). To upgrade a pinned installation, install the desired tag explicitly after preserving any local edits. For manual copies, remove only this skill's folder. The installer does not modify `AGENTS.md`, `CLAUDE.md` or `GEMINI.md`.

## If it does not appear

1. Check that the complete folder is in the current project's discovery path.
2. Check the agent version and whether skills are enabled. Older versions may not implement the current documented feature.
3. Refresh skills or start a new session. In current Gemini CLI, `/skills reload` refreshes discovery; the tested local Gemini 0.20.0 predates the current skills management command.
4. Inspect duplicate versions in project/user folders and select the intended one. Do not change unrelated settings to force activation.
5. Check host permissions for the skill and source files. A skill does not override those permissions.

The [installation check](../scripts/check_installation.py) uses Skills CLI 1.7.2 with telemetry disabled in a temporary project, compares installed bytes, and invokes each bundled helper's help command from outside the skill folder. Native host discovery and full analytical runs are separate checks; see [validation](../VALIDATION.md).
