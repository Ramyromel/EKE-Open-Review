# EKE Active Reviews
# Active Reviews Baseline v0.1

## Status

DESIGNED — ACTIVE REVIEW BASELINE

This document defines the initial lifecycle boundary for active EKE
Open Reviews.

It does not constitute evidence that any review is currently active,
completed, independently verified, certified, accredited, or
production-ready.

## 1. Active Review Identity

Every active review must reference an existing unique Review ID.

Format:

EKE-IR-YYYY-NNN

An active review must not create a second identity for the same review.

## 2. Activation

A review may enter ACTIVE state only when:

- review identity exists
- review scope is declared
- applicable reviewer requirements are established
- evidence boundary is defined
- required review application information is available
- acceptance criteria are identifiable

Activation must be recorded.

## 3. Active Review Record

An active review record should identify:

- Review ID
- Subject
- Review level
- Current status
- Scope reference
- Reviewer reference
- Evidence package reference
- Activation timestamp
- Current phase
- Applicable acceptance criteria

## 4. Lifecycle State

Supported active-review states:

DRAFT
→ ACTIVE
→ PAUSED
→ BLOCKED
→ COMPLETED

A review must not be represented as COMPLETED while required
review activities remain unresolved.

## 5. State Transitions

Every state transition should be:

- explicitly recorded
- attributable
- timestamped
- traceable to the review record

A state transition must not silently overwrite historical state.

## 6. Review Activity

Active review activities may include:

- evidence examination
- requirement analysis
- claim analysis
- test execution
- reproduction
- discrepancy analysis
- reviewer discussion
- AI-assisted analysis with disclosure
- finding generation
- resolution of review blockers

The presence of an activity record does not by itself establish
verification.

## 7. Evidence Boundary

Active review activity must remain within the declared evidence
boundary.

New evidence introduced during an active review should be explicitly
identified and incorporated according to the applicable evidence
procedure.

Evidence outside the declared boundary must not be silently treated
as reviewed evidence.

## 8. Findings

Active reviews may produce:

- observation
- finding
- non-conformity
- limitation
- unresolved issue
- risk

Each substantive finding should be traceable to:

Claim
→ Requirement
→ Evidence
→ Procedure/Test
→ Observed Result

## 9. Blocked Reviews

A review may be BLOCKED when a required condition prevents continued
review activity.

A blocked state should identify:

- blocking condition
- affected activity
- required resolution
- timestamp
- responsible party where applicable

BLOCKED must not be interpreted as FAILED.

## 10. Paused Reviews

A review may be PAUSED when review activity is intentionally
suspended without establishing a failure determination.

The pause reason and resumption condition should be recorded.

## 11. AI Participation

Where AI systems participate in active review activities, the record
should identify:

- system/provider
- model/version where available
- purpose
- activity affected
- decision authority
- reviewer verification

AI-generated material must not silently become an independent
human determination.

## 12. Integrity

Where implemented, active-review records may reference:

Artifact
→ Hash
→ Manifest
→ Attestation
→ Registry Record

The existence of this baseline does not establish that cryptographic
integrity mechanisms are implemented or verified.

## 13. Completion Boundary

An active review may transition to COMPLETED only when the applicable
review activities have reached their declared completion criteria.

Completion does not imply:

- independent verification
- certification
- accreditation
- scientific validation
- security certification

unless separately established.

## 14. Traceability

The active review record should maintain references to:

- review scope
- reviewer requirements
- evidence package
- review application
- findings
- test/reproduction records
- final review record

## 15. Change Control

Changes to active review state or material review parameters must be:

1. Explicitly identified.
2. Versioned where applicable.
3. Traceable.
4. Recorded in the review history.

Historical state must not be silently rewritten.

## 16. Current State

DESIGNED

Implementation and automated validation are separate activities.
