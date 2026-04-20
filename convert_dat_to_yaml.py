import os
import re
import yaml
import nbtlib
import paramiko

# ---- SFTP CONFIG (from environment / GitHub Secrets) ----
SFTP_HOST = os.getenv("SFTP_HOST")
SFTP_PORT = int(os.getenv("SFTP_PORT", "22"))
SFTP_USER = os.getenv("SFTP_USER")
SFTP_PASS = os.getenv("SFTP_PASS")  # required for password auth in this variant

# exact remote file paths
SFTP_REMOTE_GAME_RULES = "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/world/data/minecraft/game_rules.dat"
SFTP_REMOTE_COMMAND_STORAGE = "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/world/data/eden/command_storage.dat"
SFTP_REMOTE_COMMAND_STORAGE = "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/world/data/eden/command_storage.dat"
SFTP_REMOTE_GETOFFMYLAWN = "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/config/getoffmylawn.json"


# ---- PATHS ----
INPUT_DIR = "raw_dat"
OUTPUT_DIR = "config"
SETTINGS_DIR = os.path.join(OUTPUT_DIR, "settings")

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SETTINGS_DIR, exist_ok=True)


# -------------------------
# SFTP DOWNLOAD
# -------------------------
def fetch_files_via_sftp():
    if not SFTP_HOST or not SFTP_USER or not SFTP_PASS:
        print("Missing SFTP credentials")
        return

    transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))
    try:
        transport.connect(username=SFTP_USER, password=SFTP_PASS)
        sftp = paramiko.SFTPClient.from_transport(transport)

        files = [
            (SFTP_REMOTE_GAME_RULES, os.path.join(INPUT_DIR, "game_rules.dat")),
            (SFTP_REMOTE_COMMAND_STORAGE, os.path.join(INPUT_DIR, "command_storage.dat")),
            (SFTP_REMOTE_GETOFFMYLAWN, os.path.join(INPUT_DIR, "getoffmylawn.json")),
        ]

        for remote, local in files:
            try:
                sftp.get(remote, local)
                print(f"Downloaded: {remote}")
            except Exception as e:
                print(f"Failed: {remote} -> {e}")

        sftp.close()
    finally:
        transport.close()


# -------------------------
# UTIL
# -------------------------
def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(name))


def write_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)


