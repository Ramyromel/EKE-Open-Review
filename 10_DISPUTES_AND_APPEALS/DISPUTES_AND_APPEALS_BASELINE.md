# EKE Disputes and Appeals
# Disputes & Appeals Baseline v0.1

## Status

DESIGNED — DISPUTE AND APPEAL ARCHITECTURE

This document defines the initial dispute and appeal boundary
for an EKE Open Review.

It does not constitute evidence that any dispute has been
adjudicated, resolved, independently verified, certified,
accredited, or legally determined.

## 1. Purpose

The dispute and appeal layer provides a structured mechanism
for challenging review findings, review procedures, evidence
interpretations, determinations, or certificate states.

A dispute is a recorded challenge.

An appeal is a structured request for reconsideration of an
eligible determination.

Neither mechanism automatically invalidates the underlying
review.

## 2. Dispute Identity

Every dispute must have a unique Dispute ID.

Format:

EKE-DSP-YYYY-NNN

Example:

EKE-DSP-2026-001

Dispute IDs must not be reused.

## 3. Appeal Identity

Every appeal must have a unique Appeal ID.

Format:

EKE-APL-YYYY-NNN

Example:

EKE-APL-2026-001

Appeal IDs must not be reused.

## 4. Review Reference

Every dispute or appeal must identify the review to which
the challenge relates.

Where applicable, it may also reference:

- Review ID
- Evidence ID
- Finding ID
- Certificate ID
- Registry record
- Previous dispute
- Previous appeal

A dispute or appeal must not silently create a new review.

## 5. Grounds

A dispute or appeal should identify the grounds for challenge.

Possible grounds include:

- procedural non-conformity
- evidence omission
- evidence interpretation
- factual error
- reproducibility issue
- scope violation
- independence concern
- integrity concern
- determination inconsistency
- newly available evidence
- other explicitly stated grounds

The selected ground does not itself establish that the allegation
is valid.

## 6. Evidence Boundary

Every substantive dispute or appeal should identify its
evidence basis.

Evidence may include:

- review records
- evidence packages
- execution results
- source artifacts
- integrity records
- reviewer attestations
- correspondence
- newly submitted evidence

Evidence outside the declared boundary must not be silently
treated as established fact.

## 7. Status Lifecycle

A dispute may progress through states such as:

SUBMITTED
→ ACCEPTED
→ UNDER_REVIEW
→ DETERMINED
→ RESOLVED

It may also become:

REJECTED
WITHDRAWN
SUPERSEDED
CHALLENGED

An appeal may progress through states such as:

SUBMITTED
→ ACCEPTED
→ UNDER_REVIEW
→ DETERMINED
→ RESOLVED

The exact transition rules require explicit implementation.

## 8. Independence

Where an appeal or dispute is designated for independent review,
the applicable independence requirements must be explicitly recorded.

Independence must not be inferred from terminology alone.

## 9. Separation of Roles

The dispute and appeal process should distinguish:

- complainant
- respondent
- reviewer
- appeal reviewer
- decision authority

A participant's role must be explicitly represented where
role separation is required.

## 10. Determination

A dispute or appeal determination must identify:

- determination status
- decision basis
- evidence considered
- applicable scope
- limitations
- decision authority where applicable

A determination must remain bounded by the evidence and procedure
actually applied.

## 11. Effect on Review State

A dispute or appeal does not automatically change:

- review status
- verification status
- certificate status
- registry status

Any resulting state change must be explicitly recorded and
traceable.

## 12. Certificate Relationship

Where a dispute concerns a certificate, the certificate may
become:

CHALLENGED
SUPERSEDED
REVOKED

only through an explicit process and identifiable evidence.

A challenge alone must not be represented as revocation.

## 13. Registry Relationship

Resolved disputes and appeals should remain traceable to the
corresponding review and registry records.

Historical records must not be silently overwritten.

## 14. AI Participation

Where AI participates in dispute or appeal analysis, the record
should identify:

- system/provider
- model/version where available
- purpose
- decision authority
- reviewer verification

AI assistance must not silently become an independent human
determination.

## 15. Non-Claims

This baseline does not claim:

- legal adjudication
- regulatory authority
- certification authority
- accreditation
- scientific validation
- security certification

unless separately established by an appropriate authority.

## 16. Change Control

Changes to the dispute and appeal architecture must be:

1. Explicitly identified.
2. Versioned.
3. Traceable.
4. Reviewed for impact.
5. Tested where implementation is affected.

## 17. Current State

DESIGNED

Implementation, automated validation, adjudication authority,
and external legal or institutional recognition remain separate
concerns.
