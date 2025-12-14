import json
from datetime import datetime
from pathlib import Path

HEALING_FILE = Path("utils/healed_locators.json")

def save_healing(page, element, primary, fallback, confidence):
    record = {
        "page": page,
        "element": element,
        "primary": str(primary),
        "healed_with": str(fallback),
        "confidence": confidence,
        "timestamp": datetime.now().isoformat()
    }

    data = []
    if HEALING_FILE.exists():
        data = json.loads(HEALING_FILE.read_text())

    data.append(record)
    HEALING_FILE.write_text(json.dumps(data, indent=2))
