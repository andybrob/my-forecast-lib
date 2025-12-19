from pathlib import Path

def done_path(output_dir: str, run_id: str, step: str) -> Path:
    base = Path(output_dir) / run_id
    if step == "train":
        return base / "DONE"
    if step == "evaluate":
        return base / "eval" / "DONE"
    if step == "promote":
        return Path(output_dir) / "production" / "DONE"
    raise ValueError(f"Unknown step: {step}")

