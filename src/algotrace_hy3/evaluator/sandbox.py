"""Small local C++17 runner for trusted project fixtures.

This is not a full security sandbox. The README warns users not to execute
unknown code until the restricted runner is implemented.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess
import tempfile
from typing import Dict, List


@dataclass(frozen=True)
class TestCase:
    name: str
    input_text: str
    expected_output: str


def collect_test_cases(problem_dir: Path) -> List[TestCase]:
    tests_dir = problem_dir / "tests"
    cases: List[TestCase] = []
    for input_path in sorted(tests_dir.rglob("*.in")):
        output_path = input_path.with_suffix(".out")
        if not output_path.exists():
            raise FileNotFoundError(f"missing output for {input_path}")
        cases.append(
            TestCase(
                name=str(input_path.relative_to(tests_dir)),
                input_text=input_path.read_text(encoding="utf-8"),
                expected_output=output_path.read_text(encoding="utf-8"),
            )
        )
    if not cases:
        raise FileNotFoundError(f"no .in tests found under {tests_dir}")
    return cases


def _normalize_output(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def compile_and_run_cpp(
    code: str, test_cases: List[TestCase], timeout_seconds: float = 2.0
) -> Dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="algotrace_cpp_") as tmp:
        tmp_path = Path(tmp)
        source = tmp_path / "main.cpp"
        binary = tmp_path / "main"
        source.write_text(code, encoding="utf-8")

        compile_result = subprocess.run(
            ["g++", "-std=c++17", "-O2", str(source), "-o", str(binary)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20,
        )
        if compile_result.returncode != 0:
            return {
                "verdict": "CE",
                "passed": 0,
                "total": len(test_cases),
                "cases": [],
                "stderr": compile_result.stderr,
            }

        case_results = []
        for case in test_cases:
            try:
                run_result = subprocess.run(
                    [str(binary)],
                    input=case.input_text,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=timeout_seconds,
                )
            except subprocess.TimeoutExpired:
                case_results.append({"name": case.name, "verdict": "TLE"})
                continue

            if run_result.returncode != 0:
                case_results.append(
                    {
                        "name": case.name,
                        "verdict": "RE",
                        "stderr": run_result.stderr,
                    }
                )
                continue

            actual = _normalize_output(run_result.stdout)
            expected = _normalize_output(case.expected_output)
            verdict = "AC" if actual == expected else "WA"
            case_results.append(
                {
                    "name": case.name,
                    "verdict": verdict,
                    "actual": actual,
                    "expected": expected,
                }
            )

        passed = sum(1 for item in case_results if item["verdict"] == "AC")
        verdict = "AC" if passed == len(test_cases) else "WA"
        if any(item["verdict"] == "TLE" for item in case_results):
            verdict = "TLE"
        if any(item["verdict"] == "RE" for item in case_results):
            verdict = "RE"
        return {
            "verdict": verdict,
            "passed": passed,
            "total": len(test_cases),
            "cases": case_results,
        }

