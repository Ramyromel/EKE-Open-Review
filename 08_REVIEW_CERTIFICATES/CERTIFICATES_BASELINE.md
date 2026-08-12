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

---

## 15. Certificate Profiles

The EKE certificate layer defines three certificate profiles.

### 15.1 VERIFIABLE

The VERIFIABLE profile represents a successful review outcome
supported by identifiable review evidence and the applicable
verification requirements.

It may represent:

- SUCCESSFUL_REVIEW
- VERIFIED

The existence of the certificate does not independently establish
certification authority.

### 15.2 FAILED

The FAILED profile represents a review attempt that did not satisfy
the applicable requirements.

It may represent:

- REVIEW_FAILED
- NON_CONFORMANT

Critical findings and their supporting evidence must remain
traceable to the underlying review.

A failed certificate is a historical review record and must not be
silently deleted or replaced by a later successful record.

### 15.3 AI_ASSISTED

The AI_ASSISTED profile represents a review in which AI systems
participated in the review process and the resulting determination
was subject to the applicable human verification requirements.

It may represent:

- AI_ASSISTED_HUMAN_VERIFIED
- PARTIALLY_VERIFIED

AI participation must remain explicitly disclosed.

AI assistance must not be represented as independent human
determination.

---

## 16. Cross-Layer Traceability

A certificate may reference the following layers:

BABT
→ Independent Verification
→ Evidence
→ Certificate
→ NFT
→ Registry
→ Audit Log

These references establish traceability relationships.

They do not, by themselves, constitute proof that the referenced
systems or cryptographic mechanisms have been independently verified.

---

## 17. BABT Reference

Where BABT is applicable, the certificate may contain a
BABT reference identifying the applicable attestation or
verification record.

The certificate must not infer BABT validity merely from the
existence of a reference.

BABT eligibility and semantics remain governed by the BABT layer.

---

## 18. NFT Representation

A certificate may have a corresponding NFT representation.

The NFT is a digital representation of the certificate record.

The NFT does not replace the certificate's underlying evidence,
review record, attestation, or verification process.

The NFT metadata should reference:

- certificate identity
- review identity
- certificate profile
- review outcome
- classification
- evidence root
- registry reference
- audit reference
- applicable BABT reference
- metadata URI
- blockchain anchor

Token ownership must not be interpreted as ownership of the
underlying reviewed intellectual or scientific claim unless such
rights are separately established.

---

## 19. Blockchain Anchor

Where implemented, the certificate may reference:

- blockchain network
- transaction reference
- block reference

Blockchain anchoring provides a persistence/reference mechanism.

It must not be represented as independent validation of the
underlying review.

---

## 20. Certificate Architecture

The logical certificate architecture is:

EKE Review Certificate
|
+-- VERIFIABLE
|   +-- SUCCESSFUL_REVIEW
|   +-- VERIFIED
|
+-- FAILED
|   +-- REVIEW_FAILED
|   +-- NON_CONFORMANT
|
+-- AI_ASSISTED
    +-- AI_ASSISTED_HUMAN_VERIFIED
    +-- PARTIALLY_VERIFIED

Each certificate remains bounded by the underlying review record.

---

## 21. NFT Boundary

NFT issuance must occur only after the applicable certificate
eligibility conditions have been satisfied.

NFT issuance must not:

- create verification status
- create review authority
- upgrade review classification
- replace reviewer attestation
- replace evidence
- replace BABT verification
- erase historical certificate states

The NFT is a representation layer, not the verification authority.

---

## 22. Non-Claims

The certificate/NFT architecture does not claim:

- legal ownership of the reviewed intellectual property
- scientific validity merely from tokenization
- certification authority merely from NFT issuance
- accreditation
- regulatory approval
- cryptographic assurance without verified implementation

unless separately established by identifiable authority and evidence.

---

## 23. Current State

EXPERIMENTAL

Certificate profiles and NFT representation are schema-level
architecture.

Smart-contract implementation, metadata publication,
blockchain anchoring, cryptographic signing, BABT integration,
and independent verification remain separate implementation
and verification concerns.
