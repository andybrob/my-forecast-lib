from forecast_lib.logging_utils import get_logger

logger = get_logger(__name__)

def add(a, b):
    logger.info("Adding %s and %s", a, b)
    return a + b
