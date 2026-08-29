import json
import subprocess
import sys
from pathlib import Path

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

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "04_EVIDENCE_PACKAGE" / "RSB-0001" / "RSB-0001.md"
PYTHON_RUNNER = ROOT / "scripts" / "rsb_0001" / "python_runtime_a.py"
NODE_RUNNER = ROOT / "scripts" / "rsb_0001" / "node_runtime_b.js"


def run(command):
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def main():
    for runner in (PYTHON_RUNNER, NODE_RUNNER):
        source = runner.read_text(encoding="utf-8")
        assert "expected_answer" not in source
        assert "expected answers" not in source.lower()

    python_result = run([sys.executable, str(PYTHON_RUNNER), str(TARGET)])
    node_result = run(["node", str(NODE_RUNNER), str(TARGET)])

    assert python_result["normative_answer_data_loaded"] is False
    assert node_result["normative_answer_data_loaded"] is False
    assert python_result["queries"] == node_result["queries"]
    assert python_result["queries"] == EXPECTED

    print("RSB-0001 independent reproduction verification: PASS")
    print("python runtime: PASS")
    print("node runtime: PASS")
    print("cross-runtime equality: PASS")
    print("Q01-Q10 expected-answer comparison: PASS")


if __name__ == "__main__":
    main()
