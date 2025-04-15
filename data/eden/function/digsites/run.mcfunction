execute as @e[type=player,tag=!at_digsite,tag=has_heritage] at @s if entity @e[type=marker,predicate=eden:entity/is_digsite,distance=..32] run function eden:digsites/location/entering
execute as @e[type=player,tag=!not_at_digsite,tag=has_heritage] at @s unless entity @e[type=marker,predicate=eden:entity/is_digsite,distance=..32] run function eden:digsites/location/exiting

execute as @e[type=marker,predicate=eden:entity/is_digsite,tag=!digsite_finished] at @s run scoreboard players add @s eden.digsite.attempts 0
execute as @e[type=marker,predicate=eden:entity/is_digsite,tag=!digsite_finished] at @s run scoreboard players add @s eden.digsite.placed 0
execute as @e[type=marker,tag=eden.digsite.grass,tag=!digsite_finished] at @s if score @s eden.digsite.placed matches ..41 if score @s eden.digsite.attempts matches ..999 run function eden:digsites/grass/get_data
execute as @e[type=marker,tag=eden.digsite.nether,tag=!digsite_finished] at @s if score @s eden.digsite.placed matches ..41 if score @s eden.digsite.attempts matches ..999 run function eden:digsites/nether/get_data
execute as @e[type=marker,tag=eden.digsite.end,tag=!digsite_finished] at @s if score @s eden.digsite.placed matches ..41 if score @s eden.digsite.attempts matches ..999 run function eden:digsites/end/get_data
execute as @e[type=marker,tag=eden.digsite.ice,tag=!digsite_finished] at @s if score @s eden.digsite.placed matches ..41 if score @s eden.digsite.attempts matches ..999 run function eden:digsites/ice/get_data
execute as @e[type=marker,tag=eden.digsite.sand,tag=!digsite_finished] at @s if score @s eden.digsite.placed matches ..41 if score @s eden.digsite.attempts matches ..999 run function eden:digsites/sand/get_data
execute as @e[type=marker,tag=eden.digsite.snow,tag=!digsite_finished] at @s if score @s eden.digsite.placed matches ..41 if score @s eden.digsite.attempts matches ..999 run function eden:digsites/snow/get_data
execute as @e[type=marker,tag=eden.digsite.stone,tag=!digsite_finished] at @s if score @s eden.digsite.placed matches ..41 if score @s eden.digsite.attempts matches ..999 run function eden:digsites/stone/get_data
execute as @e[type=marker,tag=eden.digsite.terracotta,tag=!digsite_finished] at @s if score @s eden.digsite.placed matches ..41 if score @s eden.digsite.attempts matches ..999 run function eden:digsites/terracotta/get_data
execute as @e[type=marker,tag=eden.digsite.water,tag=!digsite_finished] at @s if score @s eden.digsite.placed matches ..41 if score @s eden.digsite.attempts matches ..999 run function eden:digsites/water/get_data

schedule function eden:digsites/run 7t