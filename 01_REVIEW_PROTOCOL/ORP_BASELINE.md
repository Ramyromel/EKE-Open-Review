# EKE-ORP-0001
# EKE Open Review Protocol

## Status

DRAFT — ARCHITECTURAL IMPLEMENTATION

This document defines the initial protocol boundary for EKE Open Review.

It does not constitute evidence that the protocol is implemented,
tested, independently verified, certified, accredited, or production-ready.

## 1. Purpose

EKE-ORP defines the lifecycle for conducting, documenting,
verifying, reproducing, attesting, and auditing independent reviews
of EKE-related specifications and implementations.

## 2. Review Lifecycle

Review
→ Evidence
→ Verification
→ Reproduction
→ Attestation
→ Integrity
→ Registry
→ Challenge
→ Resolution

## 3. Core Rule

No Evidence → No Verification

No Integrity Record → No Trusted Review

## 4. Review Separation

Review:
what was examined and how.

Attestation:
what a reviewer declares they performed or observed.

Certification:
a formal determination made by an appropriately authorized
certification authority.

These concepts must not be conflated.

## 5. AI Disclosure

Where AI participates in a review, its use must be explicitly recorded.

The record should identify:

- system/provider
- model/version where available
- purpose
- decision authority
- reviewer verification
- confidential-data exposure status

AI assistance does not by itself constitute independent human review.

## 6. Evidence

Every substantive determination should identify its evidence basis.

Claims without identifiable evidence must not be represented as verified.

## 7. Reproduction

Where reproduction is applicable, the review record should identify:

- reviewed artifact
- input evidence
- implementation/runtime
- environment
- procedure
- expected results
- observed results
- reproducibility status
- limitations

## 8. Integrity

Where implemented, review artifacts may be protected by:

Artifact
→ Hash
→ Manifest
→ Cryptographic Root
→ Attestation
→ Registry Record

The existence of this protocol does not establish that such mechanisms
have already been implemented or verified.

## 9. Current State

DRAFT

Further protocol requirements require explicit versioning,
traceability, implementation, testing, and verification.
