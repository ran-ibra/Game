# app/agents/content_builder.py
import uuid
from typing import Dict, Any


def build_initial_content(world: Dict[str, Any]) -> Dict[str, Any]:
    factions = [
        {
            "faction_id": "faction_1",
            "name": "Kingdom of Asteron",
            "alignment": "lawful",
            "strength": 75,
            "diplomacy": {},  
            "military_units": [
                {
                    "unit_id": str(uuid.uuid4()),
                    "type": "swordsman",
                    "attack": 10,
                    "defense": 8,
                    "cost": {"food": 2, "iron": 1},
                },
                {
                    "unit_id": str(uuid.uuid4()),
                    "type": "archer",
                    "attack": 8,
                    "defense": 4,
                    "cost": {"food": 2, "wood": 1},
                },
            ],
            "buildings": [
                {
                    "building_id": str(uuid.uuid4()),
                    "name": "Barracks",
                    "level": 1,
                    "cost": {"wood": 50, "stone": 30},
                },
                {
                    "building_id": str(uuid.uuid4()),
                    "name": "Town Hall",
                    "level": 1,
                    "cost": {"wood": 100, "stone": 80},
                },
            ],
        }
    ]

    regions = world.get("continent", {}).get("regions", [])
    if regions:
        first_region = regions[0]
        starter_city = {
            "city_id": str(uuid.uuid4()),
            "name": "Frosthelm",
            "population": 12000,
            "resources": {"iron": 200, "food": 150, "wood": 50},
            "faction_control": "faction_1",
        }
        first_region["cities"].append(starter_city)

    world["factions"] = factions
    return world
