# EKE Review Certificate
# Certificate Baseline v0.1

## Status

EXPERIMENTAL — CERTIFICATE ARCHITECTURE

This document defines the experimental certificate boundary
for an EKE Open Review.

It does not constitute evidence of certification, accreditation,
scientific validation, security certification, or production readiness.

## 1. Purpose

The certificate layer provides a structured record of the
review state and the evidence supporting that state.

A certificate is a representation of a review record.

It must not be interpreted as independent certification merely
because a certificate record exists.

## 2. Certificate Identity

Every certificate must have a unique Certificate ID.

Format:

EKE-CERT-YYYY-NNN

Example:

EKE-CERT-2026-001

Certificate IDs must not be reused.

## 3. Review Reference

Every certificate must reference the Review ID from which
the certificate was derived.

The certificate must not exist as an independent review authority.

## 4. Certificate Scope

A certificate may identify:

- review identity
- review scope
- review status
- evidence references
- verification state
- integrity metadata
- reviewer attestation
- AI disclosure
- issuance timestamp

The certificate must remain bounded by the underlying review record.

## 5. Verification Boundary

A certificate may represent a verification state only when
that state is supported by identifiable review evidence.

The existence of a certificate must not upgrade:

DESIGNED → IMPLEMENTED
IMPLEMENTED → TESTED
TESTED → VERIFIED
VERIFIED → INDEPENDENTLY REPRODUCED

without corresponding evidence.

## 6. Attestation

Where reviewer attestation is included, the certificate should
identify:

- reviewer reference
- attestation statement
- attestation timestamp
- applicable review scope

Attestation is distinct from certification authority.

## 7. Integrity Metadata

Where implemented, a certificate may reference:

Artifact
→ Hash
→ Manifest
→ Cryptographic Root
→ Signature

Integrity metadata must not be represented as cryptographic assurance
unless the underlying mechanism has been implemented and verified.

## 8. AI Disclosure

Where AI systems participated in the review, the certificate should
reference the applicable AI disclosure information.

AI participation must not be silently represented as independent
human determination.

## 9. Issuance Boundary

Certificate issuance must identify:

- certificate identity
- referenced review
- issuance state
- issuer reference where applicable
- issuance timestamp

The certificate layer must not imply authority beyond the authority
actually established by the issuing process.

## 10. Revocation and Supersession

A certificate may become:

- ACTIVE
- SUPERSEDED
- REVOKED
- CHALLENGED

A later certificate must not silently overwrite historical certificate
records.

Changes in certificate state must remain traceable.

## 11. Challenge Relationship

A certificate may be associated with a challenge or dispute.

A challenge does not automatically invalidate the underlying review.

The challenge state must be represented explicitly.

## 12. Non-Claims

This certificate baseline does not claim:

- certification authority
- accreditation
- scientific validity
- regulatory approval
- security certification
- production readiness

unless separately established through an appropriate authority
and identifiable evidence.

## 13. Current State

EXPERIMENTAL

Certificate implementation, automated validation, cryptographic
assurance, and external authority remain separate concerns.

## 14. Change Control

Changes to the certificate architecture must be:

1. Explicitly identified.
2. Versioned.
3. Traceable.
4. Reviewed for impact.
5. Tested where implementation is affected.
