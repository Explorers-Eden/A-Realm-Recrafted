##clear msg schedules
function eden:messages/restart/clear

## add default scoreboard
scoreboard objectives add eden.technical dummy

## set gamerules
#gamerule minecraft:fire_spread_radius_around_player 0
#gamerule minecraft:elytra_movement_check false
#gamerule minecraft:global_sound_events false
#gamerule minecraft:player_movement_check false
#gamerule minecraft:players_nether_portal_creative_delay 0
#gamerule minecraft:players_nether_portal_default_delay 0
#gamerule minecraft:players_sleeping_percentage 51
#gamerule minecraft:lava_source_conversion true
#gamerule minecraft:max_snow_accumulation_height 4
#gamerule minecraft:ender_pearls_vanish_on_death false

##start repeating loops
function eden:start

##set data pack version
data modify storage eden:datapack realmrecrafted.version set value "1.0"