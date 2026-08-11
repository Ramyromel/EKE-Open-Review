import json
from pathlib import Path


def test_review_application_schema_exists():
    path = Path("schemas/review_application.schema.json")
    assert path.exists()

    schema = json.loads(path.read_text())

    assert schema["title"] == "EKE Review Application"

    required = schema["required"]

    assert "application_id" in required
    assert "status" in required
    assert "subject" in required
    assert "requested_scope" in required
    assert "requested_review_level" in required


def test_review_application_id_pattern():
    schema = json.loads(
        Path("schemas/review_application.schema.json").read_text()
    )

    pattern = schema["properties"]["application_id"]["pattern"]

    assert pattern == "^EKE-RA-[0-9]{4}-[0-9]{3}$"


def test_review_application_status_values():
    schema = json.loads(
        Path("schemas/review_application.schema.json").read_text()
    )

    statuses = schema["properties"]["status"]["enum"]

    assert "DRAFT" in statuses
    assert "SUBMITTED" in statuses
    assert "SCREENING" in statuses
    assert "ACCEPTED" in statuses
    assert "REJECTED" in statuses
    assert "WITHDRAWN" in statuses
    assert "CONVERTED_TO_REVIEW" in statuses
