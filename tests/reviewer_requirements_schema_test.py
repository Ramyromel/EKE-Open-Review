import json
from pathlib import Path


def test_reviewer_requirements_schema_exists():
    path = Path("schemas/reviewer_requirements.schema.json")
    assert path.exists()

    schema = json.loads(path.read_text())

    assert schema["title"] == "EKE Reviewer Requirements"

    required = schema["required"]

    assert "reviewer_id" in required
    assert "status" in required
    assert "independence" in required
    assert "conflict_of_interest" in required
    assert "review_level" in required


def test_reviewer_id_pattern():
    schema = json.loads(
        Path("schemas/reviewer_requirements.schema.json").read_text()
    )

    pattern = schema["properties"]["reviewer_id"]["pattern"]

    assert pattern == "^EKE-RV-[0-9]{4}-[0-9]{4}$"
