import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from cli import draft_from_record, load_ledger


def test_draft_is_deterministic(tmp_path):
    rec = {
        "merkle_leaf": "abcdef0123456789deadbeef",
        "running_merkle_root": "root-1",
        "entity_id": "CAISO-TEST",
        "interval": "2026-08-01T00:00:00Z/PT5M",
        "computation": {
            "gate_state": "PASS",
            "policy_citations": ["SB253"],
        },
    }
    a = draft_from_record(rec, "email")
    b = draft_from_record(rec, "email")
    assert a == b
    assert a["gate_state"] == "PASS"
    assert a["receipt_id"] == "abcdef0123456789"


def test_load_ledger_jsonl(tmp_path):
    p = tmp_path / "ledger.jsonl"
    p.write_text(json.dumps({"entity_id": "E1", "computation": {}}) + "\n", encoding="utf-8")
    rows = load_ledger(p)
    assert len(rows) == 1
    assert rows[0]["entity_id"] == "E1"
