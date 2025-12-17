from pathlib import Path
import json
from forecast_lib.logging_utils import get_logger

logger = get_logger(__name__)

def train(run_id: str, output_dir: str = "artifacts") -> None:
    """
    Simulated training job.
    Safe to rerun (idempotent).
    """
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    model_path = out / f"model_{run_id}.json"

    logger.info("Starting training run_id=%s", run_id)

    model = {
        "run_id": run_id,
        "coef": 0.42,
        "intercept": 1.23,
    }

    # Idempotent write (overwrite is safe)
    model_path.write_text(json.dumps(model, indent=2))

    logger.info("Saved model to %s", model_path)

