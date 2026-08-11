# EKE Evidence Package
# Evidence Package Baseline v0.1

## Status

DESIGNED — EVIDENCE PACKAGE BASELINE

This document defines the initial evidence contract for an
EKE Open Review.

It does not constitute evidence that any evidence package has
been independently verified, authenticated, reproduced, or accepted.

## 1. Purpose

The Evidence Package defines the controlled boundary through which
review evidence is identified, described, referenced, and traced.

The evidence package supports:

- Evidence identification
- Evidence provenance
- Evidence integrity
- Scope traceability
- Reproduction
- Review determination

## 2. Core Rule

No Evidence → No Verification

Evidence must be identifiable before it can be used as the basis
for a substantive verification determination.

## 3. Evidence Identity

Every material evidence item must have a unique Evidence ID.

Format:

EKE-EV-YYYY-NNN

Example:

EKE-EV-2026-001

Evidence IDs must not be reused.

## 4. Evidence Source

Each evidence item should identify its source.

Possible source classes include:

- DOCUMENT
- SOURCE_CODE
- REPOSITORY
- DATASET
- TEST_ARTIFACT
- EXECUTION_OUTPUT
- CONFIGURATION
- MANIFEST
- CRYPTOGRAPHIC_RECORD
- OTHER

The source class describes the evidence type and does not establish
its validity.

## 5. Evidence Provenance

Each material evidence item should identify, where applicable:

- Evidence ID
- Source
- Origin
- Acquisition method
- Acquisition timestamp
- Artifact identifier
- Version
- Integrity reference
- Scope relationship

Provenance must not be inferred when it is unavailable.

## 6. Evidence Boundary

Evidence must remain within the declared review boundary.

Evidence obtained outside the declared boundary must be explicitly
identified before being used in a review determination.

External information must not silently become review evidence.

## 7. Integrity

Where integrity information is available, the evidence record should
identify the applicable integrity reference.

Possible mechanisms include:

- SHA-256 or equivalent artifact hash
- Signed artifact
- Manifest reference
- Cryptographic commitment
- Repository commit
- Immutable record

The existence of an integrity field does not establish that the
integrity mechanism itself has been independently verified.

## 8. Evidence Classification

Evidence should be classified according to its review state.

Suggested states:

- DECLARED
- ACQUIRED
- INTEGRITY_CHECKED
- REVIEWED
- REPRODUCED
- CHALLENGED
- REJECTED

A higher state must not be inferred from a lower state.

## 9. Evidence Relationship

Evidence should be traceable to the review elements it supports.

Possible relationships include:

Claim
→ Requirement
→ Evidence
→ Test
→ Result

An evidence item may support multiple requirements.

A requirement may depend on multiple evidence items.

## 10. Evidence and Observation

The system must distinguish:

Evidence:
an identifiable artifact or record available for review.

Observation:
a statement describing what was observed from evidence.

Evidence must not be silently replaced by interpretation.

## 11. Evidence and Verification

Evidence availability does not automatically establish verification.

The following distinction must remain explicit:

Evidence Present
≠
Evidence Validated
≠
Claim Verified

Verification requires applicable criteria and recorded results.

## 12. Reproduction Artifacts

Where reproduction is applicable, the evidence package may contain:

- Input artifacts
- Runtime information
- Environment information
- Commands or procedures
- Execution outputs
- Expected results
- Observed results
- Reproduction logs

Reproduction artifacts must remain traceable to the reviewed evidence.

## 13. Sensitive Evidence

Sensitive evidence must not be exposed merely because it belongs
to a public review.

Where required, sensitive evidence may use:

- Access control
- Encryption
- Redaction
- Cryptographic commitments
- Authorized disclosure

Obfuscation alone is not considered a security control.

## 14. Evidence Modification

Material evidence must not be silently modified after acquisition.

If a new version is introduced, it should receive:

- A new artifact identifier
- A new integrity reference
- A new acquisition record

Historical evidence records must remain traceable.

## 15. Evidence Rejection

Evidence may be rejected when:

- Provenance is insufficient
- Integrity cannot be established where required
- It falls outside the declared scope
- It cannot be reliably identified
- It conflicts with applicable evidence requirements

A rejection must be recorded rather than silently removing the item.

## 16. Evidence Completeness

An evidence package should identify known limitations.

Absence of evidence must not be represented as evidence of absence
unless that inference is explicitly justified by the review method.

## 17. Non-Claims

This baseline does not claim:

- evidence authenticity
- evidence validity
- independent verification
- scientific validity
- security assurance
- certification

unless separately established through an appropriate process
and identifiable evidence.

## 18. Change Control

Changes to the Evidence Package requirements must be:

1. Explicitly identified.
2. Versioned.
3. Traceable.
4. Reviewed for architectural impact.
5. Reflected in applicable review records.

## 19. Current State

DESIGNED

Evidence implementation, integrity verification, provenance validation,
and independent assessment are separate activities.
