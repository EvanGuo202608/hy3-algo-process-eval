#!/usr/bin/env python3
"""Lightweight validation for benchmarks/problem_catalog.yaml.

The MVP intentionally avoids third-party YAML dependencies. This script checks
the structural facts that matter for stage 1 acceptance.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from typing import Dict


REQUIRED_MVP = {
    "A01-pack-cost",
    "A02-interval-removal",
    "B01-pairing",
    "B02-cut-height",
    "C01-rising-points",
    "C02-minimum-network",
    "D01-range-affine-sum",
    "D02-route-upgrade",
}


def validate_catalog(path: Path) -> Dict[str, object]:
    text = path.read_text(encoding="utf-8")
    candidates = re.findall(r"candidate_id:\s*C\d+", text)
    mvp_items = re.findall(r"selection:\s*mvp", text)
    formal_items = re.findall(r"selection:\s*formal_extension", text)
    internal_ids = set(re.findall(r"internal_id:\s*([A-Z0-9][A-Za-z0-9-]+)", text))
    missing_mvp = sorted(REQUIRED_MVP - internal_ids)

    errors = []
    if len(candidates) < 16:
        errors.append("candidate count must be at least 16")
    if len(mvp_items) != 8:
        errors.append("there must be exactly 8 MVP selections")
    if len(formal_items) < 4:
        errors.append("there must be at least 4 formal extension selections")
    if missing_mvp:
        errors.append(f"missing MVP internal ids: {', '.join(missing_mvp)}")

    result = {
        "ok": not errors,
        "candidate_count": len(candidates),
        "mvp_count": len(mvp_items),
        "formal_extension_count": len(formal_items),
        "errors": errors,
    }
    if errors:
        raise SystemExit(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("benchmarks/problem_catalog.yaml")
    print(json.dumps(validate_catalog(path), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

