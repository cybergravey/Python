# protocol_exile/core/save_loader.py

import json
import os

SAVE_PATH = os.path.join("save_data", "save.json")

def save_game(galaxy, ship):
    data = {
        "ship": {
            "morale": ship.morale,
            "fuel": ship.fuel,
            "power": ship.power,
            "trace": ship.trace
        },
        "stars": [
            {
                "name": s.name,
                "x": s.x,
                "y": s.y,
                "visited": s.visited,
                "dangerous": s.dangerous,
                "event_triggered": s.event_triggered,
                "event_result": s.event_result
            }
            for s in galaxy.stars
        ]
    }
    with open(SAVE_PATH, "w") as f:
        json.dump(data, f, indent=2)

def load_game():
    if not os.path.exists(SAVE_PATH):
        return None, None

    with open(SAVE_PATH, "r") as f:
        content = f.read().strip()
        if not content:
            return None, None

        data = json.loads(content)
        if "ship" not in data or "stars" not in data:
            return None, None

        return data["ship"], data["stars"]