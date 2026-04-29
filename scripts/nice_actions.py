from scripts.utils import format_percent

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
    "chance": "Chance For This Type Of Event",
    "loot_table": "Loot Table",
    "max_amount": "Max Amount Of Actions Needed For Completion",
    "horse_info_cost": "Horse Info",
    "death_coords_cost": "Death/Grave Coordinates",
    "transfer_enchantments_cost": "Transfer Enchantments",
    "send_coords_cost": "Broadcast Coordinates",
    "rtp_cost": "RTP",
    "sit_cost": "Sit",
    "tp_home_cost": "TP Home",
    "set_home_cost": "Set Home",
    "tp_spawn_cost": "TP To Spawn",
    "equip_hat_cost": "Equip Item As Hat",
    "share_stats_cost": "Share Stats",
    "villager_info_cost": "Villager Info",
    "tp_spawn_cooldown": "TP To Spawn",
    "rtp_cooldown": "RTP",
    "tp_home_cooldown": "TP Home",
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

REMOVE_KEYS = {
    "spawn_y","spawn_x","spawn_dimension","time_hud_style",
    "type","event_msg","spawn_z",
}

WEEKDAY_KEY_MAP = {
    "monday": "Monday",
    "tuesday": "Tuesday",
    "wednesday": "Wednesday",
    "thursday": "Thursday",
    "friday": "Friday",
    "saturday": "Saturday",
    "sunday": "Sunday",
}


def remap_value(v):
    if isinstance(v, dict):
        out = {}
        for k, val in v.items():
            ks = str(k)
            if ks in REMOVE_KEYS:
                continue

            mapped_key = WEEKDAY_KEY_MAP.get(
                ks.lower(),
                NICE_ACTIONS_KEY_MAP.get(ks, ks)
            )

            out[mapped_key] = remap_value(val)
        return out

    if isinstance(v, list):
        return [remap_value(i) for i in v]

    return format_percent(v)


def remap_nice_actions(obj):
    if not isinstance(obj, dict):
        return obj

    result = {}
    costs = {}
    cooldowns = {}

    for k, v in obj.items():
        if k in REMOVE_KEYS:
            continue

        if k in COST_KEYS:
            mapped = NICE_ACTIONS_KEY_MAP.get(k, k)
            costs[mapped] = remap_value(v)
            continue

        if k in COOLDOWN_KEYS:
            mapped = NICE_ACTIONS_KEY_MAP.get(k, k)
            cooldowns[mapped] = remap_value(v)
            continue

        mapped_key = NICE_ACTIONS_KEY_MAP.get(k, k)

        if mapped_key == "Active Weekdays" and isinstance(v, dict):
            result[mapped_key] = {
                WEEKDAY_KEY_MAP.get(kk.lower(), kk): remap_value(vv)
                for kk, vv in v.items()
                if kk not in REMOVE_KEYS
            }
        else:
            result[mapped_key] = remap_value(v)

    if costs:
        result["Action Costs"] = costs

    if cooldowns:
        result["Action Cooldowns (Seconds)"] = cooldowns

    return result