"""Hy3 adapter boundary.

The current MVP can run without a Hy3 key by loading fixed fixture traces.
Real API calls are intentionally kept behind environment variables.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from .config import Hy3Config, load_hy3_config
from .schemas import load_solution_json


class Hy3Client:
    def __init__(self, config: Hy3Config | None = None) -> None:
        self.config = config or load_hy3_config()

    def generate_solution(self, prompt: str) -> Dict[str, Any]:
        if not self.config.is_configured:
            raise RuntimeError(
                "HY3_API_KEY is not configured. Use fixture mode for offline tests."
            )
        raise NotImplementedError(
            "Online Hy3 calls will be enabled after the offline vertical slice is stable."
        )


def load_fixture_solution(path: Path) -> Dict[str, Any]:
    return load_solution_json(path)

