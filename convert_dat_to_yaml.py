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
        print("SFTP_HOST, SFTP_USER and SFTP_PASS must be set in the environment to fetch files via SFTP.")
        return

    transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))
    try:
        transport.connect(username=SFTP_USER, password=SFTP_PASS)
        sftp = paramiko.SFTPClient.from_transport(transport)

        remote_files = [
            (SFTP_REMOTE_GAME_RULES, os.path.join(INPUT_DIR, "game_rules.dat")),
            (SFTP_REMOTE_COMMAND_STORAGE, os.path.join(INPUT_DIR, "command_storage.dat")),
        ]
        for remote_path, local_path in remote_files:
            try:
                sftp.get(remote_path, local_path)
                print(f"Downloaded: {remote_path} -> {local_path}")
            except IOError as e:
                print(f"Could not download {remote_path}: {e}")
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
        yaml.dump(data, f, sort_keys=False)


# -------------------------
# CLEANER
# -------------------------
def clean(obj):
    """
    Recursively removes:
    - *_initial keys
    - command_template anywhere
    - icon/bodyicon fields anywhere
    """
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

    def format_percent_all_decimals(value):
        try:
            if isinstance(value, (int, float)):
                v = float(value)
                if not v.is_integer():
                    return f"{int(round(v * 100))}%"
                return f"{int(v)}" if isinstance(value, int) else f"{int(round(v * 100))}%"
            if isinstance(value, str):
                s = value.strip()
                if s == "":
                    return value
                if "." in s or re.match(r"^\d+(\.\d+)?$", s):
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
            if obj in map_dict:
                return map_dict[obj]
            return format_percent_all_decimals(obj)
        if isinstance(obj, (int, float)):
            return format_percent_all_decimals(obj)
        return obj

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
        safe_key = sanitize_filename(key_str)
        output_path = os.path.join(SETTINGS_DIR, f"{safe_key}.yml")
        write_yaml(output_path, cleaned)
        written += 1
    print(f"✔ settings/*.yml written ({written} files)")


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
