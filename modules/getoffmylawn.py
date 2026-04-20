import os
import json

from modules.utils import write_yaml, clean, map_booleans


def convert_getoffmylawn(input_dir, settings_dir):

    path = os.path.join(input_dir, "getoffmylawn.json")
    if not os.path.exists(path):
        return

    data = clean(json.load(open(path, encoding="utf-8")))

    REMOVE = {
        "dimensionBlacklist","regionBlacklist","messagePrefix",
        "placeholderNoClaimInfo","placeholderNoClaimOwners",
        "placeholderNoClaimTrusted","placeholderClaimCanBuildInfo",
        "placeholderClaimCantBuildInfo","claimColorSource",
        "allowFakePlayersToModify","relaxedEntitySourceProtectionCheck",
    }

    RENAME = {
        "maxClaimsPerPlayer":"Max Claims Per Player",
        "enablePvPinClaims":"Enable PVP In Claims",
        "allowDamagingUnnamedHostileMobs":"Allow Damaging Unnamed Hostile Mobs",
        "allowDamagingNamedHostileMobs":"Allow Damaging Named Hostile Mobs",
        "claimProtectsFullWorldHeight":"Claim Protects Full World Height",
        "claimAreaHeightMultiplier":"Claim Area Height Multiplier",
        "makeClaimAreaChunkBound":"Claim Area Is Bound To Chunks",
        "allowClaimOverlappingIfSameOwner":"Allow Claim Overlapping If Same Owner",
        "protectAgainstHostileExplosionsActivatedByTrustedPlayers":
            "Protect Against Hostile Explosions Triggered By Trusted Players",
        "allowedBlockInteraction":"Allowed Blocks For Interactions Regardless Of Trust",
        "allowedEntityInteraction":"Allowed Entities For Interactions Regardless Of Trust",
    }

    RADIUS = {
        "makeshiftRadius":"Makeshift",
        "reinforcedRadius":"Reinforced",
        "glisteningRadius":"Glistening",
        "crystalRadius":"Crystal",
        "emeradicRadius":"Emerdic",
        "witheredRadius":"Withered",
    }

    AUGMENTS = {
        "goml:withering_seal":"Withering Seal",
        "goml:explosion_controller":"Explosion Controller",
        "goml:lake_spirit_grace":"Spirit Grave",
        "goml:pvp_arena":"PVP Arena",
        "goml:heaven_wings":"Heaven Wings",
        "goml:chaos_zone":"Chaos Zone",
        "goml:village_core":"Village Core",
        "goml:greeter":"Greeter",
        "goml:force_field":"Force Field",
        "goml:ender_binding":"Ender Binding",
        "goml:angelic_aura":"Angelic Aura",
    }

    result, radius = {}, {}

    for k,v in data.items():
        if k in REMOVE:
            continue

        if k in RADIUS:
            radius[RADIUS[k]] = v
            continue

        if k == "enabledAugments" and isinstance(v, dict):
            result["Enabled Claim Augments"] = {AUGMENTS.get(a,a):b for a,b in v.items()}
            continue

        result[RENAME.get(k,k)] = v

    if radius:
        result["Claim Anchor Radius"] = radius

    write_yaml(os.path.join(settings_dir, "getoffmylawn.yml"), map_booleans(result))
    print("✔ getoffmylawn.yml")