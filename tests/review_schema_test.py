import json
from pathlib import Path


def test_review_schema_exists():
    path = Path("schemas/review.schema.json")
    assert path.exists()

    schema = json.loads(path.read_text())
    assert schema["title"] == "EKE Review Record"
    assert "review_id" in schema["required"]
    assert "status" in schema["required"]
    assert "scope" in schema["required"]
