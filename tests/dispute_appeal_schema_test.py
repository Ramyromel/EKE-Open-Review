import json
from pathlib import Path


SCHEMA_PATH = Path("schemas/dispute_appeal.schema.json")


def load_schema():
    return json.loads(SCHEMA_PATH.read_text())


def test_dispute_appeal_schema_exists():
    assert SCHEMA_PATH.exists()

    schema = load_schema()

    assert schema["title"] == "EKE Dispute and Appeal Record"
    assert schema["type"] == "object"
    assert schema["additionalProperties"] is False


def test_required_fields():
    schema = load_schema()

    required = schema["required"]

    assert "record_type" in required
    assert "record_id" in required
    assert "review_id" in required
    assert "status" in required
    assert "grounds" in required


def test_record_type_enum():
    schema = load_schema()

    assert schema["properties"]["record_type"]["enum"] == [
        "DISPUTE",
        "APPEAL",
    ]


def test_record_id_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["record_id"]["pattern"]
        == "^EKE-(DSP|APL)-[0-9]{4}-[0-9]{3}$"
    )


def test_review_id_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["review_id"]["pattern"]
        == "^EKE-IR-[0-9]{4}-[0-9]{3}$"
    )


def test_status_values():
    schema = load_schema()

    statuses = schema["properties"]["status"]["enum"]

    assert "SUBMITTED" in statuses
    assert "UNDER_REVIEW" in statuses
    assert "DETERMINED" in statuses
    assert "RESOLVED" in statuses
    assert "REJECTED" in statuses
    assert "WITHDRAWN" in statuses


def test_grounds_are_required_and_non_empty():
    schema = load_schema()

    grounds = schema["properties"]["grounds"]

    assert grounds["type"] == "array"
    assert grounds["minItems"] == 1


def test_certificate_id_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["certificate_ids"]["items"]["pattern"]
        == "^EKE-CERT-[0-9]{4}-[0-9]{3}$"
    )


def test_additional_properties_disabled():
    schema = load_schema()

    assert schema["additionalProperties"] is False
