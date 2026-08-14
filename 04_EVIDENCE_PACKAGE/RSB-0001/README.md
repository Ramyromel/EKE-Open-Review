# RSB-0001 Evidence Package

## Status

`SOURCE_ARTIFACT_PENDING` — not a review result, verification, attestation, or certification.

## Review Target

- Benchmark ID: `RSB-0001`
- Title: `Semantic Invariance: Positive Test`
- Category: `Positive`
- Version: `1.0`
- Hypothesis: `CHR-0001`

The controlled source artifact is the original `RSB-0001.md` supplied for integration. Its normative content must be copied into this package verbatim when committed; no reconstruction or normalization is permitted.

## Evidence Boundary

This package is limited to the RSB-0001 benchmark itself and its declared relationship to CHR-0001. It does not establish EKE correctness, complete EKE conformance, or any semantic-invariance property outside CHR-0001.

## Review Chain

```text
RSB-0001
  -> Review Scope
  -> Evidence Package
  -> Review Procedure
  -> Independent Reproduction
  -> Observed Results
  -> Findings
  -> Review Result
```

Only the first two nodes are represented by this integration boundary. No reproduction, observed result, finding, or review determination is created here.

## Required Reproduction Evidence

RSB-0001 requires an independent run to provide, for each implementation:

```text
runs/{YYYY-MM-DD}-{implementation-id}/
  input-graph.yaml
  raw-outputs.yaml
  pass-fail.yaml
  implementation.md
  environment.md
  eqa-checklist.yaml
```

No populated run is created by this integration.

## Prior Review Material

Any prior review report concerning RSB-0001 is treated as a prior review artifact/external review evidence. It is not imported as an EKE-ORP verification result and does not create a `VERIFIED` state.

## Evidence/Verification Boundary

```text
Evidence Present != Evidence Validated != Claim Verified
```

The EKE Evidence Package baseline requires provenance and integrity information where applicable, and explicitly prohibits inferring verification from evidence availability alone.

## Blocking Condition

The original RSB-0001 source artifact is available outside the repository but is not yet present in the repository tree. Until that exact artifact is committed verbatim, this package remains `SOURCE_ARTIFACT_PENDING`.
