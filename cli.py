"""Command line interface for the offline MVP."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import List

from . import __version__
from .evaluator.aggregate import aggregate_result
from .evaluator.rules import evaluate_process_rules
from .evaluator.sandbox import collect_test_cases, compile_and_run_cpp
from .hy3_client import load_fixture_solution
from .schemas import load_solution_json


REPO_ROOT = Path(__file__).resolve().parents[2]


def _print_json(data: object) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def run_demo(args: argparse.Namespace) -> int:
    fixture_path = Path(args.fixture)
    if not fixture_path.is_absolute():
        fixture_path = REPO_ROOT / fixture_path
    solution = load_fixture_solution(fixture_path)

    problem_dir = REPO_ROOT / "benchmarks" / "problems" / args.problem
    cases = collect_test_cases(problem_dir)
    program_result = compile_and_run_cpp(
        solution["code"], cases, timeout_seconds=args.timeout
    )
    process_result = evaluate_process_rules(solution)
    _print_json(aggregate_result(solution, program_result, process_result))
    return 0


def validate_solution_cmd(args: argparse.Namespace) -> int:
    data = load_solution_json(Path(args.path))
    _print_json({"ok": True, "problem_id": data["problem_id"], "steps": len(data["steps"])})
    return 0


def validate_catalog_cmd(args: argparse.Namespace) -> int:
    script_path = REPO_ROOT / "scripts" / "validate_problem_catalog.py"
    namespace = {"__name__": "__algotrace_validation__", "__file__": str(script_path)}
    exec(script_path.read_text(encoding="utf-8"), namespace)
    result = namespace["validate_catalog"](Path(args.path))
    _print_json(result)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="algotrace-hy3")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)

    demo = subparsers.add_parser("demo", help="run the offline A01 vertical slice")
    demo.add_argument("--problem", default="A01-pack-cost")
    demo.add_argument(
        "--fixture",
        default="fixtures/a01_pack_cost/wrong_process_right_code.json",
    )
    demo.add_argument("--timeout", type=float, default=2.0)
    demo.set_defaults(func=run_demo)

    validate_solution = subparsers.add_parser("validate-solution")
    validate_solution.add_argument("path")
    validate_solution.set_defaults(func=validate_solution_cmd)

    validate_catalog = subparsers.add_parser("validate-catalog")
    validate_catalog.add_argument("--path", default="benchmarks/problem_catalog.yaml")
    validate_catalog.set_defaults(func=validate_catalog_cmd)
    return parser


def main(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())

