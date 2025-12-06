# app/agents/events_agent.py
from typing import Dict, Any, List


def propose_events(world: Dict[str, Any], max_events: int = 5) -> List[Dict[str, Any]]:
    events: List[Dict[str, Any]] = []

    factions = world.get("factions", [])
    regions = world.get("continent", {}).get("regions", [])

    for faction in factions:
        for region in regions:
            for city in region.get("cities", []):
                if city.get("faction_control") == faction["faction_id"]:
                    events.append(
                        {
                            "type": "economic_boost",
                            "description": f"{faction['name']} boosts economy in {city['name']}",
                            "target_city_id": city["city_id"],
                            "effects": {
                                "resources": {
                                    "food": 50
                                }
                            },
                        }
                    )

    return events[:max_events]
def evaluate_events(
    proposed_events: List[Dict[str, Any]], world: Dict[str, Any]
) -> Dict[str, Any]:
    approved_events = []
    rejected_events = []

    for event in proposed_events:
        if event["type"] == "economic_boost":
            approved_events.append(event)
        else:
            rejected_events.append(event)

    world_version = world.get("version", 1) + 1

    return {
        "approved_events": approved_events,
        "rejected_events": rejected_events,
        "world_version": world_version,
    }       