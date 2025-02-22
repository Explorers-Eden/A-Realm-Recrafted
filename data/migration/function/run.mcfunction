execute as @a[tag=!heritage.old.removed,tag=dunesworn] at @s run function migration:heritages/dunesworn
execute as @a[tag=!heritage.old.removed,tag=endling] at @s run function migration:heritages/endling
execute as @a[tag=!heritage.old.removed,tag=frostborne] at @s run function migration:heritages/frostborne
execute as @a[tag=!heritage.old.removed,tag=moonshroud] at @s run function migration:heritages/moonshroud
execute as @a[tag=!heritage.old.removed,tag=netherian] at @s run function migration:heritages/netherian
execute as @a[tag=!heritage.old.removed,tag=oakhearted] at @s run function migration:heritages/oakhearted
execute as @a[tag=!heritage.old.removed,tag=orebringer] at @s run function migration:heritages/orebringer
execute as @a[tag=!heritage.old.removed,tag=turtlekin] at @s run function migration:heritages/turtlekin

execute as @e[type=interaction,tag=wawo.lodestone.hub] at @s run function migration:lodestone_hub
execute as @e[type=interaction,tag=weather_device] at @s run function migration:weather_device
execute as @e[type=interaction,tag=outer_wilds_portal] at @s run function migration:outer_wilds_portal

execute as @a run attribute @s minecraft:max_health modifier remove pdr_1
execute as @a run attribute @s minecraft:max_health modifier remove pdr_2
execute as @a run attribute @s minecraft:max_health modifier remove pdr_3
execute as @a run attribute @s minecraft:max_health modifier remove pdr_4
execute as @a run attribute @s minecraft:max_health modifier remove pdr_5

execute as @a[team=eden.orebringer,tag=!hero_effect_removed] run function migration:remove_hero

#schedule function migration:run 13s