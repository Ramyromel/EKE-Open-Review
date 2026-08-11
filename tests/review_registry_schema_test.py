import json
from pathlib import Path


def load_schema():
    path = Path("schemas/review_registry.schema.json")
    assert path.exists()
    return json.loads(path.read_text())


def test_registry_schema_exists():
    schema = load_schema()

    assert schema["title"] == "EKE Review Registry Entry"
    assert schema["type"] == "object"

    required = schema["required"]

    assert "registry_id" in required
    assert "object" in required
    assert "state" in required


def test_registry_id_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["registry_id"]["pattern"]
        == "^EKE-REG-[0-9]{4}-[0-9]{3}$"
    )


def test_review_id_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["review_id"]["pattern"]
        == "^EKE-IR-[0-9]{4}-[0-9]{3}$"
    )


def test_certificate_id_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["certificate_id"]["pattern"]
        == "^EKE-CERT-[0-9]{4}-[0-9]{3}$"
    )


def test_registry_object_types():
    schema = load_schema()

    values = schema["properties"]["object"]["properties"]["type"]["enum"]

    assert values == [
        "REVIEW_APPLICATION",
        "ACTIVE_REVIEW",
        "COMPLETED_REVIEW",
        "REVIEW_CERTIFICATE",
        "EVIDENCE_PACKAGE",
        "CHALLENGE",
        "APPEAL",
        "AUDIT_RECORD"
    ]


def test_registry_state_values():
    schema = load_schema()

    values = schema["properties"]["state"]["enum"]

    assert values == [
        "ACTIVE",
        "SUPERSEDED",
        "REVOKED",
        "CHALLENGED"
    ]


def test_registry_object_identity_requirements():
    schema = load_schema()

    required = schema["properties"]["object"]["required"]

    assert required == ["type", "id"]


def test_historical_relationship_fields_exist():
    schema = load_schema()
    properties = schema["properties"]

    assert "previous_registry_id" in properties
    assert "effective_timestamp" in properties
    assert "state_change_timestamp" in properties


def test_traceability_references_exist():
    schema = load_schema()
    properties = schema["properties"]

    assert "review_id" in properties
    assert "evidence_reference" in properties
    assert "certificate_id" in properties
    assert "challenge_reference" in properties
    assert "revocation_reference" in properties
