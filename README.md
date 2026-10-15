# EvalSkill

Skills for evidence-grounded evaluation research. The current skill produces complete, claim-specific analyses of scientific benchmarks using **Measurement to Meaning (M2M)**, with explicit evidence checks and data-dependent diagnostics.

**Current version: 5.0.0.** The unchanged v4 skill is preserved at [v4.0.0](https://github.com/ToadPresident/EvalSkill/tree/v4.0.0). This is an independent implementation, not an official release by the M2M authors.

## Start here

- [Skill entrypoint](skills/scientific-benchmark-validity/SKILL.md)
- [Complete English report template](skills/scientific-benchmark-validity/references/report-template.md)
- [Framework and implementation provenance](skills/scientific-benchmark-validity/references/rule-provenance.md)
- [Measurement profile and data contract](skills/scientific-benchmark-validity/references/measurement-profile.md)
- [Analysis routing](skills/scientific-benchmark-validity/references/analysis-routing.md)

## Use the skill

Copy the complete `skills/scientific-benchmark-validity` directory into your agent's configured skills directory, or provide the entrypoint path explicitly in an agent that supports local skill instructions. Keep its references and scripts together. Merely cloning this repository does not install the skill.

Example request:

> Use scientific-benchmark-validity to produce one complete English M2M report on the benchmark described in this paper. Check the source claims, scoring conditions and available response data, explain all five validity dimensions for each material claim, and distinguish completed analysis from proposed studies.

A benchmark name, paper, link or evidence folder is enough to start. Version, claims and intended use may be specified when important. Reports default to **English**, even when the request is in Chinese; explicit Chinese or bilingual output is supported. One request may contain several internal reading, checking, computation and review steps. Missing data do not prevent a complete document-based report.

## What v5 does

- Preserves claim ownership, scope and the use being assessed.
- Examines content, criterion, construct, external and consequential validity with evidence, inference, gaps/satisfaction conditions, judgment reasons and revision conditions.
- Records system configuration, task hierarchy, scoring, repeated versus aggregated responses and source versions before selecting an analysis.
- Separates source integrity, factual accuracy, relevance to the claim and actual computational execution.
- Audits CSV observations and, when justified, computes binary response/repetition summaries and paired task/cluster bootstrap intervals.
- Returns numerical findings to the relevant claim; it does not turn a statistical output into a universal validity score.

M2M principles, independently sourced statistical methods and our implementation choices are identified separately. IRT, factor analysis and G-theory are conditional method guidance, **not bundled executable implementations**. There is no automatic torch_measure integration, hosted service or model API dependency.

## Local helpers

The helpers require Python 3.10+ and use only the standard library. PDF reading and report generation are performed by the host agent using its available tools.

From the skill directory, with your reviewed profile and data:

```sh
python3 scripts/measurement_tools.py audit --csv responses.csv --profile profile.json --output audit.json
python3 scripts/measurement_tools.py diagnose --csv responses.csv --profile profile.json --output diagnostics.json --bootstrap 2000 --seed 17
python3 scripts/verify_evidence.py --registry evidence.json --output evidence_check.json
```

Read the [response diagnostic method](skills/scientific-benchmark-validity/references/response-diagnostics.md) and [evidence registry contract](skills/scientific-benchmark-validity/references/evidence-worksheet.md) first. Profiles declare column meaning and data origin; the helpers cannot establish those facts by inspecting identifiers. No downloading, missing-to-zero conversion or automatic simulation fallback occurs. Explicit synthetic demonstrations remain labelled as such.

The evidence helper checks file/excerpt/reference integrity. It does not certify source-page attribution, numerical qualifiers or scientific inference. The diagnostic helper's uncertainty is conditional on the declared resampling design and does not include every uncertainty source.

## Validation

Run the synthetic software invariants from the repository root:

```sh
python3 -m unittest discover -s skills/scientific-benchmark-validity/tests -v
```

Tests cover invalid scores, duplicate observations, version/condition mixing, explicit ungraded attempts, missingness, repeat weighting, resampling units, synthetic provenance and evidence integrity. They are software checks, not proof of scientific validity or better agent reports.

The development protocol uses a fixed-source CORE-Bench comparison and GPQA regression, preserving first completed reports before outside review. Both are known development cases; case calibration does not establish unseen-benchmark effectiveness. Raw reports and primary materials are retained outside this clean distribution. See [CHANGELOG](CHANGELOG.md) for released changes and the validation scope.

## Repository scope

Included: reusable English skill instructions, report template, method references, original helper code, synthetic tests and maintenance documentation.

Excluded: papers, benchmark datasets, participant records, transcripts, model outputs, case reports, local execution paths, credentials and generated artifacts. The repository does not run benchmark agents or publish any user's analysis automatically.

## Sources and citation

For the analytical framework, cite [Measurement to Meaning: A Validity-Centered Framework for AI Evaluation](https://arxiv.org/abs/2505.10573v4). For this implementation, cite EvalSkill with its version or commit. The [rule register](skills/scientific-benchmark-validity/references/rule-provenance.md) links the method sources and design influences, including AI Measurement Science, Measurement Data Bank, Benchmark Caliper, SkillXiv and Paper2Agent.

No third-party source code or datasets are bundled. Linked works retain their own terms. A project-wide redistribution license has not yet been selected.
