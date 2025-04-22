import json
import os

def load_events():
    path = os.path.join("assets", "events", "events.json")
    with open(path, "r") as f:
        return json.load(f)
    
def load_fragments():
    path = os.path.join("assets", "memories", "fragments.json")
    with open(path, "r") as f:
        return json.load(f)