"""Runtime configuration helpers."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Hy3Config:
    base_url: str
    api_key: str
    model: str
    timeout: float
    temperature: float
    max_retries: int

    @property
    def is_configured(self) -> bool:
        return bool(self.api_key and self.api_key != "replace-with-local-secret")


def load_hy3_config() -> Hy3Config:
    return Hy3Config(
        base_url=os.getenv("HY3_BASE_URL", "http://127.0.0.1:8000/v1"),
        api_key=os.getenv("HY3_API_KEY", ""),
        model=os.getenv("HY3_MODEL", "hy3"),
        timeout=float(os.getenv("HY3_TIMEOUT", "120")),
        temperature=float(os.getenv("HY3_TEMPERATURE", "0.1")),
        max_retries=int(os.getenv("HY3_MAX_RETRIES", "2")),
    )

