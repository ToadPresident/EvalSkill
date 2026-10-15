# Rule provenance

This register answers where an analytical rule comes from, when it applies, and what the skill adds. **M** means a paraphrase of a principle in [Measurement to Meaning v4](https://arxiv.org/pdf/2505.10573v4), 26 June 2025. These principles draw on the measurement literature discussed by M2M; the label does not imply that M2M originated all of them. **I** means our implementation choice. Page numbers below are the PDF's printed page numbers.

The rule identifiers, grouping, examples of misuse, and mapping into report fields are themselves implementation choices. A source location warrants the stated principle, not every design decision made to apply it.

## Principles taken from M2M

| Rule | Source location | Principle and application condition | What its application does not establish |
|---|---|---|---|
| M01 Claim and context | Figure 1 and discussion, p. 2; Table 1, p. 3; Section 4, pp. 10-12 | Assess the interpretation of measurements for a specified claim, object, and use. Apply whenever a benchmark result is used to say something about a system. | A benchmark-wide verdict valid for every possible claim. |
| M02 Criterion and construct | Table 1, p. 3; Figure 2 and Section 4, pp. 10-12 | Distinguish directly observable criteria from constructs requiring operationalization and indirect evidence. Identify whether measurement and target coincide. | An observable criterion is automatically a gold standard, or naming a construct validates it. |
| M03 Context-dependent five dimensions | Table 2, p. 4; Figure 2 caption and Section 4, p. 10 | Consider content, criterion, construct, external, and consequential validity; their evidential demands depend on the measurement, claim, and context. Some can be trivially satisfied. | Every dimension needs equal space, a new experiment, or an invented defect. |
| M04 Direct criterion | Section 5.1, p. 14 | When the object is the measured criterion, criterion and construct validity can be trivially satisfied. Content and relevant context still require attention. | A finite-item result validates new items, a broader skill, or an unmeasured use. |
| M05 Different observable target | Section 4, p. 12; Section 5.2, pp. 15-16 | For a different target criterion, a justified predictive or concurrent relationship can establish the relevant link without a complete theory of latent constructs. If relying on mediation, establish the necessary construct relationships. | Expert performance on the same items proves prediction of a different assessment. Scenarios 2 and 3 are not labels for direct versus mediated prediction; they concern proxies of the same versus related different constructs. |
| M06 Construct relationships | Figure 4 and discussion, pp. 12-13; Section 5.3, pp. 16-17 | For construct-targeted or construct-mediated claims, investigate structure, convergence, discrimination, and a network linking constructs and observations. | A factor's name, a diagram, or one correlation proves a capability. The illustrative human intelligence network automatically applies to AI. |
| M07 Multiple evidence sources and narrower claims | Section 5, Sources of Validity Evidence, p. 13 | Validation can draw on multiple studies and stakeholders, and reasoning can proceed from available measurements toward defensible, narrower claims. | Multiple descriptions of one study are independent replications, or a narrower reformulation is the unchanged original claim. |
| M08 Qualitative report card | Table 3 and caption, p. 9 | M2M uses reasonable, proceed with caution, and insufficient as subjective, revisable judgments. Reasonable can retain weaknesses when strengths outweigh them for the claim. | An exhaustive checklist, numerical cutoffs, inter-rater reliability, or an additive total score. |
| M09 Consequences | Table 2, p. 4; Section 3, p. 9; Section 5.4, p. 17 | Examine effects of interpretation and use, including intended and unintended consequences. The discussion includes anticipatory analysis as well as observed impacts. | Anticipated benefit is an observed benefit, or consequential analysis always requires a completed deployment experiment. |
| M10 Content and transfer scope | Section 3, p. 8; Section 5.1, p. 14 | Examine coverage of the claim's relevant content and generalization to the contexts in which it is intended to hold. | Expert curation alone establishes exhaustive coverage, or apparent task similarity alone demonstrates transfer. |

## Our implementation choices

| Rule | Choice and purpose | Relation to M2M or external inspiration |
|---|---|---|
| I01 Delivery and language | A benchmark name/link can initiate one complete report. Default English; explicit Chinese/bilingual overrides. Clarify only consequential ambiguities. | Product design, not a requirement in M2M. |
| I02 Claim and measurement records | Preserve claim ownership and original scope; record version, subset, model configuration, protocol, denominator, and any achievement threshold. Separate original statements from operational readings and narrower reformulations. | Implements M01-M02 and the threshold concern in Section 5.1 footnote 4, p. 14. The record schema is ours. |
| I03 Argument structure | Each substantive assessment connects evidence, an explicit warrant, gap or satisfaction condition, judgment and decisive basis, and revision condition. Connected prose can carry several components without separate repeated headings. | Our report design for applying M03-M07 and M10; these are not five additional validity dimensions. |
| I04 Judgment conventions | Use M08 labels with the working definitions in judgment-and-use.md; explain the decisive support/limitation and the plausible neighboring label. Missing studies do not mechanically set the rating. Pending access is outside the scale; an asterisk marks operational satisfaction. No summed score. | M08 supplies the labels and revisable character; definitions, decision procedure, statuses, and notation are ours. |
| I05 Contribution-aware extraction | Read sources by their contribution to this analysis, allow multiple roles, and record what each finding can and cannot support. Treat M2M as a methodological framework. | Inspired by SkillXiv's category-aware extraction. Our source-role scheme adapts it for validity analysis; it is not M2M theory or a claim that SkillXiv empirically proved this design superior. |
| I06 Fact verification and reconciliation | Check decision-relevant clauses and their qualifiers against primary passages; retain exact locators, conditions, unresolved conflicts and versions. Avoid double-counting one experiment. A bounded search gap differs from a failed test or inaccessible evidence. | Research implementation supporting M07. M2M's case commentary is not automatically authoritative about a primary benchmark protocol. |
| I07 Method provenance | Keep framework principles, implementation rules, empirical findings, and current analyst judgments attributable. Show the governing rule and satisfied or missing application condition for consequential decisions. | Our traceability design. Rule identifiers are navigation aids, not evidence of benchmark validity. |
| I08 Inference review | Check facts, every dimension's argument, rating basis, use consistency, and compression before delivery; retain actual findings. Distinguish internal review from outside review and freeze the first completed calibration output. | Our procedure, informed by Paper2Agent's verification emphasis and observed calibration failures. It does not transfer that system's experimental results to this skill. |
| I09 Calibration and comparison | Preserve published case judgments; compare aligned claims, uses and evidence; allow justified disagreement. Distinguish schema checks, source-case calibration, unseen-case transfer, and comparative benefit. Do not credit later repairs to the frozen original output. | Our evaluation design. Rating agreement, strictness and report length are not quality measures by themselves. |
| I10 Conditional computation | Use calculations only when they answer a material question and are authorized. Keep proposed studies separate from completed experiments. Consult analysis guidance for relevant methods. | Implementation guidance; M2M discusses possible methods but does not mandate every analysis for every claim. |
| I11 Use consistency | Record the interpretation-decision/behavior-outcome relationship and its owner before consequence analysis. Keep it stable through the rating and revision condition. Distinct uses receive distinct records and, when needed, judgments. | Our implementation of M01/M09, introduced after observed case-use substitution; identifiers and the consistency procedure are not requirements stated by M2M. |
| I12 Compact complete reporting | Store shared facts once; write claim-specific inference locally; consolidate proposed studies and remove duplicate method traces. Use a soft length target while retaining every material argument. | Our writing design responding to repetitive calibration reports, not an M2M word limit or a claim that shorter is inherently better. |

## v5 implementation additions

| Rule | Operational requirement | Source and attribution |
|---|---|---|
| I13 Measurement profile and routing | Record data origin, source version, systems, item hierarchy, score and availability; select checks jointly by claim relevance and data adequacy. | Our implementation, informed by AI Measurement Science Chapter 2 and Measurement Data Bank; not a new M2M dimension. |
| I14 Layered verification | Separate source/excerpt integrity, fact accuracy, claim relevance and executed computation. Keep failed/unavailable/synthetic results distinct; missing extraction is not absence. | Our implementation, informed by Caliper's evidence/narrative separation and limitations observed in its structural checker. |
| I15 Bounded diagnostics and inference return | Audit explicit data contracts; run only eligible checks; record actual results and the inferential link they inform. Do not convert software success to a validity label. | Our implementation, informed by measurement science and the existing project analyses. The scripts are original code, not copies of course notebooks or a generic implementation of their methods. |

### External methods are separately attributable

Keep three levels distinct: M2M framework principles, independently sourced statistical methods, and our implementation rules. Source claims and empirical findings are evidence, not additional rules. The method source, applicability assumptions and implementation revision belong in an analysis record. No automatic M2M rating is derived from IRT, factor analysis, G-theory or the bundled descriptive/paired bootstrap checks.

The executable v5 scope is CSV auditing, binary response/repetition summaries and conditional paired task/cluster bootstrap intervals, plus evidence-record integrity. The IRT/G-theory guidance does not imply those models are implemented. Our helper neither imports torch_measure nor bundles third-party code/data.

## v5.1 implementation refinements

The existing I06, I12, I13 and I14 procedures now explicitly cover decisive outcome-table completeness, conditions retained in compact judgments, optional versioned task inventories, all-ungraded visibility, and checks against the actual report file. Reference loading moves to the relevant task step, and paths resolve from the installed skill. These are implementation refinements prompted by development failures and portability requirements; they add no M2M dimension or universal statistical requirement. Their software behavior is tested separately from their effect on complete report quality.

## Applying the register

For a decisive step, state: **principle -> application condition -> case evidence -> judgment**. For example, M04 permits direct-criterion satisfaction only after the report establishes that the measurement and claimed outcome coincide. The observed protocol supplies that fact; M04 alone cannot supply it. Use I02 when separating a fixed-set statement from a broader statement about new questions.

If an argument combines an M principle and an I convention, cite them separately rather than calling the whole procedure an original M2M requirement. Put rule references next to the relevant argument or in a compact method trace with precise claim/dimension locations. Avoid repeating the entire register in every report.

## Design references

- SkillXiv [Paper2Skill v0.0.3 entrypoint](https://github.com/ADu2021/skillXiv/blob/10b9e2ab98d22d657cdca33fadb35feaf4a2e26b/paper2skill/paper2skill-v0.0.3/SKILL.md) and its category-specific references. This skill borrows the idea of extracting different kinds of usable knowledge; it does not adopt the eleven categories as a compulsory taxonomy or quality scale.
- Paper2Agent [Nature paper](https://www.nature.com/articles/s41586-026-11044-y), especially validation and the Discussion's distinction between faithful execution and analytical validity.
- Paper2Agent [paper-material verification component](https://github.com/jmiao24/Paper2Agent/blob/61bdd684eb2d8ce57355d0ee0072393cb700f539/skills/paper2agent/paper2skill/SKILL.md). Its review and provenance practices inform I08; this is distinct from SkillXiv's similarly named engine.

### v5 design references

- [AI Measurement Science source](https://github.com/aims-foundations/aims/tree/0118277faed7602aef8493094c0ca0797078a62a), especially Chapters 2 and 5: data representation and design-dependent reliability.
- [Measurement Data Bank schemas](https://github.com/aims-foundations/measurement-db/tree/ff987fc4213845374a7eeb50b9f7923a7bd9d178): observation/scoring identities and source claims.
- [Benchmark Caliper extraction design](https://github.com/aims-foundations/benchmark-caliper/blob/f58e03d55a532bf709000e896d4229770d501119/.claude/skills/validity-pdf-extract/SKILL.md) and [structural checker](https://github.com/aims-foundations/benchmark-caliper/blob/f58e03d55a532bf709000e896d4229770d501119/scripts/verify_quotes.py): evidence/narrative separation; its six-dimensional framework and numeric ratings are not adopted.
- [torch_measure quickstart](https://github.com/aims-foundations/torch_measure/blob/a461a8f24eb2960f692afdac0a2202c7d1d507ad/docs/source/quickstart.rst): optional future implementation resource; its data API is not assumed compatible without a checked adapter.
