import os
from modules.utils import write_yaml, sanitize_filename, map_booleans, deep_format

IGNORE = {"all_neutral", "all_passive", "all_hostile", "gamerules"}

DIRECT = {
    "rarity_mobs",
    "mob_drops",
    "wandering_trader_settings",
    "misc",
    "villager_settings",
    "mob_equipment",
}


def handle_mob_manager(data, settings_dir):
    base = os.path.join(settings_dir, "mob_manager")
    entities = os.path.join(base, "entities")

    os.makedirs(base, exist_ok=True)
    os.makedirs(entities, exist_ok=True)

    for key, value in data.items():
        if key in IGNORE:
            continue

        value = map_booleans(value)
        value = deep_format(value)

        if key in DIRECT:
            path = os.path.join(base, f"{sanitize_filename(key)}.yml")
        else:
            path = os.path.join(entities, f"{sanitize_filename(key)}.yml")

        write_yaml(path, value)

    print("✔ mob_manager split")