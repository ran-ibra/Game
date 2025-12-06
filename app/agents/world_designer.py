# app/agents/world_designer.py
import uuid
from typing import Dict, Any


def generate_base_world() -> Dict[str, Any]:
    world_id = str(uuid.uuid4())

    regions = [
        {
            "region_id": str(uuid.uuid4()),
            "name": "Northern Reach",
            "biome": "tundra",
            "cities": [],
            "natural_resources": {"iron": 500, "wood": 200, "mana_crystals": 50},
        },
        {
            "region_id": str(uuid.uuid4()),
            "name": "Emerald Plains",
            "biome": "grassland",
            "cities": [],
            "natural_resources": {"food": 800, "wood": 400, "stone": 200},
        },
    ]

    world = {
        "world_id": world_id,
        "continent": {
            "name": "Arthia",
            "climate": "mixed",
            "regions": regions,
        },
        "factions": [],
        "events_log": [],
        "version": 1,
    }

    return world
# Example usage
if __name__ == "__main__":
    base_world = generate_base_world()
    print(base_world)