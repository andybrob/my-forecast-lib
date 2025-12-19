from pathlib import Path
from datetime import datetime
import json
from typing import Dict, List

def write_run_manifest(
    run_dir: Path,
    status: str,
    steps: List[str],
    step_status: Dict[str, str],
) -> None:
    manifest = {
        "run_id": run_dir.name,
        "status": status,
        "steps": steps,
        "step_status": step_status,
        "timestamp_utc": datetime.utcnow().isoformat(),
    }

    path = run_dir / "run.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n")

