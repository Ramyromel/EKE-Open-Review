import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "04_EVIDENCE_PACKAGE" / "RSB-0001"
REGISTRY = ROOT / "09_REVIEW_REGISTRY" / "RSB-0001-evidence-package.json"
REGISTRY_SCHEMA = ROOT / "schemas" / "review_registry.schema.json"

EXPECTED = {
    "Q01": {"entity": "LUXIONEX", "relation_type": "IS_CHILD_OF"},
    "Q02": {"entities": ["SULAI"]},
    "Q03": {"entity": "SULAI", "relation_type": "IS_PART_OF"},
    "Q04": False,
    "Q05": "RELATED_TO",
    "Q06": True,
    "Q07": "CANONICAL_ARCHITECTURE",
    "Q08": 1.0,
    "Q09": False,
    "Q10": "GOVERNANCE_SYSTEM",
}


def test_controlled_rsb_artifact_exists():
    assert (PACKAGE / "RSB-0001.md").is_file()
    text = (PACKAGE / "RSB-0001.md").read_text(encoding="utf-8")
    assert "RSB-0001" in text
    assert "Version: 1.0 | Status: ACTIVE" in text
    assert all(f"Q0{i}" in text for i in range(1, 10))
    assert "Q10" in text


def test_registry_entry_is_schema_valid_and_discoverable():
    schema = json.loads(REGISTRY_SCHEMA.read_text(encoding="utf-8"))
    record = json.loads(REGISTRY.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(record)
    assert record["object"] == {
        "type": "EVIDENCE_PACKAGE",
        "id": "RSB-0001",
        "version": "1.0",
        "source_reference": "04_EVIDENCE_PACKAGE/RSB-0001/RSB-0001.md",
    }
    assert record["state"] == "ACTIVE"


def test_reproduction_records_match_independently_generated_outputs():
    for run in (
        "2026-08-14-python-graph-runtime-a",
        "2026-08-14-node-graph-runtime-b",
    ):
        run_dir = PACKAGE / "runs" / run
        raw = json.loads((run_dir / "raw-outputs.json").read_text(encoding="utf-8"))
        result = json.loads((run_dir / "pass-fail.json").read_text(encoding="utf-8"))
        assert raw["normative_answer_data_loaded"] is False
        assert result["overall_pass"] is True
        assert {row["query_id"] for row in result["queries"]} == set(EXPECTED)
        for row in result["queries"]:
            assert row["expected"] == EXPECTED[row["query_id"]]
            assert row["observed"] == row["expected"]
            assert row["match"] is True


def test_two_passing_reproductions_exist():
    runs = list((PACKAGE / "runs").glob("2026-08-14-*/pass-fail.json"))
    assert len(runs) == 2


def test_no_verification_or_certification_claim_created():
    package_text = "\n".join(p.read_text(encoding="utf-8") for p in PACKAGE.rglob("*.md"))
    assert "CERTIFICATION_ISSUED" not in package_text
    assert "VERIFIED" not in package_text
    assert "ATTESTED" not in package_text
