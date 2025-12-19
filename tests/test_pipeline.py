from pathlib import Path
from forecast_lib.train import train
from forecast_lib.evaluate import evaluate
from forecast_lib.promote import promote

def test_full_pipeline_creates_production(tmp_path: Path) -> None:
    out = tmp_path / "artifacts"
    run_id = "r1"

    train(run_id, output_dir=str(out))
    evaluate(run_id, output_dir=str(out))
    promote(run_id, output_dir=str(out))

    prod = out / "production"
    assert (prod / "model.json").exists()
    assert (prod / "metrics.json").exists()
    assert (prod / "DONE").exists()

