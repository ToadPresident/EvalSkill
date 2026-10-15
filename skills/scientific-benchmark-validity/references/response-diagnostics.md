# Method: bounded response diagnostics

**Purpose:** Describe observed binary outcomes across systems, tasks and repetitions, and assess a justified paired comparison. This is an implementation method [I15], not an M2M rating algorithm.

**Inputs:** A CSV of actual observations and an explicit [measurement profile](measurement-profile.md). The helper uses Python 3.10+ standard library and makes no network or model calls. Raw data remain unchanged.

## Run

```sh
python3 scripts/measurement_tools.py audit --csv responses.csv --profile profile.json --output audit.json
python3 scripts/measurement_tools.py diagnose --csv responses.csv --profile profile.json --output diagnostics.json --bootstrap 2000 --seed 17
```

The second command audits again and refuses invalid, nonbinary, mixed-condition or mixed-version inputs. No fixed run count or benchmark-specific path is built in. `--allow-demo` is only for explicitly synthetic profiles and leaves every output labelled simulation. The standard report path never substitutes a demonstration for unavailable observations.

## Checks and calculations

1. **Audit:** finite scores within their declared scale, unique logical observations, version consistency, grouped coverage, ungraded attempts and repeat balance. Units and provenance must also be reviewed against sources; a machine pass cannot verify their scientific meaning.
2. **System summaries:** retain attempted, graded and ungraded counts for every observed system. A system with no graded responses remains visible with `null` means and `score_status: no_graded_responses`. Show both mean over observed trials and mean over observed item means when defined. The latter gives each observed item equal weight. Unequal coverage can make systems incomparable even when both means exist.
3. **Repetition summaries:** when each observed system/item cell has the same k within a system, report empirical fractions with at least one success, all successes and mixed outcomes. Preserve k, the task denominator and incomplete coverage. These are observed fractions, not a general pass@k estimator or a reliability coefficient.
4. **Item summaries:** mean over observed system cell means, with attempt/ungraded counts and `null` for no graded response. Include wholly absent tasks only when the profile supplies an applicable expected inventory; otherwise coverage refers to observed tasks. Use unusual patterns as prompts for source/item/scorer review, not proof that an item is defective. No arbitrary anomaly threshold is supplied.
5. **Paired comparisons:** for a complete graded panel with equal repeat counts, compare system cell means on the same items. Bootstrap the declared items or parent clusters jointly across the pair, retaining observed repeats. Report percentile 95% intervals, draw count, seed and the sampling interpretation. Each sampled cluster contributes all its items; the estimand is the item-weighted mean, not an equal-cluster mean. At least two resampling units are required.

An incomplete/unequal-repeat panel still permits labelled descriptive summaries but disables intervals in this helper. Designing an appropriate missing-data or hierarchical model is separate work; do not silently delete cells until the intended answer appears.

## Interpret and constrain

Connect a result to the exact C/U relationship being assessed. Explain both what it adds and why it cannot establish the rest of the argument. Similar mean accuracy with different repeated outcomes may qualify interchangeability or stability, while leaving a narrow observed-score statement supported.

Task/cluster intervals are conditional on frozen systems, scoring, and observed within-task repetitions. They do not propagate all stochastic, grader, selection or version uncertainty. They depend on a defensible resampling population; fixed-set descriptive claims need not acquire a superpopulation interpretation. Intervals are unadjusted across multiple pairs. A zero-width interval at a ceiling is not proof of certainty. These are percentile bootstrap diagnostics, not calibrated significance tests, extrapolations to new agents, or new benchmark experiments.

Save the profile, audit, diagnostics and command/result status. Outputs include input/profile/script hashes; hashes support reproducibility but do not validate the input labels. Cite JSON keys alongside the numerical result in the report. The helper fits no Rasch, factor or G-theory model and makes no decision about validity labels.

## Method sources

The need to distinguish measurement objects, facets, reliability and decision conditions is informed by [AI Measurement Science Chapter 5](https://aimslab.stanford.edu/textbook/src/chap5.html). The descriptive formulas, conservative eligibility conditions, file contract and use of a paired task/cluster percentile bootstrap here are our implementation choices. They require design-specific justification, not a claim that the course prescribes this exact procedure.
