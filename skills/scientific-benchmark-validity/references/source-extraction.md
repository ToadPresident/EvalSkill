# Reading sources by contribution

Use this guide to decide what to extract for the current claim. The roles are our implementation of I05, inspired by SkillXiv. They are reading priorities, not credibility rankings or validity judgments. A single paper can have several roles, and a section may matter more than the paper's overall genre. Confirm roles against the relevant full text.

| Source contribution | Extract | What the source cannot establish merely by having this role |
|---|---|---|
| Methodological framework | Definitions, conditional rules, relationships, scope, worked arguments, and acknowledged limitations. Separate the framework from the authors' case judgments. | Empirical support for every case assertion; a new finding about the benchmark. |
| Benchmark or dataset design | Intended use, task and answer format, sampling, author/annotator selection, validation and filtering, scoring, subsets, denominators, protocol, release, and model configuration. | Broader capability or deployment success from design intention alone. |
| Empirical validation or comparative study | Hypothesis, target relationship, comparison, independent units, outcome definition, uncertainty, selection, controls, and replication scope. | Generalization beyond the tested populations, settings, or relationships. |
| Mechanistic or diagnostic analysis | The proposed explanation, intervention or diagnostic, alternative explanations, controls, findings, and transfer conditions. | A diagnostic association proves a unique causal mechanism or an unrestricted capability. |
| Survey or synthesis | Taxonomy, selection criteria, disagreements, gaps, and pointers to primary studies. | A second independent confirmation when it summarizes an existing experiment. |
| Software, protocol, or evaluation infrastructure | Versioned scoring behavior, execution path, resource settings, dependencies, reproducible inputs/outputs, and known defects. | Successful execution proves the scientific interpretation is valid. |
| Use or impact study | User population, decision informed by the score, comparison, observed effects, implementation conditions, and unintended effects. | Plausible expected benefits are measured causal effects. |

## Extraction record

For each source that determines a conclusion, retain its role, the exact passage/table/code location, the extracted observation or principle, its conditions, the link it informs, and its inferential ceiling. The evidence worksheet provides a compact record. Summarize source roles in the report when they clarify attribution; do not turn every source into an additional essay.

Use two separate decisions:

1. **What can this material contribute?** This determines reading and extraction.
2. **What does this claim require?** M01-M10 determine the validity argument.

For instance, a benchmark's expert/non-expert comparison may inform difficulty and content relevance. Its existence alone does not establish a relation between AI scores and a different target outcome. To support that relation, inspect a study that actually tests it or state the scoped gap.

When the paper does not explain a design choice, extract the choice as documented. Any rationale supplied by the analyst remains an explicitly labelled interpretation, not an author finding. A statement of intention, an empirical result, and a normative recommendation require different attribution.

If a source combines framework exposition and case analysis, preserve that separation. Do not turn the case's ratings into universal rules, and do not silently resolve conflicts with primary protocols in favor of the framework paper.

## Research stopping rule

For a normal report, investigate decisive missing relationships and material source conflicts. Stop when the measurement facts are checked, targeted investigation addresses the claim's central links, and remaining uncertainty is bounded. Under a user-specified evidence restriction, produce the complete analysis within that scope and identify the consequence of the restriction. Do not invent an external validation or treat failure to inspect one as a demonstrated empirical failure.
