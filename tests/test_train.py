from pathlib import Path
from forecast_lib.train import train

def test_train_creates_done_marker(tmp_path: Path) -> None:
    run_id = "t1"
    out_dir = tmp_path / "artifacts"

    train(run_id=run_id, output_dir=str(out_dir))
    done = out_dir / run_id / "DONE"
    model = out_dir / run_id / "model.json"

    assert done.exists()
    assert model.exists()

def test_train_skips_when_done_exists(tmp_path: Path) -> None:
    run_id = "t2"
    out_dir = tmp_path / "artifacts"

    train(run_id=run_id, output_dir=str(out_dir))
    model = out_dir / run_id / "model.json"

    first = model.read_text()
    train(run_id=run_id, output_dir=str(out_dir))  # should skip
    second = model.read_text()

    assert first == second

