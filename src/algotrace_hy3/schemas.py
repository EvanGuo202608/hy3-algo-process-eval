"""Validation for public structured solution traces."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List


ALLOWED_STEP_KINDS = {
    "observation",
    "algorithm",
    "proof",
    "complexity",
    "boundary",
    "implementation",
}

REQUIRED_FIELDS = {
    "problem_id",
    "problem_understanding",
    "steps",
    "algorithm",
    "correctness_argument",
    "time_complexity",
    "space_complexity",
    "boundary_cases",
    "code_language",
    "code",
    "final_output_or_verdict",
}


class SchemaError(ValueError):
    """Raised when a structured solution is not evaluable."""


def load_solution_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    validate_solution(data)
    return data


def _require_text(data: Dict[str, Any], field: str) -> None:
    value = data.get(field)
    if not isinstance(value, str) or not value.strip():
        raise SchemaError(f"{field} must be a non-empty string")


def _require_text_list(data: Dict[str, Any], field: str) -> None:
    value = data.get(field)
    if not isinstance(value, list) or not value:
        raise SchemaError(f"{field} must be a non-empty list")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise SchemaError(f"{field} must contain only non-empty strings")


def validate_solution(data: Dict[str, Any]) -> List[str]:
    if not isinstance(data, dict):
        raise SchemaError("solution must be a JSON object")

    missing = sorted(REQUIRED_FIELDS - set(data))
    if missing:
        raise SchemaError(f"missing required fields: {', '.join(missing)}")

    for field in [
        "problem_id",
        "problem_understanding",
        "algorithm",
        "correctness_argument",
        "time_complexity",
        "space_complexity",
        "code",
        "final_output_or_verdict",
    ]:
        _require_text(data, field)

    language = data.get("code_language")
    if not isinstance(language, str) or language.lower() not in {"cpp17", "c++17"}:
        raise SchemaError("code_language must be cpp17")

    _require_text_list(data, "boundary_cases")

    steps = data.get("steps")
    if not isinstance(steps, list) or not steps:
        raise SchemaError("steps must be a non-empty list")

    seen = set()
    for index, step in enumerate(steps, 1):
        if not isinstance(step, dict):
            raise SchemaError(f"step {index} must be an object")
        step_id = step.get("step_id")
        if not isinstance(step_id, int):
            raise SchemaError(f"step {index} has non-integer step_id")
        if step_id in seen:
            raise SchemaError(f"duplicate step_id: {step_id}")
        if step_id != index:
            raise SchemaError("step_id values must be consecutive from 1")
        seen.add(step_id)

        kind = step.get("kind")
        if kind not in ALLOWED_STEP_KINDS:
            raise SchemaError(f"step {step_id} has invalid kind: {kind}")
        for field in ["claim", "justification"]:
            value = step.get(field)
            if not isinstance(value, str) or not value.strip():
                raise SchemaError(f"step {step_id} field {field} must be non-empty")
        depends_on = step.get("depends_on")
        if not isinstance(depends_on, list):
            raise SchemaError(f"step {step_id} depends_on must be a list")
        if any(not isinstance(dep, int) for dep in depends_on):
            raise SchemaError(f"step {step_id} depends_on must contain integers")
        invalid = [dep for dep in depends_on if dep not in seen or dep == step_id]
        if invalid:
            raise SchemaError(f"step {step_id} has invalid dependencies: {invalid}")

    return []


def iter_step_text(data: Dict[str, Any]) -> Iterable[tuple[int, str]]:
    for step in data.get("steps", []):
        yield int(step["step_id"]), f"{step.get('claim', '')}\n{step.get('justification', '')}"

