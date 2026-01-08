##clear msg schedules
function eden:messages/restart/clear

## add default scoreboard
scoreboard objectives add eden.technical dummy

## set gamerules
gamerule minecraft:fire_spread_radius_around_player 0
gamerule minecraft:elytra_movement_check false
gamerule minecraft:global_sound_events false
gamerule minecraft:player_movement_check false
gamerule minecraft:players_nether_portal_creative_delay 0
gamerule minecraft:players_nether_portal_default_delay 0
gamerule minecraft:players_sleeping_percentage 51
gamerule minecraft:show_advancement_messages false
gamerule minecraft:lava_source_conversion true
gamerule minecraft:max_snow_accumulation_height 4
gamerule minecraft:ender_pearls_vanish_on_death false

##animations at spawn
schedule function eden:spawn/decoration/frogs/_/stop_anim 5t
schedule function eden:spawn/decoration/frogs/a/default/play_anim_loop 10t

##chunky
schedule function eden:chunky/add_borders 10s

##set data pack version
data modify storage eden:datapack realmrecrafted.version set value "1.0"