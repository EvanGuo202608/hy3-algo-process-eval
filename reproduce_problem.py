#!/usr/bin/env python3
"""Reproduce the local fixture evaluation for one problem."""

from __future__ import annotations

from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from algotrace_hy3.evaluator.sandbox import collect_test_cases, compile_and_run_cpp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", default="A01-pack-cost")
    args = parser.parse_args()

    problem_dir = ROOT / "benchmarks" / "problems" / args.problem
    code = (problem_dir / "reference_solution.cpp").read_text(encoding="utf-8")
    cases = collect_test_cases(problem_dir)
    result = compile_and_run_cpp(code, cases)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["verdict"] == "AC" else 1


if __name__ == "__main__":
    raise SystemExit(main())

