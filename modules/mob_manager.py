import os

from modules.utils import (
    write_yaml,
    sanitize_filename,
    map_booleans,
    deep_format,
    clean,
)

IGNORE = {
    "all_neutral",
    "all_passive",
    "all_hostile",
    "gamerules",
}

DIRECT = {
    "rarity_mobs",
    "mob_drops",
    "wandering_trader_settings",
    "misc",
    "villager_settings",
    "mob_equipment",
}

REMOVE_KEYS = {
    "cap_type",
    "last_name",
    "first_name",
    "capslot",
    "slot",
    "trim_material",
    "trim_pattern",
}

KEY_MAP = {
    "treasurebook": "Enchanted Treasure Book As Trade",
    "spawnmsg": "Player Message When A Wandering Trader Spawns",
    "customname": "Entity Has Custom Name",
    "treasurebookpayitem": "Payment Item For Enchanted Treasure Books",
    "spawnglow": "Wandering Trader Glows When Spawning",
    "treasurebookpayamount": "Max Amount Of Payment Item For Enchanted Treasure Book",
    "miniblock": "Miniblocks As Trade",
    "miniblockpayitem": "Payment Item For Miniblocks",
    "plushie": "Plushies As Trade",
    "plushiepayamount": "Max Amount Of Payment Item For Plushies",
    "plushiepayitem": "Payment Item For Plushies",
    "miniblockpayamount": "Max Amount Of Payment Item For Miniblocks",
    "pet": "Chance Of Villager Having A Pet",
    "villagecenter_healing": "When Entities Near A Village Center Will Be Healed",
    "breeddiversity": "Villagers Can Have Babies With Different Variants",
    "villagename_rename": "Players Can Rename Villages",
    "villagename": "Village Names",
    "restock": "Villagers Restock Their Goods",
    "validmobs": "Entity Tag List Used",
    "villagename_msg": "How Village Names Will Be Displayed To Players",
    "village_heal_distance": "Distance in Blocks Entities Near A Village Center Will Be Healed",
    "locator_range": "Locator Bar Range in Blocks",
    "villager_follow": "Villagers Will Follow Players Holding Emeralds",
    "locator_color": "Locator Bar Color (Hex)",
    "gossip": "Villager Gossip",
    "talking": "How Villagers Respond To Players",
    "rare": "Rare",
    "legendary": "Legendary",
    "mythic": "Mythic",
    "common": "Common",
    "type": "Type",
    "loottable": "Loot Table Used On Death",
    "particles": "Entity Particles",
    "color": "Color",
    "spawnchance": "Chance Of Becoming A Rarity Mob Of This Type",
    "health": "Health (%)",
    "spawntime": "Time In Seconds Before Entity Can Become A Rarity Mob Of This Type",
    "mainhand": "Mainhand",
    "offhand": "Offhand",
    "head": "Head",
    "misc": "Misc",
    "feet": "Feet",
    "legs": "Legs",
    "chest": "Chest",
    "dropchance": "Chance Of Item Being Dropped (Only Applies When Not Vanilla)",
    "enchantment": "Chance Of Item Being Enchanted",
    "rngdmg": "Apply Random Damage To Item",
    "equipchance": "Chance Of Entity Being Equipped With Custom Item",
    "equiploottable": "Loot Table Used For Custom Equipment Item",
    "mobheads": "Chance Of Entity Wearing A Random Mob Head",
    "trim": "Equipment Can Be Trimmed",
    "bannershield": "Shields Have Random Banners",
    "vex_equip": "Mainhand Item For Vex",
    "leathercolor": "Leather Equipment Can Have Random Colors",
    "playerheads": "Chance For Entity Wearing A Random Mob Head",
    "dragonegg": "Chance For Ender Dragon To Drop A Dragon Egg",
    "creakingresin": "Chance For Creaking To Drop Resin",
    "strayice": "Chance For Stray To Drop Ice",
    "goatleather": "Chance For Goat To Drop Leather",
    "shulkerdrop": "Chance For Shulker To Drop Additional Shulker Shell",
    "allayshard": "Chance For Allay To Drop Amethyst Shard",
    "elderguardianseaheart": "Chance For Elder Guardian To Drop Heart Of The Ocean",
    "villageremerald": "Chance For Villager To Drop Emerald",
    "traderlead": "Chance For Wandering Trader To Drop Lead",
    "piglingold": "Chance For Piglin To Drop Gold",
    "beehoneycomb": "Chance For Bee To Drop Honeycomb",
    "dragonelytra": "Chance For Ender Dragon To Drop Elytra",
    "witherskulldrop": "Chance For Wither Skeleton To Drop Additional Skull",
    "foxsweetberries": "Chance For Fox To Drop Sweet Berries",
    "batmembrane": "Chance For Bat To Drop Phantom Membrane",
    "piglinbrutegoldblock": "Chance For Piglin Brute To Drop Gold Block",
    "husksand": "Chance For Husk To Drop Sand",
    "rabbitcarrot": "Rabbits Can Eat Planted Carrots",
    "illusionerspawning": "Chance Of Illusioner Spawning Instead Of Evoker",
    "killerrabbitspawning": "Chance Of Rabbit Being A Killer Rabbit",
    "egglay": "Chickens Can Lay Eggs",
    "jebcolor": "Sheep Can Be _jeb",
    "lefthanded": "Chance Of Mobs Being Left Handed",
    "shulkercolor": "Shulker Can Have Random Colors",
    "snifferbrain": "Sniffer Remember Where They Dug",
    "irongolemanger": "Iron Golem Can Be Angered",
    "jebspawning": "Chance Of Sheep Being A _jeb Sheep",
    "locator_assets": "Custom Icons For Locator Bar",
    "immunezombie": "Chance Of Entity Being Immune To Zombification",
    "brownmoospawning": "Chance Of Mooshroom Being A Brown Variant",
    "creeperfuse": "Creeper Fuse Time And Explosion Radius Depends On Their Size",
    "skeletonhorsetrap": "Skeleton Horse Traps",
    "mobs_on_locator_bar": "Entities Will Be Shown On Locator Bar",
    "babymountspawning": "Chance Of Entity Having A Baby Rider",
    "need_sky": "Mobs Need To See Skylight For Custom Changes",
    "scale_min": "Min Entity Size (%)",
    "move_speed": "Movement Speed (%)",
    "allow_mob": "Entity Spawning",
    "drown": "Entity Can Drown",
    "breed": "Entity Can Breed",
    "follow_range": "Follow Range (%)",
    "silent": "Entity Is Silent By Default",
    "attck_dmg": "Attack Damage (%)",
    "tempt_range": "Tempt Range (%)",
    "pickup": "Entity Can Pickup Loot",
    "burn": "Entity Can Burn",
    "safe_fall": "Safe Fall Distance (%)",
    "scale_max": "Max Entity Size (%)",
}


