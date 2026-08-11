import json
from pathlib import Path


def test_review_scope_schema_exists():
    path = Path("schemas/review_scope.schema.json")
    assert path.exists()

    schema = json.loads(path.read_text())

    assert schema["title"] == "EKE Review Scope"

    required = schema["required"]

    assert "review_id" in required
    assert "subject" in required
    assert "scope" in required
    assert "evidence_boundary" in required
    assert "review_level" in required


def test_review_scope_id_pattern():
    schema = json.loads(
        Path("schemas/review_scope.schema.json").read_text()
    )

    pattern = schema["properties"]["review_id"]["pattern"]

    assert pattern == "^EKE-IR-[0-9]{4}-[0-9]{3}$"
