# M2M framework map

Source: Salaudeen et al., [Measurement to Meaning version 4](https://arxiv.org/pdf/2505.10573v4), 26 June 2025. This is an operational guide, not a substitute for the paper.

Use [rule provenance](rule-provenance.md) for the distinction between M2M principles and our implementation choices. Route names and the guide's organization are an operational presentation of the source's distinctions.

| Source location | Question to resolve |
|---|---|
| Table 1 and Figure 1 | What are the measurement, evaluation, claim, and object? |
| Table 2, page 4; Table 3 and caption, page 9 | What do the five dimensions address; where do the qualitative labels come from? |
| Section 4 and Figure 2, pages 10 to 13 | Is the object a criterion or construct; how does the measurement relate to it? |
| Section 5.1, page 14 | When does directly measuring the criterion remove the need for additional criterion or construct validation? |
| Section 5.2, pages 15 to 16 | How can a different measurement support a target criterion? |
| Section 5.3, page 16 | What construct relationships require investigation? |
| Section 5.4, page 17 | Which consequences of evaluation and use matter? |
| Appendix D.1, pages 43 to 47 | How do GPQA interpretations change with the claim? |

## Implementation decisions

A criterion is observable; it is not automatically a gold standard. For a criterion-aligned claim, explicitly identify the operational equality and its scope. Content and context still matter.

For criterion-adjacent claims, a direct empirical relationship with the target or a justified standard may suffice. If reasoning through constructs instead, identify and investigate every needed link. Scenarios 2 and 3 concern proxies of the same versus related different constructs; direct empirical prediction and mediation are strategies, not replacement names for those scenarios.

For construct claims, define the capability before interpreting structure, convergence, discrimination, and alternatives. Clarify the expected relationships with observable measures. Distinguish conceptual assumptions from observed support. A human psychological factor structure cannot simply be assumed to apply to AI systems.

Consider all five dimensions for each claim while adapting the depth to its inferential requirements. Do not manufacture a defect in every dimension. A narrow observed-outcome claim and a transfer or capability claim can share observations without sharing the same evidential requirements.

The three qualitative labels come from M2M Table 3 (M08). Our working definitions, asterisk, pending status, source-role extraction, fact records, report layout, language defaults, discrepancy handling, inference review, use consistency records, and compression rules are implementation choices (I01-I12). They should not be attributed to M2M as additional theoretical requirements.
