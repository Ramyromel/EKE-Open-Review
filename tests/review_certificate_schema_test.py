import json
from pathlib import Path


def load_schema():
    path = Path("schemas/review_certificate.schema.json")
    assert path.exists()

    return json.loads(path.read_text())


def test_review_certificate_schema_exists():
    schema = load_schema()

    assert schema["title"] == "EKE Review Certificate"
    assert schema["type"] == "object"

    required = schema["required"]

    assert "certificate_id" in required
    assert "review_id" in required
    assert "status" in required
    assert "issuance" in required


def test_certificate_id_pattern():
    schema = load_schema()

    pattern = schema["properties"]["certificate_id"]["pattern"]

    assert pattern == "^EKE-CERT-[0-9]{4}-[0-9]{3}$"


def test_review_id_pattern():
    schema = load_schema()

    pattern = schema["properties"]["review_id"]["pattern"]

    assert pattern == "^EKE-IR-[0-9]{4}-[0-9]{3}$"


def test_certificate_status_values():
    schema = load_schema()

    values = schema["properties"]["status"]["enum"]

    assert values == [
        "ACTIVE",
        "SUPERSEDED",
        "REVOKED",
        "CHALLENGED"
    ]


def test_verification_state_does_not_exceed_defined_architecture():
    schema = load_schema()

    values = schema["properties"]["verification_state"]["enum"]

    assert values == [
        "DESIGNED",
        "IMPLEMENTED",
        "TESTED",
        "VERIFIED",
        "INDEPENDENTLY_REPRODUCED"
    ]


def test_issuance_requirements():
    schema = load_schema()

    issuance = schema["properties"]["issuance"]

    assert "timestamp" in issuance["required"]
    assert "issuer_reference" in issuance["properties"]


def test_attestation_requirements():
    schema = load_schema()

    attestation = schema["properties"]["reviewer_attestation"]

    assert attestation["required"] == [
        "reviewer_reference",
        "attestation_statement",
        "attestation_timestamp"
    ]


def test_ai_disclosure_requires_explicit_usage_flag():
    schema = load_schema()

    disclosure = schema["properties"]["ai_disclosure"]

    assert "used" in disclosure["required"]
    assert disclosure["properties"]["used"]["type"] == "boolean"
