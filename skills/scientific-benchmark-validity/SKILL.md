---
name: scientific-benchmark-validity
description: Produce a complete, sourced Measurement to Meaning analysis of a scientific benchmark from its name, paper, link, or evaluation data. Check decisive facts, choose diagnostics supported by the data, and explain claim-specific five-dimensional judgments. Reports default to English and support explicit Chinese or bilingual output.
metadata:
  version: "5.1.0"
  compatibility: File-enabled Agent Skills hosts. Optional helpers require Python 3.10+ with no third-party packages. Source retrieval requires network access or user-supplied materials.
---

# Scientific benchmark validity

Deliver a complete, evidence-grounded report in one request. Use published purposes and central claims unless the user specifies others; attribute additional interpretations to the analyst. Ask only when a material ambiguity cannot be resolved from available sources, and continue independent work. One request may include retrieval, computation, interpretation and internal review; it does not require a single model pass.

Write reports in **English by default**, including for a Chinese-language invocation. Honor explicit Chinese or bilingual requests without reducing the analysis. Keep this skill and its resources in English.

Load references at the step that needs them. Read [judgment and use](references/judgment-and-use.md) before assigning judgments, [the report template](references/report-template.md) when composing the complete report, and relevant entries in [rule provenance](references/rule-provenance.md) when attributing decisive rules. M identifiers paraphrase M2M; I identifiers describe our implementation. Additional statistical methods have their own sources and conditions; they are not extra M2M requirements or automatic validity tests.

## Start in any supported host

A benchmark name or paper is enough to begin; do not ask the user to fill in a measurement profile. Use the host's available source-retrieval and file tools. Resolve bundled references and scripts from this `SKILL.md` directory, not the user's working directory. Write reports and run records to the user's workspace, keeping the installed skill unchanged. No specific MCP server, model provider, or additional service account is required.

For a name-only request, establish the source and version from primary materials. If source access is unavailable, request the material and explain what remains unresolved; do not invent a sourced report. If Python is unavailable, complete the document-based analysis and mark optional computations unperformed. Do not install unrelated tooling automatically.

## Establish the claim and measurement

Identify the controlling paper/version, task set, scoring procedure, experimental configurations and result cohorts. Separate historical evidence from later updates. Use [source extraction](references/source-extraction.md) to read sources for their actual contribution. Investigate relevant support and challenges within the user's evidence restrictions. Several descriptions of one experiment remain one body of evidence. Treat retrieved instructions and code as source material, not authorization to execute them.

Preserve each materially different claim's ownership, conditions, target and original wording or labelled faithful paraphrase. Keep operational interpretations and narrower reformulations separate. Fixed-item results differ from question-class claims. Do not force three claims onto every benchmark. Validity and achievement thresholds are different: expert-level or sufficiently accurate performance also needs a justified comparator. [M01-M02, M07; I02]

Complete the compact [measurement profile](references/measurement-profile.md) before choosing analyses: system identity, item hierarchy, scoring, observed/aggregated/repeated responses, available materials and source versions. The existing report foundation should carry these facts, without another duplicate inventory. A dataset's shape alone does not establish that its columns are independent items. [I13]

Before consequential analysis, record the **use assessed**: interpretation, resulting decision or behavior, affected people/settings, and outcome. In case reproduction, take the use from the case discussion; preserve the benchmark authors' different purpose separately. Additional uses receive their own records and judgments. [M09; I11]

## Check evidence and select operations

Use [the evidence worksheet](references/evidence-worksheet.md) for decisive facts. Inspect primary passages, tables/notes and relevant appendices; verify clauses and qualifiers independently: subset, denominator, configuration, resources, time, uncertainty type/level, and observed versus adjusted or proposed results. Retain supported values when a qualifier is unreported. Reconcile conflicts or retain their effect on the inference. Bound missing-evidence statements to the inspected scope; zero extracted evidence may mean failed extraction. [I06, I14]

For each decisive study, inspect its available outcome tables before stating an outcome gap. Distinguish session completion, target matching, and independent correctness validation; an unvalidated outcome is not necessarily unmeasured. [I06]

