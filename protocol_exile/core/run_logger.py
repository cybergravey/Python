# protocol_exile/core/run_logger.py

import json
import os
from datetime import datetime

HISTORY_PATH = os.path.join("save_data", "run_history.json")

def log_run(ship, alignment, fragments, ending_title):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "morale": ship.morale,
        "fuel": ship.fuel,
        "power": ship.power,
        "trace": ship.trace,
        "humanity": alignment.humanity,
        "logic": alignment.logic,
        "fragments": [frag['id'] for frag in fragments],
        "ending": ending_title
    }

    if not os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, "w") as f:
            json.dump([log_entry], f, indent=2)
    else:
        with open(HISTORY_PATH, "r+") as f:
            content = f.read().strip()
            data = json.loads(content) if content else []
            data.append(log_entry)
            f.seek(0)
            json.dump(data, f, indent=2)