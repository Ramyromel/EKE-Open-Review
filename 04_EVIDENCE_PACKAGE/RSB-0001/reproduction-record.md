# RSB-0001 Independent Reproduction Record

## Evidence boundary

The benchmark source is RSB-0001 v1.0. The two reproduction runtimes consume the canonical graph and query text but do not load the normative expected-answer fields. The comparison step is separate from the reproduction runtimes.

## Runs

- `2026-08-14-python-graph-runtime-a`: PASS, Q01–Q10 all matched.
- `2026-08-14-node-graph-runtime-b`: PASS, Q01–Q10 all matched.

## Independence check

A source inspection of both runtime implementations confirms that neither implementation contains an expected-answer dataset or parses the benchmark's `expected_answer` fields. The runtimes therefore did not obtain normative expected answers while producing observations.

## Reproduction count

Passing reproduction runs contributed: 2.
RSB-0001 specifies `minimum_reproductions: 2` for CHR-0001.

## Source limitation

RSB-0001 §6.11 names an EQA five-criteria checklist but the supplied controlled artifact does not enumerate those five criteria. The run artifacts record this as `NOT_ESTABLISHED` rather than inventing criteria.

## Review boundary

These records establish two reproducible benchmark executions against the supplied canonical graph. They do not establish general EKE conformance, security certification, accreditation, attestation, or certification.