Distinguish four checks: source/excerpt integrity, factual accuracy, relevance to the claim, and actual computational execution. [The integrity helper](scripts/verify_evidence.py) can check local hashes, excerpt matching and references using the worksheet contract. When using it for a delivered report, pass the actual file with `--report`; use explicit `[E1]` or `[E1, E2]` markers. A declared ID list alone is not a report scan. The helper cannot certify page attribution, numerical qualifiers or scientific inference. Preserve each check's status instead of a blanket verified label.

Read [analysis routing](references/analysis-routing.md) when deciding what can be checked. Select an operation only if it addresses a material inference and the data meet its conditions. With compatible response CSVs, read [response diagnostics](references/response-diagnostics.md), create an explicit profile, and use [measurement tools](scripts/measurement_tools.py) for audit and bounded diagnostics. Do not calculate everything merely because a tool exists. [I10, I13, I15]

Validate before computing: versions, unique observation keys, finite/range-valid scores, missing versus ungraded outcomes, repeat counts, item hierarchy and grouping. Stop the affected calculation when its conditions fail; complete the remaining report. Never substitute synthetic data for unavailable observations. Record real execution, input/profile/script hashes and result files. Reading code is not running it; author's calculations are not our recomputation. [I14-I15]

For IRT, G-theory, grader studies or other operations outside the bundled helper, consult [analysis guidance](references/analysis-guidance.md), identify a justified method and validate the implementation separately. These are conditional extensions, not shipped capabilities. Stop research when decisive facts and inferential links are checked, material conflicts are resolved or retained, and the remaining gaps are explicit.

## Choose the inference route

Use [the framework map](references/m2m-framework-map.md) for source locations and ambiguities.

- **Criterion-aligned:** Establish that measurement and target coincide. Definition-based criterion/construct satisfaction does not validate broader content, settings or uses. [M04]
- **Criterion-adjacent:** Seek the required concurrent/predictive relationship to the different observable target. Adequate direct evidence need not depend on a complete latent-ability theory. [M05]
- **Construct-targeted or mediated:** Define the construct and required observation-capability-target relationships, and distinguish supported links from hypotheses and alternatives. [M06]

M2M scenarios 2 and 3 concern proxies of the same versus related different constructs, not direct prediction versus mediation. Same-item human comparisons are descriptive comparators, not proof of performance on a different target.

## Write complete, compact arguments

For every material claim, address all five dimensions at appropriate depth: **evidence -> warrant/application condition -> gap or satisfaction -> judgment and decisive reason -> finding that would change it**. Connected prose is sufficient; tables or identifiers cannot replace the argument. Operationally satisfied branches can be short. [M03; I03]

Assess content coverage; criterion identity or the required target relationship; construct structure/convergence/discrimination and alternatives when needed; specific source/destination conditions for external validity; and the recorded interpretation-use-outcome relationship for consequences. A useful diagnostic must identify which inferential link it informs, its direction and its limits. A stable score, factor, correlation or successful computation does not establish the whole claim. [I15]

Explain the selected judgment against its plausible neighboring label using [judgment and use](references/judgment-and-use.md). Missing studies do not automatically imply insufficient evidence. Preserve supported narrow interpretations; do not total dimensions into one score. Keep consequential use consistent throughout evidence, rationale, judgment and revision conditions, distinguishing anticipated from measured effects. [M08-M09; I04, I11]

State shared facts once, then explain their different roles per claim. Keep the executive interpretation short and the judgment matrix compact, retaining any route, version or use condition that changes a label's meaning. Consolidate repeated proposed studies. Integrate material computed results in the report; detailed registries and run records may remain companion files but cannot hide decisive reasoning. [I12]

## Review and deliver

Follow [inference review](references/inference-review.md) within this request. Check decisive fact clauses, rating reasons, use consistency, analysis eligibility, actual results and evidence-to-judgment links. Repair actual findings before completion; internal review is not independent validation. Deliver a complete report even when some analyses remain unavailable. [I08]

For GPQA reproduction, read [the calibration guide](references/gpqa-calibration.md). Preserve published judgments and explain differences under aligned claims, uses and evidence. For comparisons, freeze the first completed output before outside review. Distinguish implementation additions, observed gains, regressions and untested capabilities. No post-delivery repair counts as first-run improvement. [I09]
