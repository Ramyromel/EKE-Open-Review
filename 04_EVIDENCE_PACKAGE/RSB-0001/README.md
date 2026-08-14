# RSB-0001 Evidence Package

## Status

`ACTIVE_REVIEW_TARGET` — evidence package established; no EKE-ORP verification or certification is implied by this boundary alone.

## Controlled Artifact

- Review Target: `RSB-0001`
- Version: `1.0`
- Status: `ACTIVE`
- Artifact: `RSB-0001.md`
- Benchmark hypothesis: `CHR-0001`

The controlled benchmark is stored in this directory. Its normative expected answers are benchmark data, not observed results.

## Evidence Boundary

This package separates:

`Review Target → Evidence → Independent Reproduction → Observation → Findings → Review Result`

The following are not asserted merely by integration:

- independent reproduction
- observed execution results
- external review findings
- verification
- attestation
- certification

## Reproduction Requirement

Each independent run must provide the six artifacts required by RSB-0001:

```text
RSB-0001/runs/{YYYY-MM-DD}-{implementation-id}/
  ├── input-graph.yaml
  ├── raw-outputs.yaml
  ├── pass-fail.yaml
  ├── implementation.md
  ├── environment.md
  └── eqa-checklist.yaml
```

A passing run requires all ten queries to match the benchmark expected answers and requires the implementation to have no prior knowledge of those expected answers. Two independently reproduced passing runs are required by RSB-0001 for its stated `minimum_reproductions: 2` relationship to CHR-0001.

## Prior Review Artifact

`RSB-0001_Review_Report.md` is treated as a prior review artifact only. Its reported results are not imported as EKE-ORP observed results or verification results unless the underlying run artifacts and provenance are independently established.

## Certification Boundary

No certificate, attestation, accreditation, or `VERIFIED` status is created by this package.
