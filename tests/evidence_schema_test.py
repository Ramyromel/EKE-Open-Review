import json
from pathlib import Path


def test_evidence_schema_exists():
    path = Path("schemas/evidence.schema.json")
    assert path.exists()

    schema = json.loads(path.read_text())

    assert schema["title"] == "EKE Evidence Record"

    required = schema["required"]

    assert "evidence_id" in required
    assert "source_class" in required
    assert "status" in required
    assert "review_id" in required


def test_evidence_id_pattern():
    schema = json.loads(
        Path("schemas/evidence.schema.json").read_text()
    )

    pattern = schema["properties"]["evidence_id"]["pattern"]

    assert pattern == "^EKE-EV-[0-9]{4}-[0-9]{3}$"


def test_evidence_review_id_pattern():
    schema = json.loads(
        Path("schemas/evidence.schema.json").read_text()
    )

    pattern = schema["properties"]["review_id"]["pattern"]

    assert pattern == "^EKE-IR-[0-9]{4}-[0-9]{3}$"