def map_booleans(obj):
    if isinstance(obj, dict):
        return {k: map_booleans(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [map_booleans(v) for v in obj]
    if isinstance(obj, bool):
        return "Enabled" if obj else "Disabled"
    return obj


# -------------------------
# CLEANER
# -------------------------
def clean(obj):
    if isinstance(obj, dict):
        cleaned = {}
        for k, v in obj.items():
            k_str = str(k)
            if k_str.endswith("_initial"):
                continue
            if k_str in ("command_template", "icon", "bodyicon"):
                continue
            if "command_template" in k_str:
                continue
            cleaned_v = clean(v)
            if isinstance(cleaned_v, str) and "command_template" in cleaned_v:
                continue
            cleaned[k_str] = cleaned_v
        return cleaned
    elif isinstance(obj, list):
        return [clean(v) for v in obj if "command_template" not in str(v)]
    else:
        if isinstance(obj, str) and "command_template" in obj:
            return None
        return obj



# -------------------------
# GAMERULES
# -------------------------
def convert_gamerules():
    file_path = os.path.join(INPUT_DIR, "game_rules.dat")
    if not os.path.exists(file_path):
        print("game_rules.dat not found")
        return

    nbt = nbtlib.load(file_path)
    data = nbt.unpack()

    raw = data.get("data", {})
    gamerules_clean = {}

    if isinstance(raw, dict):
        items = raw.items()
    elif isinstance(raw, list):
        items = []
        for item in raw:
            if isinstance(item, dict):
                items.extend(item.items())
            elif isinstance(item, (list, tuple)) and len(item) == 2:
                items.append(item)
    else:
        items = []

    for rule, value in items:
        rule = str(rule)
        if str(value) in ("1", "true", "True"):
            gamerules_clean[rule] = "Enabled"
        elif str(value) in ("0", "false", "False"):
            gamerules_clean[rule] = "Disabled"
        else:
            gamerules_clean[rule] = value

    write_yaml(os.path.join(OUTPUT_DIR, "gamerules.yml"), gamerules_clean)
    print(f"✔ gamerules.yml written ({len(gamerules_clean)} entries)")


# -------------------------
# COMMAND STORAGE
# -------------------------
def convert_command_storage():
    file_path = os.path.join(INPUT_DIR, "command_storage.dat")
    if not os.path.exists(file_path):
        print("command_storage.dat not found")
        return

    nbt = nbtlib.load(file_path)
    data = nbt.unpack()

    contents = data.get("data", {}).get("contents", {})
    settings = contents.get("settings", {})

    if not isinstance(settings, dict):
        print("settings not found or invalid")
        return

    written = 0

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

    # nice_actions mappings and groupings
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
        # cost and cooldown keys will be remapped below when grouping
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
        "horse_info_cost",
        "death_coords_cost",
        "transfer_enchantments_cost",
        "send_coords_cost",
        "rtp_cost",
        "sit_cost",
        "tp_home_cost",
        "set_home_cost",
        "tp_spawn_cost",
        "equip_hat_cost",
        "share_stats_cost",
        "villager_info_cost",
    }

    COOLDOWN_KEYS = {
        "tp_spawn_cooldown",
        "rtp_cooldown",
        "tp_home_cooldown",
    }

    REMOVE_KEYS = {
        "spawn_y",
        "spawn_x",
        "spawn_dimension",
        "time_hud_style",
        "type",
        "event_msg",
        "spawn_z",
    }

    # normalize boolean/value tokens into human labels and weekday capitalization
    GLOBAL_VALUE_MAP = {
        "enabled": "Enabled",
        "disabled": "Disabled",
        "monday": "Monday",
        "tuesday": "Tuesday",
        "wednesday": "Wednesday",
        "thursday": "Thursday",
        "friday": "Friday",
        "saturday": "Saturday",
        "sunday": "Sunday",
    }

    # additionally map weekday keys when they appear as dict keys under Active Weekdays
    WEEKDAY_KEY_MAP = {
        "monday": "Monday",
        "tuesday": "Tuesday",
        "wednesday": "Wednesday",
        "thursday": "Thursday",
        "friday": "Friday",
        "saturday": "Saturday",
        "sunday": "Sunday",
    }

    def format_percent_all_decimals(value):
        try:
            if isinstance(value, (int, float)):
                v = float(value)
                if not v.is_integer():
                    return f"{int(round(v * 100))}%"
                return str(int(v)) if isinstance(value, int) else str(int(round(v * 100))) + "%"
            if isinstance(value, str):
                s = value.strip()
                if s == "":
                    return value
                low = s.lower()
                if low in GLOBAL_VALUE_MAP:
                    return GLOBAL_VALUE_MAP[low]
                # numeric check
                if re.match(r"^-?\d+(\.\d+)?$", s):
                    v = float(s)
                    if not v.is_integer():
                        return f"{int(round(v * 100))}%"
                    return s
        except Exception:
            pass
        return value

    def apply_map_fr(obj):
        if isinstance(obj, dict):
            new = {}
            for k, v in obj.items():
                k_str = str(k)
                mapped_key = FR_VALUE_MAP.get(k_str, k_str)
                new[mapped_key] = apply_map_fr(v)
            return new
        if isinstance(obj, list):
            return [apply_map_fr(v) for v in obj]
        if isinstance(obj, str):
            return FR_VALUE_MAP.get(obj, obj)
        return obj

    def apply_map_with_percent(obj, map_dict):
        if isinstance(obj, dict):
            new = {}
            for k, v in obj.items():
                k_str = str(k)
                mapped_key = map_dict.get(k_str, k_str)
                new_val = apply_map_with_percent(v, map_dict)
                new_val = format_percent_all_decimals(new_val)
                new[mapped_key] = new_val
            return new
        if isinstance(obj, list):
            res = [apply_map_with_percent(v, map_dict) for v in obj]
            return [format_percent_all_decimals(v) for v in res]
        if isinstance(obj, str):
            low = obj.lower()
            if low in GLOBAL_VALUE_MAP:
                return GLOBAL_VALUE_MAP[low]
            if obj in map_dict:
                return map_dict[obj]
            return format_percent_all_decimals(obj)
        if isinstance(obj, (int, float)):
            return format_percent_all_decimals(obj)
        return obj

    def remap_value(v):
        """Apply percent formatting recursively and remap dict/list items as needed."""
        if isinstance(v, dict):
            out = {}
            for k, val in v.items():
                ks = str(k)
                if ks in REMOVE_KEYS:
                    continue
                # capitalize weekday keys if present
                key_mapped = WEEKDAY_KEY_MAP.get(ks.lower(), NICE_ACTIONS_KEY_MAP.get(ks, ks))
                out[key_mapped] = remap_value(val)
            return out
        if isinstance(v, list):
            return [remap_value(i) for i in v]
        if isinstance(v, str):
            low = v.lower()
            if low in GLOBAL_VALUE_MAP:
                return GLOBAL_VALUE_MAP[low]
            return format_percent_all_decimals(v)
        if isinstance(v, (int, float)):
            return format_percent_all_decimals(v)
        return v

    def remap_nice_actions(obj):
        """
        Remap keys for nice_actions:
        - rename simple keys
        - collect cost keys under "Action Costs"
        - collect cooldown keys under "Action Cooldowns (Seconds)"
        - remove unwanted keys
        - apply percentage formatting to numeric decimals
        """
        if not isinstance(obj, dict):
            return obj

        result = {}
        action_costs = {}
        action_cooldowns = {}

        for k, v in obj.items():
            if k in REMOVE_KEYS:
                continue
            # costs
            if k in COST_KEYS:
                mapped = NICE_ACTIONS_KEY_MAP.get(k, k)
                action_costs[mapped] = format_percent_all_decimals(remap_value(v))
                continue
            # cooldowns
            if k in COOLDOWN_KEYS:
                mapped = NICE_ACTIONS_KEY_MAP.get(k, k)
                action_cooldowns[mapped] = format_percent_all_decimals(remap_value(v))
                continue
            # generic remap
            mapped_key = NICE_ACTIONS_KEY_MAP.get(k, k)
            # special-case Active Weekdays (misc) to remap weekday keys inside
            if mapped_key == "Active Weekdays" and isinstance(v, dict):
                result[mapped_key] = {WEEKDAY_KEY_MAP.get(kk.lower(), kk): remap_value(vv) for kk, vv in v.items() if kk not in REMOVE_KEYS}
            else:
                result[mapped_key] = remap_value(v)

        if action_costs:
            result["Action Costs"] = action_costs
        if action_cooldowns:
            result["Action Cooldowns (Seconds)"] = action_cooldowns

        return result

    for key, value in settings.items():
        key_str = str(key)
        if key_str == "nice_admin_tools":
            continue
        if key_str == "command_template" or key_str.endswith("_initial"):
            continue

        cleaned = clean(value)
        if cleaned is None or cleaned == {}:
            continue

        if key_str == "fabled_roots" or key_str.startswith("fabled_roots"):
            cleaned = apply_map_fr(cleaned)

        if key_str == "keepinv" or key_str.startswith("keepinv"):
            cleaned = apply_map_with_percent(cleaned, KI_VALUE_MAP)

        if key_str == "warping_wonders" or key_str.startswith("warping_wonders"):
            cleaned = apply_map_with_percent(cleaned, WW_VALUE_MAP)

        if key_str == "nice_actions" or key_str.startswith("nice_actions"):
            cleaned = remap_nice_actions(cleaned)

        safe_key = sanitize_filename(key_str)
        output_path = os.path.join(SETTINGS_DIR, f"{safe_key}.yml")

        write_yaml(output_path, cleaned)
        written += 1

    print(f"✔ settings/*.yml written ({written} files)")


# -------------------------
# GETOFFMYLAWN
# -------------------------
def convert_getoffmylawn():
    path = os.path.join(INPUT_DIR, "getoffmylawn.json")
    if not os.path.exists(path):
        return

    data = json.load(open(path, encoding="utf-8"))
    data = clean(data)

    REMOVE_KEYS = {
        "dimensionBlacklist","regionBlacklist","messagePrefix",
        "placeholderNoClaimInfo","placeholderNoClaimOwners",
        "placeholderNoClaimTrusted","placeholderClaimCanBuildInfo",
        "placeholderClaimCantBuildInfo","claimColorSource",
        "allowFakePlayersToModify","relaxedEntitySourceProtectionCheck",
    }

    RENAME = {
        "maxClaimsPerPlayer": "Max Claims Per Player",
        "enablePvPinClaims": "Enable PVP In Claims",
        "allowDamagingUnnamedHostileMobs": "Allow Damaging Unnamed Hostile Mobs",
        "allowDamagingNamedHostileMobs": "Allow Damaging Named Hostile Mobs",
        "claimProtectsFullWorldHeight": "Claim Protects Full World Height",
        "claimAreaHeightMultiplier": "Claim Area Height Multiplier",
        "makeClaimAreaChunkBound": "Claim Area Is Bound To Chunks",
        "allowClaimOverlappingIfSameOwner": "Allow Claim Overlapping If Same Owner",
        "protectAgainstHostileExplosionsActivatedByTrustedPlayers":
            "Protect Against Hostile Explosions Triggered By Trusted Players",
        "allowedBlockInteraction":
            "Allowed Blocks For Interactions Regardless Of Trust",
        "allowedEntityInteraction":
            "Allowed Entities For Interactions Regardless Of Trust",
    }

    RADIUS = {
        "makeshiftRadius": "Makeshift",
        "reinforcedRadius": "Reinforced",
        "glisteningRadius": "Glistening",
        "crystalRadius": "Crystal",
        "emeradicRadius": "Emerdic",
        "witheredRadius": "Withered",
    }

    AUGMENTS = {
        "goml:withering_seal": "Withering Seal",
        "goml:explosion_controller": "Explosion Controller",
        "goml:lake_spirit_grace": "Spirit Grave",
        "goml:pvp_arena": "PVP Arena",
        "goml:heaven_wings": "Heaven Wings",
        "goml:chaos_zone": "Chaos Zone",
        "goml:village_core": "Village Core",
        "goml:greeter": "Greeter",
        "goml:force_field": "Force Field",
        "goml:ender_binding": "Ender Binding",
        "goml:angelic_aura": "Angelic Aura",
    }

    result = {}
    radius_group = {}

    for k, v in data.items():
        if k in REMOVE_KEYS:
            continue

        if k in RADIUS:
            radius_group[RADIUS[k]] = v
            continue

        if k == "enabledAugments" and isinstance(v, dict):
            result["Enabled Claim Augments"] = {
                AUGMENTS.get(ak, ak): av for ak, av in v.items()
            }
            continue

        result[RENAME.get(k, k)] = v

    if radius_group:
        result["Claim Anchor Radius"] = radius_group

    result = map_booleans(result)

    write_yaml(os.path.join(SETTINGS_DIR, "getoffmylawn.yml"), result)
    print("✔ settings/getoffmylawn.yml")



# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    try:
        fetch_files_via_sftp()
    except Exception as e:
        print(f"SFTP fetch failed: {e}")
    convert_gamerules()
    convert_command_storage()
