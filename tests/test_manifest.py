from pathlib import Path
import json
from forecast_lib.run_manifest import write_run_manifest

def test_run_manifest_written(tmp_path: Path) -> None:
    run_dir = tmp_path / "r1"
    run_dir.mkdir()

    write_run_manifest(run_dir, status="success", steps=["train", "eval"])

    path = run_dir / "run.json"
    data = json.loads(path.read_text())

    assert data["run_id"] == "r1"
    assert data["status"] == "success"
    assert data["steps"] == ["train", "eval"]
    assert "timestamp_utc" in data

