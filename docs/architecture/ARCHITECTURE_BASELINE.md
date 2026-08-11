# EKE Open Review
# Architecture Baseline v0.1

## Status

ARCHITECTURAL BASELINE — EXPERIMENTAL

This document defines the current architectural baseline of the
EKE Open Review system.

It does not constitute evidence that the described components are
implemented, independently verified, certified, accredited, or
production-ready.

## 1. Architectural Objective

EKE Open Review is designed as an open, auditable architecture for
the lifecycle of independent technical and scientific review.

The lifecycle is:

Review
→ Evidence
→ Verification
→ Reproduction
→ Attestation
→ Integrity
→ Registry
→ Challenge
→ Resolution

## 2. Core Principle

No Evidence → No Verification

No Integrity Record → No Trusted Review

A review result must remain traceable to the evidence and procedures
from which it was derived.

## 3. Layer Harmonization

The architecture is based on coordinated interaction between
specialized layers.

The existence of a layer does not imply that the complete system
has been implemented or verified.

## 4. Core Layers

### EKE Core

Knowledge and specification layer.

### EKE-ORP

EKE Open Review Protocol.

Defines the review lifecycle, scope, evidence handling,
reproduction, disclosure, attestation, publication, and challenge
processes.

### RVP

Review Verification Protocol.

Defines verification of review integrity, evidence linkage,
reproduction, result traceability, manifests, and signatures.

### RCP

Reviewer Credential Protocol.

Defines reviewer identity, institutional affiliation,
independence declarations, conflict disclosure, and public
attestation.

### AIRE

AI Integrity, Ethics & Quality.

Provides controls for AI-assisted review processes.

AI assistance does not by itself constitute review authority.

### Evidence Model

Defines evidence objects, provenance, traceability,
classification, integrity, and reproduction artifacts.

### Cryptographic Integrity Layer

Provides artifact hashes, manifests, commitments, signatures,
and cryptographic roots where implemented and verified.

### Registry

Provides persistent public records of review lifecycle states.

### Challenge System

Provides a mechanism for counter-evidence, disputes,
corrections, appeals, and resolution history.

### Certificate Layer

Defines the experimental architecture for verifiable review
certificates.

Certificates must not be interpreted as certification or
accreditation unless issued by an appropriately authorized body.

## 5. Review / Attestation / Certification Separation

These concepts are distinct.

Review:
what was examined and how.

Attestation:
what a reviewer declares they performed or observed.

Certification:
a formal determination made by an appropriately authorized
certification authority.

The system must never infer certification merely from review
completion or attestation.

## 6. Evidence Chain

Every substantive review determination should be traceable through:

Claim
→ Requirement
→ Evidence
→ Test
→ Reproduction
→ Result
→ Reviewer Attestation
→ Integrity Manifest

Missing links must be explicitly represented rather than inferred.

## 7. AI Disclosure

Where AI systems participate in a review, the review record should
identify:

- AI usage
- system/provider
- model/version where available
- purpose of use
- decision authority
- reviewer verification of AI-generated outputs
- confidential-data exposure status

AI-generated conclusions must not be silently represented as
independent human determinations.

## 8. Identity and Sensitive Data

Private identity verification and public verifiability are separate
concerns.

Sensitive identity information should not be exposed merely because
a public review record exists.

Where implemented, protection may use:

- encryption
- cryptographic commitments
- access control
- authorized disclosure
- signatures
- audit records

Encoding or obfuscation alone is not considered a security control.

## 9. Entity Provenance

The system should distinguish:

OBSERVED
VERIFIED
INFERRED
UNVERIFIED
HALLUCINATED / UNSUPPORTED

In particular:

Observed ≠ Verified ≠ Inferred

An entity appearing in supplied evidence must not automatically be
represented as independently verified in the external world.

## 10. Independent Reproduction

Independent reproduction is a separate verification dimension.

A reproduction record should identify:

- reviewed artifact
- input evidence
- implementation/runtime
- environment
- procedure
- outputs
- expected results
- observed results
- reproducibility status
- limitations

## 11. Integrity Model

Where cryptographic integrity is implemented, relevant artifacts
may be represented through:

Artifact
→ Hash
→ Manifest
→ Cryptographic Root
→ Signed Attestation
→ Registry Record

The existence of this architecture does not imply that a valid
cryptographic implementation currently exists.

## 12. Security Boundary

Client-controlled information must not be treated as authoritative
for security-sensitive decisions.

Authority-sensitive operations should be enforced by trusted
server-side or otherwise independently controlled components.

## 13. Experimental Certificate Boundary

The certificate layer is experimental.

A certificate record may attest to:

- review identity
- review scope
- evidence references
- verification state
- integrity metadata
- reviewer attestation
- AI disclosure
- timestamp

It must not claim scientific validity, accreditation, or external
certification unless those claims are independently established.

## 14. Architectural Maturity

Current state:

ARCHITECTURAL DEVELOPMENT

Future maturity states must be supported by explicit evidence.

Suggested progression:

DESIGNED
→ IMPLEMENTED
→ TESTED
→ VERIFIED
→ INDEPENDENTLY REPRODUCED
→ PRODUCTION READY

A higher state must not be inferred from a lower state.

## 15. Baseline Rule

This document is a design baseline.

Changes to the architecture should be:

1. Explicitly identified.
2. Versioned.
3. Traceable.
4. Reviewed for architectural impact.
5. Tested where implementation is affected.

## 16. Non-Claims

This baseline does not claim:

- external certification
- accreditation
- independent verification
- production readiness
- security certification
- cryptographic assurance
- scientific validation

unless separately established by evidence and an appropriate
verification process.
