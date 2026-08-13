# Contributing to EKE Open Review

Thank you for contributing to EKE Open Review.

The project is designed around evidence-first, traceable, and
reproducible technical review.

## 1. Contribution Principles

Contributions should prioritize:

- correctness
- traceability
- reproducibility
- security
- explicit scope
- testability
- backward compatibility where applicable

Do not introduce claims of verification, certification, accreditation,
or production readiness without identifiable supporting evidence.

## 2. Development States

The project distinguishes:

DESIGNED
→ IMPLEMENTED
→ TESTED
→ VERIFIED
→ INDEPENDENTLY REPRODUCED
→ PRODUCTION READY

A higher state must not be inferred from a lower state.

## 3. Evidence First

The core principle is:

> No Evidence → No Verification

Changes affecting review determinations, evidence handling, integrity,
certificates, registries, or verification contracts should include
appropriate tests or other identifiable evidence.

## 4. Pull Requests

Pull requests should clearly describe:

- what changed
- why it changed
- affected components
- architectural impact
- compatibility impact
- security implications
- tests performed
- known limitations

Avoid unrelated changes in the same pull request.

## 5. Schema Changes

Changes to normative schemas should include:

- explicit version/change description
- updated fixtures where applicable
- validation tests
- compatibility analysis
- documentation updates where required

## 6. Verification Claims

Do not describe a component as VERIFIED, INDEPENDENTLY REPRODUCED,
CERTIFIED, or PRODUCTION READY unless the applicable requirements and
evidence have actually been satisfied.

## 7. AI-Assisted Contributions

AI-assisted contributions are permitted.

Where AI materially contributes to a review, verification process,
security analysis, or determination, the relevant activity should
remain explicitly disclosed.

AI assistance does not constitute independent human verification.

## 8. Security

Security-sensitive issues should follow the project's security
reporting process rather than being disclosed publicly before an
appropriate assessment.

## 9. Code Quality

Before submitting a change, contributors should run the applicable:

- schema validation
- unit tests
- integration tests
- static analysis
- formatting checks
- repository integrity checks

Only checks relevant to the changed component are required.

## 10. Scope Discipline

Do not expand the architectural scope merely to increase apparent
feature coverage.

A smaller verified boundary is preferable to a larger unsupported claim.
