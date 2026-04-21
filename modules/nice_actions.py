from modules.utils import format_percent

NICE_ACTIONS_KEY_MAP = {
    "time_format": "Time Format For HUD",
    "rtp_height_min": "Min Y Height For RTP",
    "rtp_height_max": "Max Y Height For RTP",
    "rtp_radius": "RTP Radius (in Blocks)",
    "rtp_type": "RTP Type",
    "player": "Player Position As Origin",
    "events": "Events",
    "fishing": "Fishing",
    "consuming": "Consuming",
    "breeding": "Breeding",
    "misc": "Active Weekdays",
    "killing": "Killing",
    "brewing": "Brewing",
}

COST_KEYS = {
    "horse_info_cost","death_coords_cost","transfer_enchantments_cost",
    "send_coords_cost","rtp_cost","sit_cost","tp_home_cost",
    "set_home_cost","tp_spawn_cost","equip_hat_cost",
    "share_stats_cost","villager_info_cost",
}

COOLDOWN_KEYS = {
    "tp_spawn_cooldown","rtp_cooldown","tp_home_cooldown",
}


def remap_nice_actions(obj):
    if not isinstance(obj, dict):
        return obj

    result = {}
    costs = {}
    cooldowns = {}

    for k, v in obj.items():
        if k in COST_KEYS:
            costs[k] = format_percent(v)
            continue
        if k in COOLDOWN_KEYS:
            cooldowns[k] = format_percent(v)
            continue

        mapped = NICE_ACTIONS_KEY_MAP.get(k, k)
        result[mapped] = v

    if costs:
        result["Action Costs"] = costs
    if cooldowns:
        result["Action Cooldowns (Seconds)"] = cooldowns

    return result