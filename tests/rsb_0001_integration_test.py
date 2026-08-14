import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DIR = ROOT / "04_EVIDENCE_PACKAGE" / "RSB-0001"
REGISTRY_PATH = ROOT / "09_REVIEW_REGISTRY" / "RSB-0001-evidence-package.json"
REGISTRY_SCHEMA_PATH = ROOT / "schemas" / "review_registry.schema.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_rsb_0001_package_boundary_exists():
    assert (PACKAGE_DIR / "README.md").exists()
    assert (PACKAGE_DIR / "metadata.json").exists()


def test_rsb_0001_metadata_declares_source_pending_without_fabrication():
    metadata = load_json(PACKAGE_DIR / "metadata.json")

    assert metadata["artifact_id"] == "RSB-0001"
    assert metadata["artifact_filename"] == "RSB-0001.md"
    assert metadata["artifact_version"] == "1.0"
    assert metadata["repository_artifact_status"] == "PENDING"
    assert metadata["integrity"]["value"] is None
    assert metadata["integrity"]["status"] == "NOT_ESTABLISHED"
    assert metadata["review_id"] is None
    assert metadata["verification_status"] == "NOT_VERIFIED"
    assert metadata["review_result_status"] == "NOT_ESTABLISHED"
    assert metadata["certification_status"] == "NOT_ISSUED"


def test_rsb_0001_registry_entry_conforms_to_schema():
    schema = load_json(REGISTRY_SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)

    record = load_json(REGISTRY_PATH)
    Draft202012Validator(schema).validate(record)


def test_rsb_0001_registry_discoverability():
    record = load_json(REGISTRY_PATH)

    assert record["object"]["type"] == "EVIDENCE_PACKAGE"
    assert record["object"]["id"] == "RSB-0001"
    assert record["object"]["version"] == "1.0"
    assert record["state"] == "ACTIVE"
    assert "review_id" not in record
    assert "certificate_id" not in record


def test_rsb_0001_does_not_create_verification_result():
    metadata = load_json(PACKAGE_DIR / "metadata.json")

    assert metadata["evidence_record_status"] == "NOT_INSTANTIATED"
    assert metadata["reproduction_status"] == "NO_POPULATED_RUN_ARTIFACTS"
    assert metadata["verification_status"] == "NOT_VERIFIED"
    assert metadata["review_result_status"] == "NOT_ESTABLISHED"
    assert metadata["certification_status"] == "NOT_ISSUED"
