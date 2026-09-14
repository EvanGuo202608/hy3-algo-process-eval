"""Aggregate program execution and process checks."""

from __future__ import annotations

from typing import Any, Dict


def aggregate_result(
    solution: Dict[str, Any],
    program_result: Dict[str, Any],
    process_result: Dict[str, Any],
) -> Dict[str, Any]:
    final_correct = program_result.get("verdict") == "AC"
    process_correct = bool(process_result.get("process_correct"))
    return {
        "problem_id": solution.get("problem_id"),
        "final_correct": final_correct,
        "program_verdict": program_result.get("verdict"),
        "passed": program_result.get("passed"),
        "total": program_result.get("total"),
        "process_correct": process_correct,
        "first_error_step": process_result.get("first_error_step"),
        "primary_error_type": process_result.get("primary_error_type"),
        "secondary_error_types": process_result.get("secondary_error_types", []),
        "severity": process_result.get("severity"),
        "confidence": process_result.get("confidence"),
        "evidence": process_result.get("evidence"),
        "warnings": process_result.get("warnings", []),
        "correct_answer_wrong_process": final_correct and not process_correct,
    }

