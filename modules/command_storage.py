import os
import nbtlib
import re

from modules.utils import sanitize_filename, write_yaml, clean, map_booleans


def convert_command_storage(input_dir, settings_dir):

    path = os.path.join(input_dir, "command_storage.dat")
    if not os.path.exists(path):
        return

    data = nbtlib.load(path).unpack()
    settings = data.get("data", {}).get("contents", {}).get("settings", {})

    WEEKDAY_KEY_MAP = {
        "monday":"Monday","tuesday":"Tuesday","wednesday":"Wednesday",
        "thursday":"Thursday","friday":"Friday","saturday":"Saturday","sunday":"Sunday",
    }

    NICE = {
        "time_format":"Time Format For HUD",
        "rtp_height_min":"Min Y Height For RTP",
        "rtp_height_max":"Max Y Height For RTP",
        "rtp_radius":"RTP Radius (in Blocks)",
        "rtp_type":"RTP Type",
        "player":"Player Position As Origin",
        "events":"Events","fishing":"Fishing","consuming":"Consuming",
        "breeding":"Breeding","misc":"Active Weekdays","killing":"Killing",
        "brewing":"Brewing","chance":"Chance For This Type Of Event",
        "loot_table":"Loot Table","max_amount":"Max Amount Of Actions Needed For Completion",
        "horse_info_cost":"Horse Info","death_coords_cost":"Death/Grave Coordinates",
        "transfer_enchantments_cost":"Transfer Enchantments","send_coords_cost":"Broadcast Coordinates",
        "rtp_cost":"RTP","sit_cost":"Sit","tp_home_cost":"TP Home","set_home_cost":"Set Home",
        "tp_spawn_cost":"TP To Spawn","equip_hat_cost":"Equip Item As Hat",
        "share_stats_cost":"Share Stats","villager_info_cost":"Villager Info",
        "tp_spawn_cooldown":"TP To Spawn","rtp_cooldown":"RTP","tp_home_cooldown":"TP Home",
    }

    COSTS = {k for k in NICE if k.endswith("_cost")}
    COOLDOWNS = {k for k in NICE if k.endswith("_cooldown")}

    REMOVE = {"spawn_y","spawn_x","spawn_dimension","time_hud_style","type","event_msg","spawn_z"}

    def fmt(v):
        if isinstance(v, bool):
            return "Enabled" if v else "Disabled"
        return v

    def remap(obj):
        if isinstance(obj, dict):
            out, costs, cds = {}, {}, {}

            for k,v in obj.items():
                if k in REMOVE:
                    continue

                if k in COSTS:
                    costs[NICE[k]] = fmt(v)
                    continue

                if k in COOLDOWNS:
                    cds[NICE[k]] = fmt(v)
                    continue

                key = WEEKDAY_KEY_MAP.get(k.lower(), NICE.get(k, k))

                if key == "Active Weekdays" and isinstance(v, dict):
                    out[key] = {WEEKDAY_KEY_MAP.get(x.lower(),x): remap(y) for x,y in v.items()}
                else:
                    out[key] = remap(v)

            if costs:
                out["Action Costs"] = costs
            if cds:
                out["Action Cooldowns (Seconds)"] = cds

            return out

        if isinstance(obj, list):
            return [remap(v) for v in obj]

        return fmt(obj)

    written = 0

    for k, v in settings.items():
        if k.endswith("_initial") or k == "nice_admin_tools":
            continue

        cleaned = remap(clean(v))
        write_yaml(os.path.join(settings_dir, f"{sanitize_filename(k)}.yml"), cleaned)
        written += 1

    print(f"✔ settings/*.yml written ({written})")