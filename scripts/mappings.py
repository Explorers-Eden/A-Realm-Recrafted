from scripts.utils import format_percent

FR_VALUE_MAP = {
    "enabled": "Enabled",
    "disabled": "Disabled",
    "starter_equip": "Starter Equipment After Race Selection",
    "prefix": "Race Prefix In Front Of Player Name",
    "pvp": "PVP Among Own Race",
    "seeinvis": "See Invisible Players Of Own Race",
    "npc_spawning": "Descendant Spawning",
}

KI_VALUE_MAP = {
    "enabled": "Enabled",
    "disabled": "Disabled",
    "equip_dmg": "Damage Equipment on Death",
    "exp_loss_amount": "Amount Of Exp Level Lost On Death",
    "grave_status": "Graves",
    "grave_duration": "Duration Before Graves Vanish (in Minutes)",
    "player_head_drop_chance": "Chance To Drop Playerhead On Death",
    "equip_dmg_amount": "Amount Of Damage Applied To Equipment On Death",
    "grave_type": "Graves Appearence",
    "player_head_drop": "Players Drop Their Head When Dying",
    "non_droppable_tag_list": "Tag List For Non Droppable Items",
    "exp_loss": "Players Lose Exp Level When Dying",
}

WW_VALUE_MAP = {
    "enabled": "Enabled",
    "disabled": "Disabled",
    "portal_horn": "Portal Horn Settings",
    "breaking_chance": "Chance Of Item Breaking",
    "mob_teleport": "Teleport Pets And Leashed Mobs Alongside Player",
    "active": "Active",
    "exp_cost": "Exp Level Cost",
    "clock": "Clock Settings",
    "compass": "Compass Settings",
    "recovery_compass": "Recovery Compass Settings",
    "waypoint_hub": "Waypoint Hub Settings",
    "min_distance": "Min Distance Between Waypoint Hubs (in Blocks)",
    "player_limit": "Max Waypoint Hubs A Player Can Have Simultaneously",
}


def apply_mapping(obj, mapping):
    if isinstance(obj, dict):
        return {mapping.get(k, k): apply_mapping(v, mapping) for k, v in obj.items()}
    if isinstance(obj, list):
        return [apply_mapping(v, mapping) for v in obj]
    if isinstance(obj, str):
        return mapping.get(obj, obj)
    return format_percent(obj)