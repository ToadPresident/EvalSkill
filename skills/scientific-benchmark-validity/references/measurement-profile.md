# Measurement profile

Use this as a compact working record, reflected in the report's measurement foundation. It is our I13 implementation, informed by the AI Measurement Science data inventory and Measurement Data Bank. It is not a form the user must complete.

Record the benchmark and paper versions, task/subset definitions, source revision/date, score definition and aggregation, and available evidence. Distinguish original item counts, current task sets and result-file observations.

Describe **system** as the measured configuration (model, scaffold, tools and material settings), **item** at its actual level (question, capsule, paper, rubric leaf), and **score** as single outcome, repeated rate, partial credit or aggregate. Retain parent-child relationships and repeats before constructing any matrix. The role of a scaffold depends on the question: system identity for a comparison of agents, or a varying facet in a scaffold study.

List available materials separately: documents/items, aggregate results, item responses, repeat/rater information, traces/artifacts, and independent target outcomes. These are capabilities, not a quality ladder. A paper-only case still warrants a complete report. A response matrix does not supply missing construct or use evidence.

## Executable CSV profile

The bundled helper accepts UTF-8 CSV and JSON, using Python 3.10+ standard library. Adapt column names explicitly; do not rewrite source data or silently average it. One profile selects one coherent analysis slice. Below is a **synthetic schema example**, not empirical data:

```json
{
  "schema_version": 1,
  "benchmark": {"name": "Example", "version": "revision-A"},
  "data_origin": "synthetic",
  "source": {"url": "https://example.org/data", "sha256": "<actual input SHA256>"},
  "units": {
    "system": "Full agent configuration, including model and scaffold",
    "item": "Independent task; no shared parent task in this example",
    "score": "Official single-trial binary success"
  },
  "columns": {"system": "system_id", "item": "task_id", "trial": "trial_id", "score": "success"},
  "condition": "fixed scorer and resources",
  "filters": {"split": "evaluation"},
  "score_scale": {"kind": "binary"},
  "score_mapping": {"True": 1, "False": 0},
  "resampling": {"unit": "item", "justification": "Task sampling is the declared uncertainty target; observed repeats are held fixed"}
}
```

Use `data_origin: observed` only for actual observations. An author-produced table remains author data; script results are our recomputation of that table, not new experiments. A stored hash establishes byte identity, not truthful provenance or semantics. Source hash is optional for exploration but required for frozen comparisons.

Optional columns: `condition`, `version`, `cluster`, `status`. A `version` column must match the declared benchmark version. Multiple conditions need separate filtered profiles for diagnostics. Filter values are exact CSV strings, or lists of strings. With no trial column, the helper permits only one observation per system/item/condition/version. Identity columns must be nonempty.

Blank score means an ungraded attempt **only** with an explicit `status` column whose value is `ungraded`. No row means no available observation. `NaN`/infinity are rejected, not converted to failures. If the source uses other missing codes, document a reviewed conversion before invoking the helper. Non-binary data can be audited with `interval` (finite `min`, `max`) or `discrete` (`values`), but the bundled diagnostic does not threshold or fit them.

Use `resampling.unit: none` when no sampling interpretation is justified. For related tasks/rubric leaves, retain `columns.cluster` and consider `unit: cluster`; verify the clusters actually match the uncertainty question. The helper cannot infer independence from identifiers. Trial IDs are labels, not interchangeable judges or shared random seeds.

## Sources and adaptation

- [AI Measurement Science, Chapter 2](https://aimslab.stanford.edu/textbook/src/chap2.html): subject/item meaning, response structure, scoring variants and missingness.
- [Measurement Data Bank schema](https://github.com/aims-foundations/measurement-db/blob/ff987fc4213845374a7eeb50b9f7923a7bd9d178/parquet_schemas.yaml): scoring protocol identity and observed/ungraded/unavailable distinctions.
- [Characterization schema](https://github.com/aims-foundations/measurement-db/blob/ff987fc4213845374a7eeb50b9f7923a7bd9d178/characterization_schema.yaml): reported versus data-derived numeric claims and source locators.

Our lightweight profile is not an implementation of their full schema. We ship no third-party datasets or code.
