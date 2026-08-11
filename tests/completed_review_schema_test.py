import json
from pathlib import Path


def test_completed_review_schema_exists():
    path = Path("schemas/completed_review.schema.json")
    assert path.exists()

    schema = json.loads(path.read_text())

    assert schema["title"] == "EKE Completed Review"

    required = schema["required"]

    assert "review_id" in required
    assert "status" in required
    assert "determination" in required


def test_completed_review_id_pattern():
    schema = json.loads(
        Path("schemas/completed_review.schema.json").read_text()
    )

    pattern = schema["properties"]["review_id"]["pattern"]

    assert pattern == "^EKE-IR-[0-9]{4}-[0-9]{3}$"
