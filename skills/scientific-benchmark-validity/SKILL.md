---
name: scientific-benchmark-validity
description: Produce a complete, sourced Measurement to Meaning analysis of a scientific benchmark from its name, paper, or link. Verify decisive facts, explain five-dimensional judgments, and keep the intended use consistent. Use for benchmark interpretation and validity case studies. Reports default to English and support explicit Chinese or bilingual output.
metadata:
  version: "4.0.0"
---

# Scientific benchmark validity

Deliver a complete, evidence-grounded report in one request. Use published purposes and central claims unless the user specifies others; attribute additional interpretations to the analyst. Ask only when a material ambiguity cannot be resolved from the available sources, and continue independent work while waiting.

Write the report in **English by default**, including for a Chinese-language invocation. Honor explicit Chinese or bilingual requests without reducing the analysis. Keep this skill and its resources in English.

Read [the report template](references/report-template.md) for delivery, [rule provenance](references/rule-provenance.md) for attribution, and [judgment and use](references/judgment-and-use.md) before deciding ratings. The M identifiers paraphrase M2M; the I identifiers describe our implementation. These identifiers, operational rating definitions, fact checks, use records, and writing conventions are ours, not additional M2M theory.

## Establish the case before judging it

Identify the controlling paper/version, task set, scoring procedure, experimental configurations, and result cohorts. Separate historical evidence from later updates. Read source sections according to what they contribute using [source extraction](references/source-extraction.md), rather than treating a framework's case commentary as a primary experiment. Investigate relevant supporting findings, challenges, and independent validation within the user's evidence restrictions. Multiple descriptions of one experiment remain one body of evidence.

Preserve each materially different claim's ownership, conditions, target, and original wording or labelled faithful paraphrase. Show operational interpretations and narrower reformulations separately. A fixed-item result is different from a claim about a question class. Do not force three claims onto other benchmarks. Separate validity from achievement: expert-level, acceptable, or sufficiently accurate performance also needs a justified comparator or threshold. [M01-M02, M07; I02]

Before consequential analysis, record the **use being assessed**: interpretation, resulting decision or behavior, affected people/settings, and outcome. When reproducing a case, take that use from the case's relevant discussion; the benchmark authors may propose a different purpose. Retain both attributions. An additional research or deployment use gets its own record and judgment. [M09; I11]

## Check facts before using them as premises

Use the clause-level procedure in [the evidence worksheet](references/evidence-worksheet.md). For decision-relevant numbers and protocol statements, inspect the primary passage/table and check qualifiers separately: subset, denominator, configuration, allowed resources, time requirement, uncertainty type/level, and whether a result is observed, adjusted, estimated, or proposed. A nearby citation does not establish every clause in a sentence. If a qualifier is unreported, preserve the supported fact and say what is unspecified instead of inferring it. [I06]

Bind every result to its actual cohort and conditions. Check table notes and appendices when they resolve a material ambiguity. Keep author claims, empirical findings, and analyst interpretations distinct. Reconcile source/version conflicts or retain them explicitly; test whether their resolution changes the inference. Distinguish an untested relationship, a tested failure, and inaccessible evidence. Bound negative evidence statements to inspected sources.

Stop research when central measurement facts are checked, decisive inferential links have received targeted investigation, material conflicts have been resolved or retained, and remaining gaps are clear. Do not stop at citation coverage or continue searching without a decision-relevant question.

## Choose and explain the inference route

Consult [the framework map](references/m2m-framework-map.md) for source locations or routing ambiguities.

- **Criterion-aligned:** State exactly how the measured outcome and target coincide. Criterion/construct satisfaction by definition does not validate broader content, new settings, or uses. [M04]
- **Criterion-adjacent:** Seek a justified concurrent/predictive relationship with the different observable target. Adequate direct evidence can support this route without a complete latent-ability theory. [M05]
- **Construct-targeted or construct-mediated:** Define the construct and the necessary relationships between observations, capability, alternatives, and any downstream outcome. Mark each relationship as hypothesized or empirically supported. [M06]

M2M scenarios 2 and 3 concern proxies of the same versus related different constructs; they are not names for direct prediction versus mediation. Same-item human comparisons can establish a descriptive comparator without establishing a model's performance on a different target.

## Write complete, compact arguments

For every claim, address all five dimensions with depth proportional to the inference. Each substantive dimension must connect **evidence -> warrant/application condition -> gap or satisfaction condition -> judgment and decisive reason -> finding that would change it**. Use connected prose; separate micro-headings for every component are unnecessary. A table or identifier cannot replace the argument. [M03; I03]

Assess coverage for content; identity or the required target relationship for criterion; structure, convergence, discrimination, and alternatives for construct when required; specific origin/destination conditions for external validity; and the recorded interpretation-use-outcome relationship for consequences. An operationally satisfied dimension needs a short explanation of its condition, not an invented defect or experiment.

Apply [judgment and use](references/judgment-and-use.md) to explain why the evidence warrants the selected label and what separates it from the plausible neighboring label. Missing studies do not automatically determine the rating. Keep evidence direction, availability, and sufficiency separate; preserve supported narrow interpretations when wider ones lack support. Do not total the dimensions into one score. [M08; I04]

For consequences, keep the same use through the evidence, rationale, rating, conclusion, and proposed validation. Distinguish anticipated effects from measured effects. An argument that research is worth doing cannot replace assessment of the original claimed use, and unmeasured impact does not by itself defeat a justified anticipatory argument. [M09; I11]

State shared facts once in the measurement/evidence foundation and cite them by identifier. In each claim, explain their changed inferential role. Keep the executive interpretation short, the matrix label-only, and each claim conclusion usable without restating its five sections. Consolidate repeated proposed studies in one priority table, with local cross-references preserving revision conditions. [I12]

## Review and deliver in the same request

Follow [inference review](references/inference-review.md) before delivering. Check material fact clauses against the sources, every rating's decisive reason, and every consequence argument against its use record. Repair findings within the generation; record actual corrections or unresolved issues, rather than declaring the report error-free. Internal review is part of one-request generation, not independent validation. [I08]

Keep the complete analysis in the report. Working fact records may be separate, but cannot replace missing arguments. Use [analysis guidance](references/analysis-guidance.md) only for authorized calculations that resolve a real question; proposed studies are not completed experiments.

For GPQA reproduction, read [the calibration guide](references/gpqa-calibration.md). Preserve published judgments and explain any differences under aligned claims, uses, and evidence. For a version comparison, freeze the completed original output before outside review, label later corrections separately, and distinguish design changes, observed output changes, and source-supported improvements. Rating agreement, strictness, and shorter length alone are not quality measures. [I09]
