import os
from dataclasses import dataclass

def _get_env(name: str, default: str) -> str:
    return os.environ.get(name, default)

def _get_int(name: str, default: int) -> int:
    return int(os.environ.get(name, default))

def _get_float(name: str, default: float) -> float:
    return float(os.environ.get(name, default))

def _get_log_level(name: str, default: str) -> str:
    val = os.environ.get(name, default).upper()
    allowed = {"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"}
    return val if val in allowed else default


@dataclass(frozen=True)
class Config:
    output_dir: str = _get_env("FORECAST_OUTPUT_DIR", "artifacts")
    retries_train: int = _get_int("FORECAST_RETRIES_TRAIN", 2)
    retries_evaluate: int = _get_int("FORECAST_RETRIES_EVAL", 2)
    retries_promote: int = _get_int("FORECAST_RETRIES_PROMOTE", 1)
    base_delay_s: float = _get_float("FORECAST_BASE_DELAY_S", 0.2)
    log_level: str = _get_log_level("FORECAST_LOG_LEVEL", "INFO")

