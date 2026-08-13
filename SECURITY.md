# Security Policy

## Scope

EKE Open Review is an experimental open architecture.

The existence of security-related documentation, schemas, workflows,
or controls does not constitute a claim of security certification,
production security, or complete security assurance.

## Reporting a Vulnerability

If you identify a security vulnerability affecting the repository,
please avoid publicly disclosing exploitable details before a
responsible assessment can be performed.

Where private reporting is available through the repository hosting
platform, use the platform's private security reporting mechanism.

If private reporting is unavailable, open a minimal public issue
without including credentials, private keys, sensitive personal data,
or directly exploitable payloads.

## What to Include

A useful security report should contain, where possible:

- affected component
- affected version or commit
- vulnerability description
- reproduction steps
- expected behavior
- observed behavior
- security impact
- suggested mitigation

Do not include:

- private keys
- passwords
- access tokens
- confidential credentials
- unnecessary personal information

## Security Claims

Security properties must be supported by identifiable evidence.

The project distinguishes:

DESIGNED
→ IMPLEMENTED
→ TESTED
→ VERIFIED
→ INDEPENDENTLY REPRODUCED

A security control must not be described as verified merely because
its architectural design exists.

## Cryptographic Integrity

Hashing, manifests, signatures, commitments, blockchain anchors,
or related mechanisms must not be represented as cryptographic
assurance unless the underlying implementation has been tested and
appropriately verified.

## AI-Assisted Analysis

AI may be used as an analysis aid.

AI-generated security findings must not automatically be treated as
independent human security determinations.

## Current Security Status

The repository should be considered experimental unless a component
is explicitly identified otherwise through documented evidence.

Security review, penetration testing, formal verification, and
independent security assessment are separate activities.
