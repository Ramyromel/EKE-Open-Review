import json
from pathlib import Path

import jsonschema
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "independent_verification.schema.json"


def load_schema():
    with SCHEMA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def valid_record():
    return {
        "verification_id": "EKE-IV-2026-001",
        "review_id": "EKE-IR-2026-001",
        "status": "DETERMINED",
        "outcome": "PASS",
        "subject": {
            "name": "EKE Test Subject",
            "version": "0.1"
        },
        "criteria": [
            "criterion-001"
        ],
        "evidence_references": [
            "EKE-EV-2026-001"
        ],
        "procedure": {
            "reference": "PROC-IV-001",
            "description": "Independent verification procedure"
        },
        "independence": {
            "status": "SATISFIED",
            "verifier_reference": "EKE-RV-2026-0001",
            "conflict_of_interest": "NONE_DECLARED"
        },
        "reproduction": {
            "status": "REPRODUCED",
            "artifact_reference": "artifact-001",
            "result_reference": "result-001"
        },
        "multi_implementation": {
            "status": "NOT_APPLICABLE"
        },
        "determination": {
            "statement": "Verification criteria satisfied.",
            "timestamp": "2026-08-12T00:00:00Z",
            "limitations": []
        }
    }


def test_independent_verification_schema_is_valid():
    schema = load_schema()
    jsonschema.Draft202012Validator.check_schema(schema)


def test_valid_independent_verification_record():
    schema = load_schema()
    record = valid_record()

    jsonschema.validate(record, schema)


def test_invalid_verification_id_is_rejected():
    schema = load_schema()
    record = valid_record()

    record["verification_id"] = "INVALID"

    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(record, schema)


def test_missing_evidence_is_rejected():
    schema = load_schema()
    record = valid_record()

    del record["evidence_references"]

    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(record, schema)


def test_invalid_outcome_is_rejected():
    schema = load_schema()
    record = valid_record()

    record["outcome"] = "VERIFIED"

    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(record, schema)



def test_invalid_determination_timestamp_is_rejected():
    schema = load_schema()
    record = valid_record()

    record["determination"]["timestamp"] = "2026-08-12"

    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(record, schema)


def test_evidence_reference_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["evidence_references"]["items"]["pattern"]
        == "^EKE-EV-[0-9]{4}-[0-9]{3}$"
    )


def test_invalid_evidence_reference_value_is_rejected():
    schema = load_schema()
    record = valid_record()
    record["evidence_references"] = ["evidence-001"]

    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(record, schema)
