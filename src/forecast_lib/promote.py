from pathlib import Path
import shutil
from forecast_lib.logging_utils import get_logger

logger = get_logger(__name__)

def promote(run_id: str, output_dir: str = "artifacts", force: bool = False) -> None:
    run_dir = Path(output_dir) / run_id
    model_path = run_dir / "model.json"
    metrics_path = run_dir / "eval" / "metrics.json"

    if not model_path.exists():
        raise FileNotFoundError(f"Missing model: {model_path}. Run train first.")
    if not metrics_path.exists():
        raise FileNotFoundError(f"Missing metrics: {metrics_path}. Run evaluate first.")

    prod_dir = Path(output_dir) / "production"
    prod_dir.mkdir(parents=True, exist_ok=True)

    prod_model = prod_dir / "model.json"
    prod_metrics = prod_dir / "metrics.json"
    done_path = prod_dir / "DONE"

    if done_path.exists() and not force:
        current = done_path.read_text().strip()
        if current == f"ok {run_id}":
            logger.info("Production already set for %s. Skipping.", run_id)
            return

    logger.info("Promoting run_id=%s to %s", run_id, prod_dir)

    shutil.copy2(model_path, prod_model)
    shutil.copy2(metrics_path, prod_metrics)
    done_path.write_text(f"ok {run_id}\n")

    logger.info("Wrote production model to %s", prod_model)
    logger.info("Wrote production metrics to %s", prod_metrics)
    logger.info("Wrote DONE marker to %s", done_path)

