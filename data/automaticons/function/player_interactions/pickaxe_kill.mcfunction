$tag @s add $(tier)

execute as @s[tag=wood] run loot give @s loot eden:item/automaticons/wood/pickaxe
execute as @s[tag=stone] run loot give @s loot eden:item/automaticons/stone/pickaxe
execute as @s[tag=gold] run loot give @s loot eden:item/automaticons/gold/pickaxe
execute as @s[tag=iron] run loot give @s loot eden:item/automaticons/iron/pickaxe
execute as @s[tag=diamond] run loot give @s loot eden:item/automaticons/diamond/pickaxe
execute as @s[tag=netherite] run loot give @s loot eden:item/automaticons/netherite/pickaxe

execute as @e[type=interaction,tag=ac_pickaxe,tag=automaticon_interaction] if data entity @s attack at @s run particle minecraft:trial_omen ~ ~.3 ~ .2 .5 .2 0 15
execute as @e[type=interaction,tag=ac_pickaxe,tag=automaticon_interaction] if data entity @s attack at @s run kill @s
execute as @e[type=armor_stand,tag=ac_pickaxe,tag=automaticon] at @s unless data entity @s Passengers run kill @s
execute as @e[type=text_display,tag=automaticons_durability_display,predicate=!eden:automaticons/vehicle] run kill @s
execute as @e[type=text_display,tag=automaticons_name_display,predicate=!eden:automaticons/vehicle] run kill @s

$tag @s remove $(tier)
tag @s remove ac_break