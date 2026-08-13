import json
from pathlib import Path

import jsonschema
import pytest


def load_schema():
    path = Path("schemas/audit_log.schema.json")
    assert path.exists()
    return json.loads(path.read_text())


def test_audit_schema_exists():
    schema = load_schema()

    assert schema["title"] == "EKE Audit Log Record"
    assert schema["type"] == "object"


def test_audit_required_fields():
    schema = load_schema()

    assert schema["required"] == [
        "audit_id",
        "event_type",
        "event_timestamp",
        "object",
    ]


def test_audit_id_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["audit_id"]["pattern"]
        == "^EKE-AUDIT-[0-9]{4}-[0-9]{3}$"
    )


def test_review_id_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["review_id"]["pattern"]
        == "^EKE-IR-[0-9]{4}-[0-9]{3}$"
    )


def test_registry_reference_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["registry_reference"]["pattern"]
        == "^EKE-REG-[0-9]{4}-[0-9]{3}$"
    )


def test_certificate_reference_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["certificate_reference"]["pattern"]
        == "^EKE-CERT-[0-9]{4}-[0-9]{3}$"
    )


def test_event_types():
    schema = load_schema()

    assert schema["properties"]["event_type"]["enum"] == [
        "CREATED",
        "UPDATED",
        "STATE_CHANGED",
        "SUBMITTED",
        "ACCEPTED",
        "REJECTED",
        "WITHDRAWN",
        "COMPLETED",
        "ISSUED",
        "SUPERSEDED",
        "REVOKED",
        "CHALLENGED",
        "APPEALED",
        "RESOLVED",
    ]


def test_object_types():
    schema = load_schema()

    assert schema["properties"]["object"]["properties"]["type"]["enum"] == [
        "REVIEW_APPLICATION",
        "ACTIVE_REVIEW",
        "COMPLETED_REVIEW",
        "REVIEW_CERTIFICATE",
        "EVIDENCE_PACKAGE",
        "CHALLENGE",
        "APPEAL",
        "AUDIT_RECORD",
    ]


def test_object_identity_requirements():
    schema = load_schema()

    assert schema["properties"]["object"]["required"] == [
        "type",
        "id",
    ]


def test_actor_types():
    schema = load_schema()

    assert schema["properties"]["actor"]["properties"]["type"]["enum"] == [
        "HUMAN_REVIEWER",
        "REVIEW_PROCESS",
        "SYSTEM_PROCESS",
        "AUTOMATED_MECHANISM",
        "AI_ASSISTED_MECHANISM",
    ]


def test_historical_fields_exist():
    schema = load_schema()
    properties = schema["properties"]

    assert "previous_audit_id" in properties
    assert "previous_state" in properties
    assert "resulting_state" in properties


def test_traceability_fields_exist():
    schema = load_schema()
    properties = schema["properties"]

    assert "review_id" in properties
    assert "evidence_reference" in properties
    assert "registry_reference" in properties
    assert "certificate_reference" in properties
    assert "challenge_reference" in properties
    assert "disclosure_reference" in properties
    assert "integrity_reference" in properties


def test_evidence_and_challenge_reference_patterns():
    schema = load_schema()
    properties = schema["properties"]

    assert (
        properties["evidence_reference"]["pattern"]
        == "^EKE-EV-[0-9]{4}-[0-9]{3}$"
    )
    assert (
        properties["challenge_reference"]["pattern"]
        == "^EKE-(DSP|APL)-[0-9]{4}-[0-9]{3}$"
    )


def test_event_timestamp_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["event_timestamp"]["pattern"]
        == "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?Z$"
    )


def test_invalid_event_timestamp_is_rejected():
    schema = load_schema()
    record = {
        "audit_id": "EKE-AUDIT-2026-001",
        "event_type": "CREATED",
        "event_timestamp": "2026-08-12 00:00:00",
        "object": {"type": "ACTIVE_REVIEW", "id": "EKE-IR-2026-001"},
    }

    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(record, schema)


def test_invalid_evidence_reference_is_rejected():
    schema = load_schema()
    record = {
        "audit_id": "EKE-AUDIT-2026-001",
        "event_type": "CREATED",
        "event_timestamp": "2026-08-12T00:00:00Z",
        "object": {"type": "ACTIVE_REVIEW", "id": "EKE-IR-2026-001"},
        "evidence_reference": "ev-2026-001",
    }

    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(record, schema)
