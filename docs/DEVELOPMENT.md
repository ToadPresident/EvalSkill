# Design review and next evidence

This document separates implemented v5.1 refinements from proposed research and presentation work. v5.0.0 and its first-completed CORE-Bench/GPQA reports remain unchanged. The underlying M2M framework, five dimensions and qualitative judgments are retained.

## What to preserve

- M2M principles and implementation choices have separate provenance.
- Claims retain ownership, target, version and intended use.
- Sources are read for their contribution rather than treated as interchangeable evidence.
- The required inference and available data jointly determine the analysis.
- Integrity, fact accuracy, inferential relevance and execution are separate checks.
- A justified narrow conclusion can be supported; stricter ratings are not inherently better.

## How the external designs inform this work

| Reference | Design lesson | EvalSkill implication |
|---|---|---|
| [Paper2Agent, Nature, Discussion and Methods](https://www.nature.com/articles/s41586-026-11044-y) | Reusable tools require execution checks; agreement with one reference does not exhaust analytical validity for open questions. | Preserve executable checks and inspectable outputs, while evaluating argument quality and justified disagreement separately. Its MCP architecture is not required here. |
| [SkillXiv Paper2Skill v0.0.3](https://github.com/ADu2021/skillXiv/blob/main/paper2skill/paper2skill-v0.0.3/SKILL.md) | Contribution type selects the extraction procedure and relevant resources. | Keep contribution-aware source reading; do not duplicate its entire category system or licensing choices. |
| [SkillsBench v4, §5.1.3, §6 and Appendix F.3](https://arxiv.org/html/2602.12670v4) | Heavy pipelines, displaced native strategies and brittle solvers can reduce performance; host loading matters. | Keep a document-only path, defer optional work, and distinguish installation from actual invocation. These findings motivate tests; they do not prove EvalSkill was harmed by its document length. |
| [Agent Skills specification](https://agentskills.io/specification) | Standard package structure and conditional resource access support reuse. | Use one provider-neutral package, relative resource paths and small optional helpers. |

Design alignment supports the rationale for these choices. It is not an effectiveness result for EvalSkill.

## Implemented in v5.1

| Observation or requirement | Change | Evidence available now |
|---|---|---|
| A registry could pass while an uninspected report cited an unknown E ID. | Optional `--report` reads and hashes the actual report; explicit markers are checked; no-file status is `not_checked`. | Synthetic report/registry mismatch regressions. |
| An entirely ungraded system disappeared from diagnostics. | Keep attempt/ungraded counts and `null` scores, including all-ungraded panels. | Synthetic missingness regressions. |
| Constant and column condition declarations could disagree silently. | Require agreement when both are supplied. | Matching and conflicting inputs tested. |
| Malformed profile objects could crash before a failure record. | Validate object structure before field access. | CLI failure-record tests. |
| A task missing from every system was outside observed-table coverage. | Optional versioned expected item inventory; report observed-only scope otherwise. | Entire-column omission and identity tests. |
| CORE v5 omitted an available study outcome table; GPQA's matrix lost a condition. | Explicit outcome-table review and condition-preserving summary instructions. | Instruction changes only; report-quality effects have not been retested. |
| Installation required users to work out host paths. | One-command Skills CLI route, manual alternative, version pinning, demonstration guide and install CI. | File installation/identity checks, separate from model runs. |
| All detailed references loaded at entry. | Load judgment rules, provenance and template at their relevant steps. | No measured token/cost or accuracy improvement claimed. |

## Next: make existing analysis easier to explore

Keep the complete report. Add a one-page HTML entrance generated from the same reviewed records, without a second set of ratings. The useful views are:

1. **Task and scoring process:** distinguish what is provided, what the agent must do, and what the scorer directly checks.
2. **Claim–evidence relationship:** selecting a claim exposes its inference route, evidence, application conditions, alternatives and unresolved link.
3. **Coverage comparison:** show benchmark tasks against an explicitly stated target scope; do not invent a percentage of scientific ability covered.
4. **Concrete task/result view:** show genuine task input, available output and scoring basis. If logs are absent, show scoring structure only.

Connect C/U/E/A identifiers to report anchors and primary-source locators. Preserve conditions in both views. Any user-edited claim or use creates a revised analysis state; it should not silently modify the frozen original. The HTML renderer and shared structured analysis schema are not yet implemented.

A related verification increment would bind computed evidence to a pinned output file, a result key/value and an execution record. The current report scanner validates explicit E references, not numerical entailment or automatic execution provenance.

## Next: a public, inspectable evaluation package

Keep research artifacts outside the installed skill. Publish a separate, curated package containing permitted source links/versions, exact prompts, first-completed reports, review findings, separately labelled corrected reports, host/model versions and measured time/cost where available. Missing historical metadata should remain missing, not reconstructed as if recorded. Primary papers and private transcripts need not be copied into it.

For a controlled comparison, hold source access, model, tools, request and budget rules constant:

- A: benchmark materials only.
- B: the same materials plus the original M2M paper.
- C: the same primary sources and M2M access plus EvalSkill.
- Optional D: the skill's exact content supplied as an ordinary prompt, to isolate packaging from content.

B versus C is central to the operationalization claim. Keep GPQA and CORE-Bench as known regressions; reserve a benchmark not used during development for transfer. Freeze first completions, record failures and allow justified analytical disagreement. Evaluate facts, evidence relevance, conditions, scope and decisions rather than label matching alone.

Use paired input changes to test behavior: widen a claim while preserving scores; add relevant supporting evidence; remove item responses; change the use; duplicate a source describing the same experiment; replace a completed computation with a failed one. Each should change only the inferential relationships warranted by the change.

For the visual companion, compare the same content as text versus text-plus-diagrams. Ask researchers to identify scoring units, retrieve supporting evidence, detect an unsupported generalization and choose a useful next check. Preference ratings alone do not establish understanding.

## Research narrative

The intended contribution is a **portable, evidence-traceable operationalization of claim-dependent benchmark validity reasoning**, followed by evidence that researchers can apply it accurately. Portability demonstrates accessibility. Controlled analytical and comprehension evaluations are needed to establish the method's added value. A project-wide redistribution license remains an owner decision, separate from the technical installation path.
