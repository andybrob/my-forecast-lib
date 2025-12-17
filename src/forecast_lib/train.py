from pathlib import Path
import json
from forecast_lib.logging_utils import get_logger

logger = get_logger(__name__)

def train(run_id: str, output_dir: str = "artifacts", force: bool = False) -> None:
    """
    Simulated training job.
    Contract:

     - Writes outputs under artifacts/<run_id>/
     - Creates DONE marker when successful
     - If DONE exists and force=False, it does nothing (safe retry)
    """
    run_dir = Path(output_dir) / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    done_path = run_dir / "DONE"
    model_path = run_dir / "model.json"

    if done_path.exists() and not force:
        logger.info("Run %s already complete (%s exists). Skipping.", run_id, done_path)
        return

    logger.info("Starting training run_id=%s output_dir=%s", run_id, run_dir)

    model = {
        "run_id": run_id,
        "coef": 0.42,
        "intercept": 1.23,
    }

    # Idempotent write (overwrite is safe)
    model_path.write_text(json.dumps(model, indent=2))
    done_path.write_text("ok\n")

    logger.info("Saved model to %s", model_path)
    logger.info("Wrote DONE marker to %s", done_path)