def remap_mob_manager_value(obj, mobhead_label):
    if isinstance(obj, dict):
        out = {}
        for key, value in obj.items():
            key_str = str(key)

            if key_str in REMOVE_KEYS:
                continue

            if key_str == "mobhead":
                mapped_key = mobhead_label
            else:
                mapped_key = KEY_MAP.get(key_str, key_str)

            out[mapped_key] = remap_mob_manager_value(value, mobhead_label)
        return out

    if isinstance(obj, list):
        return [remap_mob_manager_value(v, mobhead_label) for v in obj]

    return obj


def keep_leathercolor_only_in_misc(data):
    if not isinstance(data, dict):
        return data

    leather_key = "Leather Equipment Can Have Random Colors"

    for section_name, section_value in data.items():
        if not isinstance(section_value, dict):
            continue

        if section_name != "Misc" and leather_key in section_value:
            del section_value[leather_key]

    return data


def handle_mob_manager(data, settings_dir):
    base = os.path.join(settings_dir, "mob_manager")
    entities = os.path.join(base, "entities")

    os.makedirs(base, exist_ok=True)
    os.makedirs(entities, exist_ok=True)

    for key, value in data.items():
        if key in IGNORE:
            continue

        value = clean(value)
        if not value:
            continue

        if key == "mob_equipment":
            mobhead_label = "Chance Of Entity Wearing A Random Mob Head"
            path = os.path.join(base, f"{sanitize_filename(key)}.yml")
        elif key in DIRECT:
            mobhead_label = "Chance Of Entity Dropping Its Head"
            path = os.path.join(base, f"{sanitize_filename(key)}.yml")
        else:
            mobhead_label = "Chance Of Entity Dropping Its Head"
            path = os.path.join(entities, f"{sanitize_filename(key)}.yml")

        value = remap_mob_manager_value(value, mobhead_label)
        value = map_booleans(value)
        value = deep_format(value)

        if key == "mob_equipment":
            value = keep_leathercolor_only_in_misc(value)

        write_yaml(path, value)

    print("✔ mob_manager split")