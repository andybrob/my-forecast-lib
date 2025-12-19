from pathlib import Path
from datetime import datetime
import json

def write_run_manifest(
    run_dir: Path,
    status: str,
    steps: list[str],
) -> None:
    manifest = {
        "run_id": run_dir.name,
        "status": status,
        "steps": steps,
        "timestamp_utc": datetime.utcnow().isoformat(),
    }

    path = run_dir / "run.json"
    path.write_text(json.dumps(manifest, indent=2))

