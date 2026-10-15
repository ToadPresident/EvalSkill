# Conditional analysis guidance for scientific workflows

These are conditional method recommendations, not shipped or validated implementations. The bundled v5 executable is limited to [auditing and response diagnostics](response-diagnostics.md). Read [analysis routing](analysis-routing.md) first.

Use only the rows relevant to the requested inference. An instrument can be useful without every diagnostic below.

| Evidence/question | Appropriate analysis | Interpretation to preserve |
|---|---|---|
| Which operations does the benchmark cover? | Task-to-deliverable mapping using instructions and scoring code | Task labels or disciplines alone do not show full workflow coverage. |
| Which current candidates can be distinguished? | Response matrix and paired task comparison; optionally fitted IRT information | Whole-panel spread is different from resolution among a selected high-performing group. |
| Does a fixed artifact receive the same judgment? | Hold artifact fixed; compare judge scores, threshold crossings and accepted sets | Judge repeats are not independent agent attempts; changing acceptance is not automatically an incorrect grade. |
| Does execution lead to accepted science? | Within the same cohort, separate execution, artifact checks and scientific criteria | Compare denominators and gate definitions; avoid treating all failures as one mechanism. |
| Can saved code and outputs be reproduced? | Run original saved code with controlled inputs/environment when authorized | Replaying the same program adds reproducibility evidence, not new independent agent performance trials. |
| Why does an all-checks task fail? | Inspect component checks and the scientific basis of the failed condition | Useful partial work may coexist with a justified whole-task failure; preserve official score. |
| What does a weighted progress score count? | Reconstruct hierarchical effective weights and compare categories | Rubric leaf count, weighted achievement and fraction of entire papers reproduced are different quantities. |

## IRT / Rasch

For a binary outcome, the Rasch working model uses a system position and task difficulty. Once fitted, local information is proportional to `p(1-p)` per attempt. For a specific target configuration, that quantity may help assess whether a task is informative. Overall task pass rate is not the target-conditional probability.

Before using the interpretation, identify the target population, fitted scale, repeated-response structure, shrinkage and observed fit. Validate prediction on held-out responses if predicting is the intended use. A statistically useful factor is not automatically scientific reasoning or a named discipline. Tasks calibrated on other systems and held out for the target system are not entirely unseen scientific tasks.

A retrospective case analysis should not be rewritten as a prospective IRT selection. A fitted probability for one configuration does not directly estimate that for another configuration. Near-50% success can provide information while also producing variable binary outcomes. Two consistent attempts do not establish a stable population success rate.

## G theory and repeated evaluation

Define the object of measurement and the universe to which the judgment should extend. A full agent configuration can be the object rather than a nuisance factor. Tasks, attempts, judges and execution jobs may be facets; their crossed or nested structure comes from the actual protocol.

Separate descriptive repeat metrics, paired task resampling, G-study variance decomposition and D-study projections. Mean success, all-runs success and an agreement statistic are not G coefficients. High whole-panel G does not decide a close pair. One task cannot identify generality across unobserved tasks.

For a saturation follow-up, G theory can organize questions such as: what changes with the task sample, repeated attempts, or evaluation conditions? This is our analysis of the team's design, not a statement that its authors used G theory. Task repairs address score meaning, and time/cost studies concern separate outcomes; do not recast all such work as variance components.

Respect shared jobs and nesting. A projection that assumes independent runs needs that assumption stated where it affects the decision. Label D-study projected precision/cost separately from observed held-out performance. Do not promise that one or two tasks can recover benchmark-wide rankings.

## Local numerical checks

Recalculate only figures material to the requested conclusion, preserving the original record. Keep continuous progress scores continuous; do not feed them to binary Rasch by convenience. Do not count thousands of nested rubric leaves as thousands of independent papers. When versions conflict, identify the different cohorts instead of silently averaging or selecting a convenient result.

## Source tradition

These are project methods informed by the Stanford AI Measurement Science course/textbook (reliability, validity, item response and efficient evaluation), source benchmark protocols and the local analyses. They extend the workflow implementation; they are not all prescriptions of M2M. Read relevant original methods when performing a new fit or design, rather than using this reference as a statistical software specification.
