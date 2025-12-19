from pathlib import Path
import json
from forecast_lib.logging_utils import get_logger

logger = get_logger(__name__)

def evaluate(run_id: str, output_dir: str = "artifacts", force: bool = False) -> None:
    run_dir = Path(output_dir) / run_id
    model_path = run_dir / "model.json"

    if not model_path.exists():
        raise FileNotFoundError(f"Missing model: {model_path}. Run train first.")

    eval_dir = run_dir / "eval"
    eval_dir.mkdir(parents=True, exist_ok=True)

    done_path = eval_dir / "DONE"
    metrics_path = eval_dir / "metrics.json"

    if done_path.exists() and not force:
        logger.info("Eval for %s already complete (%s exists). Skipping.", run_id, done_path)
        return

    logger.info("Evaluating run_id=%s", run_id)

    if "FAIL" in run_id:
        raise ValueError("Intentional failure for testing failure semantics")

    model = json.loads(model_path.read_text())

    # Simulated metric (deterministic so reruns match)
    metrics = {
        "run_id": run_id,
        "metric_name": "mae",
        "metric_value": round(abs(model["coef"] - 0.5) + abs(model["intercept"] - 1.0), 4),
    }
    
    # Simulated quality gate
    if metrics["metric_value"] > 0.5:
        raise ValueError(
            f"Model quality too poor (mae={metrics['metric_value']})"
        )


    metrics_path.write_text(json.dumps(metrics, indent=2))
    done_path.write_text("ok\n")

    logger.info("Saved metrics to %s", metrics_path)
    logger.info("Wrote DONE marker to %s", done_path)

