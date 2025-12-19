import time
from typing import Callable, TypeVar
from forecast_lib.logging_utils import get_logger

logger = get_logger(__name__)
T = TypeVar("T")

def retry(fn: Callable[[], T], *, retries: int = 2, base_delay_s: float = 0.2) -> T:
    """
    Run fn with retries and exponential backoff.
    retries=2 -> up to 3 attempts total.
    """
    attempt = 0
    while True:
        try:
            return fn()
        except Exception as e:
            if attempt >= retries:
                logger.error("Retries exhausted. Last error: %s", e)
                raise
            delay = base_delay_s * (2 ** attempt)
            logger.warning("Attempt %d failed: %s. Retrying in %.2fs", attempt + 1, e, delay)
            time.sleep(delay)
            attempt += 1

