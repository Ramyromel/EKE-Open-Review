# EKE Review Registry
# Registry Baseline v0.1

## Status

DESIGNED — REVIEW REGISTRY ARCHITECTURE

This document defines the initial registry boundary for EKE Open Review.

It does not constitute evidence that any review, certificate,
attestation, accreditation, or certification has been registered,
validated, or independently verified.

## 1. Purpose

The Review Registry provides a structured record of review-related
objects and their lifecycle state.

The registry is intended to provide:

- stable identifiers
- discoverability
- lifecycle state
- traceability
- relationship references
- historical continuity
- integrity references where available

The registry does not itself perform review verification.

## 2. Registry Objects

The registry may contain references to:

- review applications
- active reviews
- completed reviews
- review certificates
- evidence packages
- challenges and appeals
- audit records

A registry entry represents a record or reference to an object.
It does not replace the underlying object.

## 3. Registry Identity

Every registry entry must have a unique Registry ID.

Format:

EKE-REG-YYYY-NNN

Example:

EKE-REG-2026-001

Registry IDs must not be reused.

## 4. Object Identity

Every registry entry must identify the object being registered.

The object should include:

- object type
- object identifier
- object version where applicable
- source reference where applicable

The registry must not silently alter the identity of the registered object.

## 5. Supported Object Types

Initial supported object types are:

- REVIEW_APPLICATION
- ACTIVE_REVIEW
- COMPLETED_REVIEW
- REVIEW_CERTIFICATE
- EVIDENCE_PACKAGE
- CHALLENGE
- APPEAL
- AUDIT_RECORD

Additional object types require explicit versioning and change control.

## 6. Registry State

A registry entry may have one of the following states:

- ACTIVE
- SUPERSEDED
- REVOKED
- CHALLENGED

Registry state represents registry status only.

It must not be interpreted as a verification result.

## 7. Lifecycle Traceability

Registry transitions must remain historically traceable.

A later registry entry or state must not silently overwrite
the historical state of an earlier entry.

Where applicable, the registry should identify:

- previous entry
- superseding entry
- challenge reference
- revocation reference
- effective timestamp

## 8. Review Relationship

Where the registered object belongs to a review lifecycle,
the registry should preserve references to the applicable Review ID.

The registry must not create a review determination that does not
exist in the underlying review record.

## 9. Evidence Relationship

Where evidence is referenced, the registry should identify
the applicable Evidence ID or evidence package reference.

Registry registration does not establish evidence validity.

## 10. Certificate Relationship

Where a review certificate is registered, the registry should
identify the Certificate ID and the Review ID from which it derives.

A registry entry must not upgrade the authority of a certificate.

## 11. Integrity Metadata

Where implemented, registry entries may reference:

Artifact
→ Hash
→ Manifest
→ Cryptographic Root
→ Signature

Integrity metadata must not be represented as cryptographic assurance
unless the underlying mechanism has been implemented and verified.

## 12. Timestamps

Material registry events should identify timestamps.

At minimum, applicable records should distinguish:

- registration timestamp
- effective timestamp
- state-change timestamp

Timestamps must not be represented as proof of an event beyond
the evidence supporting them.

## 13. Source and Provenance

Where applicable, a registry entry should identify:

- source
- origin
- registration actor or system
- acquisition method
- integrity reference

The registry must preserve provenance rather than silently
substituting registry metadata for source evidence.

## 14. Challenge and Dispute Boundary

A registry entry may reference a challenge or dispute.

A challenge must be represented explicitly.

The existence of a challenge does not automatically invalidate
the underlying review or certificate.

## 15. Non-Claims

This registry baseline does not claim:

- independent verification
- certification
- accreditation
- scientific validation
- regulatory approval
- security certification
- legal authority

unless separately established through an appropriate process
and identifiable evidence.

## 16. Registry Authority Boundary

The registry is a record-keeping and traceability layer.

It must not be treated as:

- a certification authority
- a verification authority
- an accreditation authority
- a scientific authority

unless such authority is separately established.

## 17. Change Control

Changes to the registry architecture must be:

1. Explicitly identified.
2. Versioned.
3. Traceable.
4. Reviewed for impact.
5. Tested where implementation is affected.

Historical registry records must not be silently rewritten.

## 18. Current State

DESIGNED

Registry implementation, persistence guarantees, integrity protection,
query interfaces, access control, and external authority remain
separate concerns.
