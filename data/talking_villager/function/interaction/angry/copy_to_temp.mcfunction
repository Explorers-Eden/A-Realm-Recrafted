execute store result score $villager_msg eden.technical run random value 1..20

$execute if score $villager_msg eden.technical matches 1 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.builds.$(id)
$execute if score $villager_msg eden.technical matches 2 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.cats.$(id)
$execute if score $villager_msg eden.technical matches 3 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.creeper.$(id)
$execute if score $villager_msg eden.technical matches 4 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.daily_life.$(id)
$execute if score $villager_msg eden.technical matches 5 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.daylength.$(id)
$execute if score $villager_msg eden.technical matches 6 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.emeralds.$(id)
$execute if score $villager_msg eden.technical matches 7 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.kids.$(id)
$execute if score $villager_msg eden.technical matches 8 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.location.$(id)
$execute if score $villager_msg eden.technical matches 9 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.minecarts.$(id)
$execute if score $villager_msg eden.technical matches 10 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.misc.$(id)
$execute if score $villager_msg eden.technical matches 11 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.neighbor.$(id)
$execute if score $villager_msg eden.technical matches 12 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.nitwit.$(id)
$execute if score $villager_msg eden.technical matches 13 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.no_horse.$(id)
$execute if score $villager_msg eden.technical matches 14 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.phantom.$(id)
$execute if score $villager_msg eden.technical matches 15 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.pillager.$(id)
$execute if score $villager_msg eden.technical matches 16 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.player.$(id)
$execute if score $villager_msg eden.technical matches 17 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.protection.$(id)
$execute if score $villager_msg eden.technical matches 18 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.stealing.$(id)
$execute if score $villager_msg eden.technical matches 19 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.wandering_trader.$(id)
$execute if score $villager_msg eden.technical matches 20 run return run data modify storage eden:temp villager.talking.msg set from storage eden:dialogue_db villager.angry.zombie_villager.$(id)