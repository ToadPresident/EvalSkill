# Contributing

Keep the skill focused on complete, sourced analyses of benchmark claims. Changes should explain the observed problem, the proposed behavior and how the change was checked.

- Keep the skill and report template in English. Preserve explicit Chinese/bilingual report support.
- Distinguish M2M principles, external methods and implementation choices. Add exact method/source locations for substantive analytical rules.
- Keep the entrypoint concise; load detailed method instructions only when their conditions apply.
- Add or change helper code only for concrete reusable operations. Validate assumptions, data semantics and execution status; do not introduce automatic validity scores or silent synthetic fallback.
- Test observable behavior with synthetic fixtures and independently check numerical expectations. Run `python3 -m unittest discover -s skills/scientific-benchmark-validity/tests -v`.
- For report comparisons, use matched primary inputs, preserve the first completed outputs, and review evidence support rather than merely counting headings or matching ratings. Keep known-case calibration separate from held-out evaluation.
- Keep papers, real datasets, reports, logs, local paths, credentials and generated artifacts out of commits. Include only compact non-sensitive synthetic fixtures in tests.
- Update the version, README and CHANGELOG when behavior changes. Preserve prior releases in Git history/tags; do not overwrite old calibration outputs.

Review feedback and issue discussions should use minimal, redacted examples. This repository does not require running live model APIs to execute its software tests.
