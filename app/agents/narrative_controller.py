from typing import Dict, Any, List, Tuple


def validate_events(
    world: Dict[str, Any], events: List[Dict[str, Any]]
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    approved: List[Dict[str, Any]] = []
    rejected: List[Dict[str, Any]] = []

    factions_ids = {f["faction_id"] for f in world.get("factions", [])}
    city_ids = set()

    for region in world.get("continent", {}).get("regions", []):
        for city in region.get("cities", []):
            city_ids.add(city["city_id"])

    for ev in events:
        reason = None

        if ev.get("type") == "war_declaration":
            attacker = ev.get("attacker_id")
            defender = ev.get("defender_id")
            if attacker not in factions_ids or defender not in factions_ids:
                reason = "Unknown attacker or defender faction."

        if ev.get("type") == "economic_boost":
            target_city_id = ev.get("target_city_id")
            if target_city_id not in city_ids:
                reason = "Target city does not exist."

        if reason:
            ev_with_reason = dict(ev)
            ev_with_reason["rejected_reason"] = reason
            rejected.append(ev_with_reason)
        else:
            approved.append(ev)

    return approved, rejected
# i need to add more event types and apply 