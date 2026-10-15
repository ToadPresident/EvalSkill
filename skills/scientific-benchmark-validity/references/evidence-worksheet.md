# Evidence and fact verification record

This is a working record for I02, I03, I06, and I11. Keep the finished report compact; do not copy every working field into it. During a calibration, save the fact record so a reviewer can inspect the checks. For ordinary delivery, a compact evidence index with exact locators is sufficient.

## Clause-level fact check

Check decision-relevant numbers, protocols, comparisons, and source attributions against the passage or table that establishes them. Split a sentence into separately supported clauses when its qualifiers have different sources. Record a short paraphrase and exact locator; long quotations are unnecessary.

| Fact ID / report location | Supported observation and source locator | Conditions and qualifiers checked | Status / action |
|---|---|---|---|
| F1 / E1 | [Primary passage, table row/note, appendix, or code version.] | [Only applicable fields below.] | [Verified as written; narrowed to supported wording; unresolved discrepancy; secondary-only; inaccessible.] |

Check applicable qualifiers independently:

- **Quantity:** cohort/subset, numerator/denominator, units, configuration; initial observation versus filtered, adjusted, or retrospective estimate.
- **Uncertainty:** interval/error type and confidence level only if stated or actually calculated with a documented method. A plus/minus value does not establish either by itself.
- **Protocol:** allowed tools and assistance, exclusions, mandatory minimum versus permitted maximum versus observed duration. Avoid ambiguous words such as unaided when resources were allowed; name the resources.
- **Comparison:** same items versus an independent target; selection-dependent comparator versus independent validation; multiple descriptions versus separate experiments.
- **Attribution:** observed result, author claim/intention, analyst inference, or proposed study. A general source citation cannot convert one kind into another.

When the source supports the value but not a qualifier, retain the value with the supported description. Do not guess the missing qualifier, silently substitute another version, or discard a useful result unnecessarily. Reconcile substantive conflicts using version-specific primary evidence; state what the correction changes in the argument.

## Claims, uses, and evidence

Record claim owner, original scope, target, route, achievement threshold if relevant, and narrower reformulation separately. Record uses as U identifiers using [judgment and use](judgment-and-use.md). A case author's use and the benchmark's published purpose can differ.

For each E identifier, retain source/version/locator, contribution role, observation, conditions, independence, verification status, and inferential limit. Roles are extraction guides, not credibility scores. Bound evidence gaps to the inspected scope.

For each claim/dimension, retain the relevant E identifiers, warrant and factual application condition, decisive support/gap, rating basis, and a finding that would alter the assessment. Shared evidence is not independent corroboration. When a construct route is necessary, identify each score-construct-target relationship and the status of alternatives; a named factor alone is not a capability explanation.

## Review record

Follow [inference review](inference-review.md). Keep actual findings, corrections, unresolved issues, and effects on judgments. Preserve original completed outputs in version comparisons; do not use subsequent edits as evidence of first-run performance.

## Verification layers and optional executable registry

Separate source integrity, fact accuracy, relevance and execution status. A failed extraction is not evidence that a paper is silent. Revisit unreadable tables/appendices or record access limits before declaring bounded absence. Distinguish author-reported results, completed reanalysis, non-execution, failure, unavailable inputs and simulation. These are our I14 records, not M2M ratings.

For calibration or substantial source/computation audits, save `evidence.json` and run `python3 scripts/verify_evidence.py --registry evidence.json --output evidence_check.json`. Source paths resolve from the registry directory, or an explicit `--base-dir`. This compact registry supports the report rather than duplicating it.

```json
{
  "sources": [{"id": "S1", "version": "paper revision 1", "locator": "source URL", "path": "paper.txt", "sha256": "<actual SHA256>"}],
  "evidence": [{
    "id": "E1", "source_id": "S1", "locator": "Table 2, PDF page 6",
    "kind": "reported_result", "observation": "Supported paraphrase including material qualifiers",
    "excerpt": "A short exact locator excerpt, if useful",
    "review": {
      "fact": {"status": "checked", "basis": "Describe the inspected passage, qualifiers and reconciliation"},
      "relevance": {"status": "checked", "basis": "Explain the claim link supported and its limit"}
    }
  }],
  "report_evidence_ids": ["E1"]
}
```

Kinds: `author_claim`, `reported_result`, `protocol`, `computed_result`, `simulation`, `analyst_inference`, `proposed_study`. Computed entries reference actual result files/keys and input/command records. Keep excerpts short and optional; paraphrase rather than copying large passages. Page/row verification and semantic support remain source-grounded review tasks.

The helper checks local hashes, ID/reference integrity and optional whitespace-normalized excerpt presence. It checks that a declared completed fact/relevance review records its basis; it does not validate that basis. It does not require a quotation for every dimension, certify factual truth, or decide a validity rating. Never fabricate evidence to pass coverage checks.
