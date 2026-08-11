import json
from pathlib import Path


def test_active_review_schema_exists():
    path = Path("schemas/active_review.schema.json")
    assert path.exists()

    schema = json.loads(path.read_text())

    assert schema["title"] == "EKE Active Review"

    required = schema["required"]

    assert "review_id" in required
    assert "status" in required
    assert "review_level" in required
    assert "scope_reference" in required
    assert "evidence_boundary" in required
    assert "current_phase" in required


def test_active_review_id_pattern():
    schema = json.loads(
        Path("schemas/active_review.schema.json").read_text()
    )

    pattern = schema["properties"]["review_id"]["pattern"]

    assert pattern == "^EKE-IR-[0-9]{4}-[0-9]{3}$"


def test_active_review_statuses():
    schema = json.loads(
        Path("schemas/active_review.schema.json").read_text()
    )

    statuses = schema["properties"]["status"]["enum"]

    assert statuses == [
        "DRAFT",
        "ACTIVE",
        "PAUSED",
        "BLOCKED",
        "COMPLETED",
    ]
