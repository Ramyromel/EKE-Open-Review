# EKE Review Scope
# Scope Baseline v0.1

## Status

DESIGNED — SCOPE BASELINE

This document defines the initial scope contract for an EKE Open Review.

It does not constitute evidence that any review has been performed,
independently verified, certified, accredited, or completed.

## 1. Review Identity

Every review must have a unique Review ID.

Format:

EKE-IR-YYYY-NNN

Example:

EKE-IR-2026-001

Review IDs must not be reused.

## 2. Subject

The review record must identify:

- Subject name
- Subject version
- Subject artifact
- Artifact identifier where applicable
- Artifact integrity reference where available

## 3. Review Scope

The scope must explicitly define:

### In Scope

The specifications, implementations, claims, requirements,
tests, or artifacts that are subject to review.

### Out of Scope

Items that are explicitly excluded from the review.

An out-of-scope item must not be interpreted as reviewed merely
because it is related to the reviewed subject.

## 4. Claims and Requirements

Each substantive claim or requirement included in the review
should have a unique identifier.

Example:

REQ-001
REQ-002
REQ-003

Claims and requirements should be traceable to their source.

## 5. Evidence Boundary

The review must define the evidence available to the reviewer.

Evidence may include:

- source documents
- source code
- repositories
- datasets
- test artifacts
- execution outputs
- configuration
- manifests
- cryptographic integrity records

Evidence outside the declared review boundary must not be silently
treated as reviewed evidence.

## 6. Evidence Provenance

Each material evidence item should identify, where applicable:

- Evidence ID
- Source
- Origin
- Timestamp
- Artifact identifier
- Integrity reference
- Acquisition method
- Scope relationship

## 7. Review Level

The review record must identify the applicable review level.

Supported architectural levels:

R0 — Document Review

R1 — Technical Review

R2 — Independent Reproduction

R3 — Multi-Implementation Verification

R4 — Formal / Mathematical / Security Review

R5 — Institutional / Standards-Level Review

Review Level does not imply certification authority.

## 8. Independence Requirement

Where a review is designated independent, the review record must
state the independence requirements applicable to the reviewer.

Independence must not be inferred merely from the use of the word
"independent".

## 9. Reproduction Requirement

If reproduction is within scope, the review must define:

- artifact to reproduce
- execution environment
- required inputs
- procedure
- expected outputs
- observed outputs
- reproducibility criteria

## 10. AI Participation

If AI systems participate in the review, the scope should identify:

- whether AI is used
- system/provider
- model/version where available
- intended purpose
- decision authority

AI assistance must not silently become an independent human
determination.

## 11. Acceptance Criteria

The review scope must define objective acceptance criteria.

Acceptance criteria should be:

- identifiable
- testable
- traceable
- reproducible where applicable

A claim must not be marked verified solely because it appears
consistent with the documentation.

## 12. Expected Review Artifacts

A review may produce:

- review report
- evidence register
- traceability matrix
- test results
- reproduction artifacts
- reviewer attestation
- AI disclosure
- integrity manifest
- challenge record

The presence of an artifact does not by itself establish its validity.

## 13. Non-Conformities

The review record should distinguish:

- finding
- observation
- non-conformity
- limitation
- unresolved issue
- risk

These classifications must not be conflated.

## 14. Final Determination Boundary

A review determination must remain bounded by:

- declared scope
- available evidence
- executed procedures
- observed results
- reproducibility
- stated limitations

No conclusion may exceed the evidence boundary.

## 15. Non-Claims

This scope baseline does not claim:

- independent verification
- certification
- accreditation
- scientific validation
- security certification
- production readiness

unless separately established through an appropriate process
and identifiable evidence.

## 16. Change Control

Changes to the review scope must be:

1. Explicitly identified.
2. Versioned.
3. Traceable.
4. Approved according to the applicable review process.
5. Reflected in the review record.

A material scope change must not silently overwrite historical scope.

## 17. Current State

DESIGNED

Implementation and automated validation are separate activities.
