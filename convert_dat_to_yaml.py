import os
import re
import yaml
import json
import nbtlib
import paramiko

# ---- SFTP CONFIG ----
SFTP_HOST = os.getenv("SFTP_HOST")
SFTP_PORT = int(os.getenv("SFTP_PORT", "22"))
SFTP_USER = os.getenv("SFTP_USER")
SFTP_PASS = os.getenv("SFTP_PASS")

# ---- REMOTE PATHS ----
SFTP_REMOTE_GAME_RULES = "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/world/data/minecraft/game_rules.dat"
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
        out = {}
        for k, v in obj.items():
            k = str(k)
            if k.endswith("_initial") or k in ("command_template", "icon", "bodyicon") or "command_template" in k:
                continue
            val = clean(v)
            if isinstance(val, str) and "command_template" in val:
                continue
            out[k] = val
        return out

    if isinstance(obj, list):
        return [clean(v) for v in obj if "command_template" not in str(v)]

    if isinstance(obj, str) and "command_template" in obj:
        return None

    return obj


# -------------------------
# GAMERULES
# -------------------------
def convert_gamerules():
    path = os.path.join(INPUT_DIR, "game_rules.dat")
    if not os.path.exists(path):
        return

    nbt = nbtlib.load(path).unpack()
    raw = nbt.get("data", {})

    out = {}
    for k, v in raw.items():
        s = str(v).lower()
        if s in ("true", "1"):
            out[k] = "Enabled"
        elif s in ("false", "0"):
            out[k] = "Disabled"
        else:
            out[k] = v

    write_yaml(os.path.join(OUTPUT_DIR, "gamerules.yml"), out)
    print("✔ gamerules.yml")


# -------------------------
# COMMAND STORAGE
# -------------------------
def convert_command_storage():
    path = os.path.join(INPUT_DIR, "command_storage.dat")
    if not os.path.exists(path):
        return

    nbt = nbtlib.load(path).unpack()
    settings = nbt.get("data", {}).get("contents", {}).get("settings", {})

    for key, value in settings.items():
        if str(key).endswith("_initial"):
            continue

        cleaned = clean(value)
        if not cleaned:
            continue

        cleaned = map_booleans(cleaned)

        name = sanitize_filename(key)
        write_yaml(os.path.join(SETTINGS_DIR, f"{name}.yml"), cleaned)

    print("✔ settings/*.yml")


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
        "dimensionBlacklist", "regionBlacklist", "messagePrefix",
        "placeholderNoClaimInfo", "placeholderNoClaimOwners",
        "placeholderNoClaimTrusted", "placeholderClaimCanBuildInfo",
        "placeholderClaimCantBuildInfo", "claimColorSource",
        "allowFakePlayersToModify", "relaxedEntitySourceProtectionCheck",
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
        print("SFTP error:", e)

    convert_gamerules()
    convert_command_storage()
    convert_getoffmylawn()