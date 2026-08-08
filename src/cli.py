#!/usr/bin/env python3
"""
Minimal CLI for Unignorable: consume a Q-Reg / VERA ledger.jsonl and emit
structured outreach drafts. Pure functions only; no network in critical path.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List


def load_ledger(path: Path) -> List[Dict[str, Any]]:
    records = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def draft_from_record(rec: Dict[str, Any], outreach_type: str = "email") -> Dict[str, Any]:
    """Deterministic mapping from sealed record to outreach skeleton."""
    computation = rec.get("computation", {})
    return {
        "receipt_id": rec.get("merkle_leaf", "")[:16],
        "merkle_root": rec.get("running_merkle_root"),
        "gate_state": computation.get("gate_state"),
        "entity_id": rec.get("entity_id"),
        "interval": rec.get("interval"),
        "policy_citations": computation.get("policy_citations", []),
        "outreach_type": outreach_type,
        "target_role": "compliance / sustainability lead",
        "claim_summary": f"Deterministic {computation.get('gate_state')} gate for {rec.get('entity_id')} under SB 253 / Title 17 CCR",
        "proof_link": None,  # filled by caller with public receipt URL
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Unignorable receipt-to-outreach CLI")
    parser.add_argument("ledger", type=Path, help="Path to ledger.jsonl from Q-Reg")
    parser.add_argument("--type", default="email", choices=["email", "linkedin", "proposal", "thread"])
    parser.add_argument("--out", type=Path, default=None, help="Optional output JSONL")
    args = parser.parse_args()

    if not args.ledger.exists():
        print(f"Ledger not found: {args.ledger}", file=sys.stderr)
        return 1

    records = load_ledger(args.ledger)
    drafts = [draft_from_record(r, args.type) for r in records]

    for d in drafts:
        print(json.dumps(d, ensure_ascii=True))

    if args.out:
        with args.out.open("w", encoding="utf-8") as f:
            for d in drafts:
                f.write(json.dumps(d, ensure_ascii=True) + "\n")
        print(f"Wrote {len(drafts)} drafts to {args.out}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
