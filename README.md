# EKE Open Review

## EKE-ORP — EKE Open Review Protocol

EKE Open Review is an architecture for conducting, documenting,
verifying, reproducing, attesting, and auditing independent reviews
of EKE-related specifications and implementations.

## Core Principle

No Evidence → No Verification

No Integrity Record → No Trusted Review

## Status

ARCHITECTURAL DEVELOPMENT

This repository is under active development.

Descriptions of components, protocols, certificates, cryptographic
mechanisms, and verification layers are architectural definitions
unless an explicit implementation and verification record establishes
otherwise.

No experimental certificate constitutes external certification,
accreditation, or independent verification by itself.

## Repository Structure

- `00_INVITATION/` — review invitations
- `01_REVIEW_PROTOCOL/` — review protocol
- `02_REVIEW_SCOPE/` — review scope
- `03_REVIEWER_REQUIREMENTS/` — reviewer requirements
- `04_EVIDENCE_PACKAGE/` — controlled evidence packages
- `05_REVIEW_APPLICATIONS/` — review applications
- `06_ACTIVE_REVIEWS/` — active reviews
- `07_COMPLETED_REVIEWS/` — completed review records
- `08_REVIEW_CERTIFICATES/` — certificate artifacts
- `09_REVIEW_REGISTRY/` — review registry
- `10_DISPUTES_AND_APPEALS/` — challenges and appeals
- `11_AUDIT_LOG/` — audit records
- `schemas/` — machine-readable schemas
- `policies/` — governance policies
- `scripts/` — validation and automation
- `tests/` — automated tests
- `docs/` — architecture documentation
- `artifacts/` — controlled/generated artifacts

## Verification Rule

A component must not be marked `VERIFIED` merely because it is
described in documentation.

Verification requires:

1. Defined verification criteria
2. Identifiable evidence
3. Reproducible execution where applicable
4. Recorded result
5. Traceability to the reviewed artifact

## Review / Attestation / Certification

The repository distinguishes:

- **Review** — what was examined and how.
- **Attestation** — what a reviewer declares they performed or observed.
- **Certification** — a formal determination by an appropriately
  authorized certification authority.

These concepts must not be conflated.

## Experimental Certificate

The certificate architecture is currently experimental.

Any future certificate implementation must identify its evidence,
scope, verification state, integrity information, and authority.
