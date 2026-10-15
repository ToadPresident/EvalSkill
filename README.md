# EvalSkill

Understand what a scientific benchmark measures, how its score is produced, and which claims the evidence supports. Give your coding agent a benchmark name, paper or result files; EvalSkill applies **Measurement to Meaning (M2M)** to produce one complete, sourced analysis.

**Current version: 5.1.0.** Earlier releases remain available at [v5.0.0](https://github.com/ToadPresident/EvalSkill/tree/v5.0.0) and [v4.0.0](https://github.com/ToadPresident/EvalSkill/tree/v4.0.0). This is an independent implementation, not an official release by the M2M authors.

## Install, then ask

From the project where you want to use the skill:

```sh
npx skills@1.7.2 add ToadPresident/EvalSkill --skill scientific-benchmark-validity
```

Choose your agent in the installer. Supported installation targets include **Codex, Claude Code, Cursor, Gemini CLI, GitHub Copilot and OpenCode**. This route uses the [Skills CLI](https://github.com/vercel-labs/skills) and needs Node.js 22.20+ and Git. No additional model account, API key or MCP service is needed by EvalSkill. [Manual installation without Node, agent-specific commands, version pinning and troubleshooting](docs/INSTALLATION.md) are available.

Then ask your agent:

> Use scientific-benchmark-validity to help me understand CORE-Bench. Produce one complete English report explaining its tasks, scoring, main claims, evidence and all five M2M dimensions. Identify the paper and benchmark version before interpreting results.

You can start with a name alone. The agent gathers the measurement details; you do not need to fill in a profile. It needs source access, or materials you supply. Python 3.10+ is needed only for optional bundled data checks. Reports default to English; explicitly request Chinese or bilingual output when wanted.

See the [demonstration guide](docs/DEMO.md) for a short installation-to-analysis walkthrough. Installation tests and analytical-quality tests are reported separately in [VALIDATION.md](VALIDATION.md).

## Start here

- [Skill entrypoint](skills/scientific-benchmark-validity/SKILL.md)
- [Complete English report template](skills/scientific-benchmark-validity/references/report-template.md)
- [Framework and implementation provenance](skills/scientific-benchmark-validity/references/rule-provenance.md)
- [Measurement profile and data contract](skills/scientific-benchmark-validity/references/measurement-profile.md)
- [Analysis routing](skills/scientific-benchmark-validity/references/analysis-routing.md)

## Input and output

Optional inputs include a particular claim, intended use, version, task examples or response CSV. Without a user-specified use, the report explains published purposes and claims rather than inventing a deployment decision. One request may contain retrieval, computation and internal review.

The complete report explains the measurement process, attributed claims, five-dimensional evidence and inference, reasons for each judgment, supported narrower conclusions, and the evidence that would change them. Relevant diagnostics and exact source locations accompany the reasoning. Missing response data do not prevent a document-based report. An interactive visual companion is a [planned extension](docs/DEVELOPMENT.md), not a shipped renderer.

## What the skill does

- Preserves claim ownership, scope and the use being assessed.
- Examines content, criterion, construct, external and consequential validity with evidence, inference, gaps/satisfaction conditions, judgment reasons and revision conditions.
- Records system configuration, task hierarchy, scoring, repeated versus aggregated responses and source versions before selecting an analysis.
- Separates source integrity, factual accuracy, relevance to the claim and actual computational execution.
- Checks explicit evidence markers in the actual report, retains all-ungraded systems, and optionally compares observed tasks with a versioned expected inventory.
- Audits CSV observations and, when justified, computes binary response/repetition summaries and paired task/cluster bootstrap intervals.
- Returns numerical findings to the relevant claim; it does not turn a statistical output into a universal validity score.

M2M principles, independently sourced statistical methods and our implementation choices are identified separately. IRT, factor analysis and G-theory are conditional method guidance, **not bundled executable implementations**. There is no automatic torch_measure integration, hosted service or model API dependency.

## Local helpers

The helpers require Python 3.10+ and use only the standard library. PDF reading and report generation are performed by the host agent using its available tools.

From the skill directory, with your reviewed profile and data:

```sh
python3 scripts/measurement_tools.py audit --csv responses.csv --profile profile.json --output audit.json
python3 scripts/measurement_tools.py diagnose --csv responses.csv --profile profile.json --output diagnostics.json --bootstrap 2000 --seed 17
python3 scripts/verify_evidence.py --registry evidence.json --report report.md --output evidence_check.json
```

Read the [response diagnostic method](skills/scientific-benchmark-validity/references/response-diagnostics.md) and [evidence registry contract](skills/scientific-benchmark-validity/references/evidence-worksheet.md) first. Profiles declare column meaning and data origin; the helpers cannot establish those facts by inspecting identifiers. No downloading, missing-to-zero conversion or automatic simulation fallback occurs. Explicit synthetic demonstrations remain labelled as such.

The evidence helper checks file/excerpt/reference integrity. It does not certify source-page attribution, numerical qualifiers or scientific inference. The diagnostic helper's uncertainty is conditional on the declared resampling design and does not include every uncertainty source.

## Validation

Run the synthetic software invariants from the repository root:

```sh
python3 -m unittest discover -s skills/scientific-benchmark-validity/tests -v
```

The 37 synthetic tests cover invalid scores, duplicate observations, version/condition mixing, explicit ungraded attempts, missingness, repeat weighting, resampling units, task inventories, malformed input, synthetic provenance and evidence integrity. `python3 scripts/check_installation.py` separately installs the package in a disposable project for six agent targets, compares every packaged file, and loads the installed helpers. It requires the installation prerequisites above and makes no model calls. These are software and packaging checks, not proof of scientific validity or better agent reports.

The development comparison uses fixed-source CORE-Bench reports and GPQA regression, preserving first completed outputs before outside review. See [validation methods and observed results](VALIDATION.md), including retained strengths and regressions. These known cases do not establish unseen-benchmark effectiveness. Raw reports and primary materials are retained outside this clean distribution. See [CHANGELOG](CHANGELOG.md) for released changes.

## Repository scope

Included: reusable English skill instructions, report template, method references, original helper code, synthetic tests and maintenance documentation.

Excluded: papers, benchmark datasets, participant records, transcripts, model outputs, case reports, local execution paths, credentials and generated artifacts. The repository does not run benchmark agents or publish any user's analysis automatically.

## Sources and citation

For the analytical framework, cite [Measurement to Meaning: A Validity-Centered Framework for AI Evaluation](https://arxiv.org/abs/2505.10573v4). For this implementation, cite EvalSkill with its version or commit. The [rule register](skills/scientific-benchmark-validity/references/rule-provenance.md) links the method sources and design influences, including AI Measurement Science, Measurement Data Bank, Benchmark Caliper, SkillXiv and Paper2Agent.

No third-party source code or datasets are bundled. Linked works retain their own terms. A project-wide redistribution license has not yet been selected.
