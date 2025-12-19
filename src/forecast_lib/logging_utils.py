from forecast_lib.config import Config

import logging

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    config = Config()
    level = getattr(config, "log_level", "INFO")
    logger.setLevel(level)

    # Ensure we have a StreamHandler configured for INFO
    has_stream = False
    for h in logger.handlers:
        if isinstance(h, logging.StreamHandler):
            has_stream = True
            h.setLevel(config.log_level)
            h.setFormatter(logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            ))

    if not has_stream:
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        handler.setFormatter(logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        ))
        logger.addHandler(handler)

    # Avoid double-logging through the root logger
    logger.propagate = False
    return logger


