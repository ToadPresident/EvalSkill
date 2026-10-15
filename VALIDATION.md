# Validation scope and development observations

## Software checks

The v5 helpers pass 22 synthetic tests under Python 3.10 and 3.13 in the repository's GitHub Actions workflow. The tests cover invalid/nonfinite scores, duplicate observations, version/condition mixing, missing and ungraded outcomes, repeat aggregation, declared resampling units, synthetic-data handling and evidence-record integrity. They do not test whether a model's validity argument is scientifically persuasive.

The skill entrypoint and internal reference links were checked separately. IRT, factor analysis, G-theory, transcript grading and new model evaluations are not bundled executable capabilities. The evidence helper checks declared records and file/excerpt integrity; factual accuracy and inferential relevance still require source review.

## Report comparison procedure

CORE-Bench received fresh v4 and v5 runs with the same neutral task and fixed primary materials. GPQA received a fresh v5 regression run against the preserved v4 first report, using the same primary paper versions. Each new runner used a fresh context without previous reports or coordinator findings. Ordinary internal checking was allowed before the first completed delivery. Reports were frozen before outside comparison and were not repaired afterward.

Primary CORE-Bench materials were [CORE-Bench v2](https://arxiv.org/abs/2409.11363v2), [Life After Benchmark Saturation v1](https://arxiv.org/abs/2606.26158v1), author tables at commits [9cff74](https://github.com/nnadgi01/corebench-analysis/tree/9cff74b3645be6dac41ff70f46c15e02d005ba8f) and [5d3767](https://github.com/nnadgi01/corebench-analysis/tree/5d3767d9cca750d7944ae49bb1ede1b31f39de77), and supplied author documentation/code. The GPQA packet used [GPQA v1](https://arxiv.org/abs/2311.12022v1) and [M2M v4](https://arxiv.org/abs/2505.10573v4). M2M also supplied the framework for CORE-Bench. No new benchmark trials or outside research were part of the report runs.

Review considered source-correct facts, measurement identity, appropriate analysis selection, actual execution, arithmetic, all five dimensions for each selected claim, rating reasons, consistent use scenarios, supported narrow interpretations and repetition. Matching headings or labels, choosing stricter ratings, and producing shorter reports were not counted as improvements by themselves.

These are known development cases, not held-out evaluation. The comparison is not blinded, exact sampling/inference budgets are uncontrolled, and the historical GPQA baseline was not rerun under identical execution conditions. The observations do not isolate tools from instructions or establish general superiority on unseen benchmarks. Raw reports, source files and execution records are intentionally kept outside this clean skill distribution.

## CORE-Bench observations

Both versions completed substantive analyses and reproduced the inspected response counts. v4 already wrote its own working analysis code and identified major snapshot, metric and study-interpretation issues. v5 did not introduce those strengths from scratch.

v5 added six explicit measurement profiles, executed the packaged audits/diagnostics, and recorded commands and input/profile/script/output hashes. Its report made the operation-to-claim connection more explicit and newly exposed disagreement between exported and harness success fields, plus missing model metadata in 12 OOD records. These additional semantic findings required the runner's source-specific checks; the generic helper does not identify the scientifically correct columns automatically.

The v5 report contains 7,321 whitespace-delimited words versus 8,422 in v4, about 13.1% less. It analyzes six claim families rather than eight: scaffold/strategy findings are consolidated, and the novel-research prerequisite is retained only as an untested extension. The reduction therefore partly reflects changed scope, not only removal of repetition.

There is also a material omission: v5 does not include the later paper's Table 20 target-match outcomes, which v4 used to distinguish completed sessions from matching the selected published target. v5 still correctly states that final scientific correctness was not independently verified, but this does not replace reporting the available outcome table. The run therefore shows stronger traceability and some additional data scrutiny, **not uniformly better analytical completeness**.

The v5 CORE-Bench run used descriptive repeated-response summaries and intentionally did not run bootstrap intervals. The helper's resampling implementation is software-tested; this case run is not evidence of its use in an empirical report.

## GPQA regression observations

Both reports contain the three published case claims and all fifteen dimension arguments. v5 retains the original communication, educational and conditional decision-support uses rather than replacing them with GPQA's oversight-research purpose. The analyst judgments are substantively unchanged, with the same differences from M2M's separately preserved published matrix.

v5 fills a comparator-condition omission: GPQA's expert validators could use Google if they disclosed it in their explanation. v4 did not claim that the experts were unaided, but did not include this permission in its main report. Other material safeguards, including subset selection, retrospective objectivity, uncertainty qualifiers, non-expert resource/time conditions and search backoff, were already present in v4 and were retained.

The only new data computation was bounded arithmetic on published question counts. No response-level or latent-variable analysis was invented. The evidence helper checked six file hashes, ten selected excerpts and twelve evidence references; factual and inferential review remained separate.

The main report changes from 5,403 to 5,333 whitespace-delimited words (1.3% less), with slightly more characters. Main-plus-Markdown-companion prose increases from 8,629 to 9,231 words. This is not a meaningful compression gain. A small presentation regression also remains: the v5 C2 construct section correctly specifies the optional competence-mediated interpretation, but its condensed matrix drops that qualifier. The unchanged raw output is retained for comparison.

## Priorities from the observed gaps

- Check all available outcome tables for each decisive experiment; distinguish an unmeasured outcome from a measured outcome without independent validation.
- Preserve route and version conditions directly in compact judgment tables.
- Reduce duplicated prose across companions without moving decisive arguments out of the main report.

These are documented next-iteration priorities, not changes applied after the evaluated first outputs. The v5 code and instructions used in these runs are the ones distributed here.
