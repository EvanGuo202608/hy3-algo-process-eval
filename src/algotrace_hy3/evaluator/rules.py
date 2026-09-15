"""Deterministic process checks for the MVP."""

from __future__ import annotations

from typing import Any, Dict, List

from algotrace_hy3.schemas import SchemaError, iter_step_text, validate_solution


def evaluate_process_rules(solution: Dict[str, Any]) -> Dict[str, Any]:
    try:
        validate_solution(solution)
    except SchemaError as exc:
        return {
            "process_correct": False,
            "first_error_step": None,
            "primary_error_type": "E8",
            "secondary_error_types": [],
            "severity": "high",
            "confidence": 0.95,
            "evidence": f"Schema invalid: {exc}",
            "warnings": [],
        }

    warnings: List[str] = []
    if len(solution.get("boundary_cases", [])) < 2:
        warnings.append("boundary case list is short")
    if "O(" not in solution.get("time_complexity", ""):
        warnings.append("time complexity is not written in standard O(...) style")

    if solution.get("problem_id") == "A01-pack-cost":
        bad_markers = ["向下取整", "floor", "n /", "整数除法得到包数"]
        for step_id, text in iter_step_text(solution):
            lowered = text.lower()
            if any(marker.lower() in lowered for marker in bad_markers):
                return {
                    "process_correct": False,
                    "first_error_step": step_id,
                    "primary_error_type": "E5",
                    "secondary_error_types": ["E3"],
                    "severity": "high",
                    "confidence": 0.9,
                    "evidence": (
                        "A01 requires ceiling division for package counts. "
                        "Using floor division or integer division as the reasoning "
                        "basis can buy too few pencils when n is not divisible."
                    ),
                    "warnings": warnings,
                }

    if solution.get("problem_id") == "A02-interval-removal":
        bad_markers = [
            "不包含端点",
            "开区间",
            "open interval",
            "does not include endpoints",
            "exclusive",
            "right - left",
            "r - l",
        ]
        for step_id, text in iter_step_text(solution):
            lowered = text.lower()
            if any(marker.lower() in lowered for marker in bad_markers):
                return {
                    "process_correct": False,
                    "first_error_step": step_id,
                    "primary_error_type": "E5",
                    "secondary_error_types": ["E1"],
                    "severity": "high",
                    "confidence": 0.88,
                    "evidence": (
                        "A02 intervals are inclusive on integer positions. Treating "
                        "endpoints as excluded can leave removed boundary positions "
                        "incorrectly counted."
                    ),
                    "warnings": warnings,
                }

    if solution.get("problem_id") == "B01-pairing":
        bad_markers = [
            "pair the lightest people first",
            "two lightest",
            "最轻的两",
            "先配最轻",
            "unit price",
            "平均",
            "always pair everyone",
            "一定两两配对",
        ]
        for step_id, text in iter_step_text(solution):
            lowered = text.lower()
            if any(marker.lower() in lowered for marker in bad_markers):
                return {
                    "process_correct": False,
                    "first_error_step": step_id,
                    "primary_error_type": "E3",
                    "secondary_error_types": ["E2"],
                    "severity": "high",
                    "confidence": 0.87,
                    "evidence": (
                        "B01 needs the standard two-pointer greedy argument: handle "
                        "the heaviest remaining person first, pairing with the lightest "
                        "only if their sum fits. Pairing lightest people first or claiming "
                        "everyone can always be paired does not justify optimality."
                    ),
                    "warnings": warnings,
                }

    return {
        "process_correct": True,
        "first_error_step": None,
        "primary_error_type": None,
        "secondary_error_types": [],
        "severity": "none",
        "confidence": 0.78 if warnings else 0.86,
        "evidence": "No deterministic process error was found by MVP rules.",
        "warnings": warnings,
    }
