# EKE Review Applications
# Review Applications Baseline v0.1

## Status

DESIGNED — APPLICATIONS BASELINE

This document defines the initial application contract for submitting
requests for EKE Open Review.

It does not constitute evidence that any review has been accepted,
performed, independently verified, certified, accredited, or completed.

## 1. Application Identity

Every review application must have a unique Application ID.

Format:

EKE-RA-YYYY-NNN

Example:

EKE-RA-2026-001

Application IDs must not be reused.

## 2. Review Reference

Each application must identify the requested review.

Where a Review ID has not yet been assigned, the application must
remain distinguishable from the eventual review record.

## 3. Applicant

The application should identify:

- Applicant ID
- Applicant role
- Organization where applicable
- Contact reference
- Relationship to the subject
- Conflict-of-interest declaration

Sensitive personal information must not be unnecessarily exposed
in the public application record.

## 4. Subject

The application must identify:

- Subject name
- Subject version
- Subject artifact
- Artifact identifier where applicable
- Repository or source reference where applicable

## 5. Requested Review Scope

The applicant must describe:

### Requested In Scope

The claims, requirements, specifications, implementations,
or artifacts proposed for review.

### Requested Out of Scope

Known exclusions or boundaries.

The requested scope does not become the final review scope
automatically.

## 6. Evidence Declaration

The application should identify the evidence expected to be available.

Evidence may include:

- source documents
- source code
- repositories
- datasets
- test artifacts
- execution outputs
- configurations
- manifests
- integrity records

Evidence availability must not be interpreted as evidence validity.

## 7. Requested Review Level

The applicant may request:

R0 — Document Review

R1 — Technical Review

R2 — Independent Reproduction

R3 — Multi-Implementation Verification

R4 — Formal / Mathematical / Security Review

R5 — Institutional / Standards-Level Review

Requested Review Level is not a certification claim.

## 8. AI Declaration

The applicant must disclose known AI participation relevant to
the submitted material where applicable.

The declaration should identify:

- AI usage
- system/provider where known
- model/version where known
- purpose
- generated or transformed material

Applicant disclosure does not replace reviewer AI disclosure.

## 9. Application States

Supported architectural states:

DRAFT
→ SUBMITTED
→ SCREENING
→ ACCEPTED
→ REJECTED
→ WITHDRAWN
→ CONVERTED_TO_REVIEW

A rejected or withdrawn application must remain historically traceable.

## 10. Screening Boundary

Application screening determines whether the submission is
sufficiently defined for consideration.

Screening does not constitute technical verification of the subject.

## 11. Acceptance Boundary

Acceptance of an application does not mean:

- the subject is correct
- the claims are valid
- the evidence is sufficient
- the reviewer is independent
- the review will produce a positive result
- certification exists

## 12. Conversion to Review

An accepted application may be converted into a formal Review Record.

The resulting Review ID must be permanently linked to the
originating Application ID.

## 13. Traceability

The application should remain traceable through:

Application
→ Screening
→ Acceptance / Rejection
→ Review ID
→ Review Scope
→ Evidence
→ Review Result

Historical application records must not be silently overwritten.

## 14. Change Control

Changes to an application after submission must be:

1. Explicitly identified.
2. Versioned.
3. Traceable.
4. Recorded in the application history.

Material changes may require renewed screening.

## 15. Non-Claims

This baseline does not claim:

- acceptance of any review
- reviewer assignment
- independent verification
- certification
- accreditation
- scientific validation
- security certification
- production readiness

unless separately established through an appropriate process
and identifiable evidence.

## 16. Current State

DESIGNED

Implementation and automated validation are separate activities.
