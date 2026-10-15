# Analysis routing

Read after establishing the claim and measurement profile. Choose an operation by the intersection of **a material inference question** and **available, adequate observations**. Do not treat methods as required report sections or data richness as a validity rating.

| Question and available materials | Candidate check | Decision condition and output |
|---|---|---|
| What do authors claim; what is covered? Documents, items, rubrics | Source and coverage review | Compare sampled work and grading with the specific claim. Report observed coverage, assumptions and omissions. |
| Are reported scores comparable? Aggregate results | Version/configuration/denominator audit | No reconstruction of item structure from totals. Preserve inconclusive comparisons. |
| What response pattern supports a performance claim? Item-level responses | Audit, descriptive item/cell summaries, justified paired uncertainty | Check identity, scale, missingness and hierarchy first. Describe the frozen panel and retain alternatives. |
| Is behavior stable over repeated trials? Actual repeated responses | Observed any/all/mixed outcomes; conditional task bootstrap | These are empirical repetition summaries, not a fitted reliability coefficient or independent deployment probability. |
| What produces score variability? Appropriate crossed/nested observations | Design-specific G-study or mixed model | Identify estimable facets, measurement object, fixed/random conditions and interactions; validate implementation separately. No generic G-study is shipped. |
| Do response structures support a construct? Adequate systems/items or matched multi-instrument data | IRT, factor/MTMM or convergent/discriminant study | Need a hypothesis, fit/identifiability/uncertainty checks and competing explanations. Factor naming and correlations alone are insufficient. |
| Does the score predict a different target? Matched independent target observations | Concurrent/predictive validation | Establish subject correspondence, target quality, conditions, uncertainty and transfer scope. A group benefit study is not automatically benchmark-score prediction. |
| Was the intended work actually done? Traces, saved artifacts and grading | Trace/artifact/scorer review | Keep execution, artifact production and scientific adequacy distinct. Published descriptions can be reported without claiming direct artifact inspection. |

For each selected or material unavailable analysis, record an A identifier: question and C/U link, input/source IDs, availability and assumptions, operation, actual status, result file (if executed), and the resulting change or limit in the claim. Statuses are `author_reported`, `completed`, `not_executed`, `failed`, `unavailable`, or `simulation`. A script's presence does not imply completion. An operational identity argument does not need a statistical model.

Use the bundled [response diagnostic method](response-diagnostics.md) only within its supported scope. For other authorized calculations, [analysis guidance](analysis-guidance.md) specifies important conditions but is not a tested software implementation. The current [torch_measure quickstart](https://github.com/aims-foundations/torch_measure/blob/a461a8f24eb2960f692afdac0a2202c7d1d507ad/docs/source/quickstart.rst) returns long-form data before an explicit matrix conversion; library integration requires a separately pinned and checked adapter.

## Evidence changes must change the right argument

Map each result to the relationship it informs. Within-task inconsistency may qualify a stable-performance claim, but does not itself establish a content omission. Better precision on the same items does not demonstrate transfer. An independent prediction result can strengthen a criterion link without resolving a different consequential use. Findings can strengthen as well as weaken claims; do not default to escalating caution.

If execution or a data requirement fails, record that failure and complete the report using other evidence. No silent synthetic fallback, missing-to-zero conversion, answer lookup or copying a prior case's verdict. When simulated data are useful to illustrate a method, label the demonstration throughout and keep it out of empirical evidence for the benchmark.
