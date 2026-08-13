import json
from pathlib import Path


def load_schema():
    path = Path("schemas/review_certificate.schema.json")
    assert path.exists()

    return json.loads(path.read_text())


def test_review_certificate_schema_exists():
    schema = load_schema()

    assert schema["title"] == "EKE Review Certificate"
    assert schema["type"] == "object"

    required = schema["required"]

    assert "certificate_id" in required
    assert "review_id" in required
    assert "status" in required
    assert "issuance" in required


def test_certificate_id_pattern():
    schema = load_schema()

    pattern = schema["properties"]["certificate_id"]["pattern"]

    assert pattern == "^EKE-CERT-[0-9]{4}-[0-9]{3}$"


def test_review_id_pattern():
    schema = load_schema()

    pattern = schema["properties"]["review_id"]["pattern"]

    assert pattern == "^EKE-IR-[0-9]{4}-[0-9]{3}$"


def test_certificate_status_values():
    schema = load_schema()

    values = schema["properties"]["status"]["enum"]

    assert values == [
        "ACTIVE",
        "SUPERSEDED",
        "REVOKED",
        "CHALLENGED",
    ]


def test_verification_state_does_not_exceed_defined_architecture():
    schema = load_schema()

    values = schema["properties"]["verification_state"]["enum"]

    assert values == [
        "DESIGNED",
        "IMPLEMENTED",
        "TESTED",
        "VERIFIED",
        "INDEPENDENTLY_REPRODUCED",
    ]


def test_issuance_requirements():
    schema = load_schema()

    issuance = schema["properties"]["issuance"]

    assert "timestamp" in issuance["required"]
    assert "issuer_reference" in issuance["properties"]


def test_attestation_requirements():
    schema = load_schema()

    attestation = schema["properties"]["reviewer_attestation"]

    assert attestation["required"] == [
        "reviewer_reference",
        "attestation_statement",
        "attestation_timestamp",
    ]


def test_certificate_timestamps_have_utc_iso8601_pattern():
    schema = load_schema()

    issuance_timestamp = (
        schema["properties"]["issuance"]["properties"]["timestamp"]["pattern"]
    )
    attestation_timestamp = (
        schema["properties"]["reviewer_attestation"]["properties"][
            "attestation_timestamp"
        ]["pattern"]
    )

    expected_pattern = (
        "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?Z$"
    )

    assert issuance_timestamp == expected_pattern
    assert attestation_timestamp == expected_pattern


def test_ai_disclosure_requires_explicit_usage_flag():
    schema = load_schema()

    disclosure = schema["properties"]["ai_disclosure"]

    assert "used" in disclosure["required"]
    assert disclosure["properties"]["used"]["type"] == "boolean"


def test_certificate_type_profiles():
    schema = load_schema()

    values = schema["properties"]["certificate_type"]["enum"]

    assert values == [
        "VERIFIABLE",
        "FAILED",
        "AI_ASSISTED",
    ]


def test_certificate_outcomes():
    schema = load_schema()

    values = schema["properties"]["review_outcome"]["enum"]

    assert values == [
        "SUCCESSFUL_REVIEW",
        "REVIEW_FAILED",
        "AI_ASSISTED_HUMAN_VERIFIED",
    ]


def test_certificate_classifications():
    schema = load_schema()

    values = schema["properties"]["classification"]["enum"]

    assert values == [
        "VERIFIED",
        "NON_CONFORMANT",
        "PARTIALLY_VERIFIED",
    ]


def test_certificate_cross_layer_references():
    schema = load_schema()

    properties = schema["properties"]

    assert "babt_reference" in properties
    assert "registry_reference" in properties
    assert "audit_reference" in properties
    assert "evidence_root" in properties


def test_registry_reference_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["registry_reference"]["pattern"]
        == "^EKE-REG-[0-9]{4}-[0-9]{3}$"
    )


def test_audit_reference_pattern():
    schema = load_schema()

    assert (
        schema["properties"]["audit_reference"]["pattern"]
        == "^EKE-AUDIT-[0-9]{4}-[0-9]{3}$"
    )


def test_nft_structure():
    schema = load_schema()

    nft = schema["properties"]["nft"]

    assert nft["type"] == "object"
    assert nft["required"] == ["enabled"]

    properties = nft["properties"]

    assert "token_id" in properties
    assert "contract_reference" in properties
    assert "chain_reference" in properties
    assert "metadata_uri" in properties


def test_blockchain_anchor_structure():
    schema = load_schema()

    anchor = schema["properties"]["blockchain_anchor"]

    assert anchor["type"] == "object"

    properties = anchor["properties"]

    assert "network" in properties
    assert "transaction_reference" in properties
    assert "block_reference" in properties


def test_babt_reference_structure():
    schema = load_schema()

    babt = schema["properties"]["babt_reference"]

    assert babt["type"] == "object"
    assert babt["additionalProperties"] is False

    assert babt["required"] == [
        "network",
        "contract_address",
        "token_id",
        "token_standard",
        "holding_address",
    ]


def test_babt_contract_address_pattern():
    schema = load_schema()

    pattern = (
        schema["properties"]["babt_reference"]
        ["properties"]["contract_address"]["pattern"]
    )

    assert pattern == "^0x[a-fA-F0-9]{40}$"


def test_babt_token_id_pattern():
    schema = load_schema()

    pattern = (
        schema["properties"]["babt_reference"]
        ["properties"]["token_id"]["pattern"]
    )

    assert pattern == "^[0-9]+$"


def test_babt_token_standard():
    schema = load_schema()

    values = (
        schema["properties"]["babt_reference"]
        ["properties"]["token_standard"]["enum"]
    )

    assert values == ["BEP-721"]


def test_babt_reference_actual_contract_example():
    schema = load_schema()

    examples = (
        schema["properties"]["babt_reference"]
        ["properties"]["contract_address"]["examples"]
    )

    assert examples == [
        "0x2B09d47D550061f995A3b5C6F0Fd58005215D7c8"
    ]


def test_babt_reference_actual_token_example():
    schema = load_schema()

    examples = (
        schema["properties"]["babt_reference"]
        ["properties"]["token_id"]["examples"]
    )

    assert examples == ["930387"]


def test_babt_reference_actual_holding_address_example():
    schema = load_schema()

    examples = (
        schema["properties"]["babt_reference"]
        ["properties"]["holding_address"]["examples"]
    )

    assert examples == [
        "0xf6F211bEEb7bbA594c4B0B93708fD709318F32Eb"
    ]


def test_nft_includes_token_standard():
    schema = load_schema()

    properties = schema["properties"]["nft"]["properties"]

    assert "token_standard" in properties
    assert properties["token_standard"]["enum"] == ["BEP-721"]


def test_nft_includes_holding_address():
    schema = load_schema()

    properties = schema["properties"]["nft"]["properties"]

    assert "holding_address" in properties


def test_valid_babt_certificate_fixture_conforms_to_schema():
    from jsonschema import Draft202012Validator

    schema = load_schema()

    fixture_path = Path(
        "tests/fixtures/valid_babt_certificate.json"
    )

    fixture = json.loads(fixture_path.read_text())

    Draft202012Validator(schema).validate(fixture)


def test_invalid_issuance_timestamp_is_rejected():
    from jsonschema import Draft202012Validator

    schema = load_schema()
    fixture_path = Path("tests/fixtures/valid_babt_certificate.json")
    fixture = json.loads(fixture_path.read_text())
    fixture["issuance"]["timestamp"] = "2026-08-12"

    validator = Draft202012Validator(schema)
    errors = list(validator.iter_errors(fixture))

    assert errors, "Invalid issuance timestamp was accepted"
