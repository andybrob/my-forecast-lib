import os
from dataclasses import dataclass
from typing import Optional

def _get_env(name: str, default: Optional[str] = None) -> str:
    value = os.getenv(name, default)
    if value is None:
        raise RuntimeError(f"Missing required env var: {name}")
    return value

@dataclass(frozen=True)
class Config:
    log_level: str = _get_env("FORECAST_LOG_LEVEL", "INFO")
    environment: str = _get_env("FORECAST_ENV", "dev")


