# EKE Audit Log
# Audit Log Baseline v0.1

## Status

EXPERIMENTAL — AUDIT LOG ARCHITECTURE

This document defines the experimental audit-log boundary
for an EKE Open Review.

It does not constitute proof of tamper resistance,
cryptographic integrity, regulatory compliance,
security certification, or production readiness.

## 1. Purpose

The audit-log layer provides a structured historical record
of significant review-system events.

Its purpose is to preserve traceability across the review
lifecycle and to provide identifiable references to changes
affecting review objects and their states.

An audit record is a historical record.

It is not itself a review determination, evidence of correctness,
or certification authority.

## 2. Audit Record Identity

Every audit record must have a unique Audit Record ID.

Format:

EKE-AUDIT-YYYY-NNN

Example:

EKE-AUDIT-2026-001

Audit Record IDs must not be reused.

## 3. Event Identity

Each audit record should identify the event represented by
the record.

The event should remain associated with:

- event type
- event timestamp
- affected object
- object identifier
- actor or source reference where applicable

The audit layer must not invent an event that cannot be
identified from the underlying review process.

## 4. Object Reference

An audit record should identify the object affected by the event.

Supported object classes are bounded by the existing review
architecture, including:

- REVIEW_APPLICATION
- ACTIVE_REVIEW
- COMPLETED_REVIEW
- REVIEW_CERTIFICATE
- EVIDENCE_PACKAGE
- CHALLENGE
- APPEAL
- AUDIT_RECORD

The object reference must remain traceable to its source record.

## 5. Review Reference

Where an event belongs to a review lifecycle, the audit record
should reference the applicable Review ID.

Review reference:

EKE-IR-YYYY-NNN

The audit layer must not become an independent authority over
the review itself.

## 6. Event Types

The initial experimental event vocabulary may include:

- CREATED
- UPDATED
- STATE_CHANGED
- SUBMITTED
- ACCEPTED
- REJECTED
- WITHDRAWN
- COMPLETED
- ISSUED
- SUPERSEDED
- REVOKED
- CHALLENGED
- APPEALED
- RESOLVED

This vocabulary is extensible through explicit versioned change.

An event type must represent a recorded lifecycle action and
must not imply successful verification unless corresponding
evidence exists.

## 7. Historical Traceability

Audit records should preserve historical relationships.

Where an event represents a change from an earlier record,
the audit record may reference:

- previous audit record
- previous object state
- resulting object state
- related registry record
- supporting evidence reference

Historical records must not be silently overwritten.

A later record represents a later event; it does not erase
the historical existence of the earlier record.

## 8. State Representation

The audit record may identify:

- previous state
- resulting state

State transitions must remain bounded by the lifecycle of
the referenced object.

The audit log must not independently authorize a transition
that the underlying object model does not recognize.

## 9. Actor and Source

Where available, an audit record should identify the source
responsible for recording the event.

The source may be:

- human reviewer
- review process
- system process
- automated mechanism
- AI-assisted mechanism

Where AI participation is material, it should remain explicitly
identifiable and must not be silently represented as independent
human determination.

## 10. Evidence and Traceability

Where an audit event is supported by evidence, the record
should contain an evidence reference.

Audit records should remain traceable to:

- review
- object
- state transition
- evidence
- registry entry
- certificate or dispute record where applicable

Traceability does not itself establish validity.

## 11. Integrity Boundary

The audit-log architecture may later support integrity mechanisms
such as:

Artifact
→ Hash
→ Manifest
→ Cryptographic Root
→ Signature

However, cryptographic integrity must not be claimed unless
the underlying mechanism has actually been implemented and
verified.

An append-only design must not be represented as cryptographically
immutable merely because historical records are retained.

## 12. Ordering

Where timestamps are available, audit records should provide
an identifiable temporal ordering.

Timestamp presence does not by itself establish trusted time.

If ordering requires a stronger mechanism, that mechanism must
be separately specified and verified.

## 13. Audit Record Lifecycle

Audit records should remain historically identifiable.

A record may be:

- ACTIVE
- SUPERSEDED
- VOIDED

Lifecycle semantics must be explicit.

A later audit record must not silently overwrite the historical
record of an earlier event.

## 14. Relationship to Review Registry

The Review Registry is the record-keeping and traceability layer
for review objects.

The Audit Log records events affecting those objects.

An audit record may therefore reference a registry record.

The two layers must remain distinguishable:

Registry:
object state and lifecycle identity.

Audit Log:
historical event and traceability record.

## 15. Relationship to Evidence

Audit records are not equivalent to evidence.

An audit record may reference evidence supporting an event,
but the existence of the audit record does not establish the
truth or validity of that evidence.

## 16. Relationship to Certificates

A certificate may reference audit records where issuance,
state change, supersession, revocation, or challenge history
requires traceability.

An audit record does not create certification authority.

## 17. AI Disclosure

Where AI systems participate in an event or its recording,
the audit record should preserve the applicable disclosure
reference.

AI participation must not be silently represented as human
independent determination.

## 18. Non-Claims

This baseline does not claim:

- cryptographic immutability
- tamper-proof storage
- trusted timestamping
- regulatory compliance
- security certification
- accreditation
- scientific validity
- production readiness

unless separately established through implementation,
verification, and identifiable evidence.

## 19. Current State

EXPERIMENTAL

The Audit Log currently defines an architectural boundary
and record model.

A production audit implementation remains a separate concern.

## 20. Change Control

Changes to the audit-log architecture must be:

1. Explicitly identified.
2. Versioned.
3. Traceable.
4. Reviewed for impact.
5. Tested where implementation is affected.
