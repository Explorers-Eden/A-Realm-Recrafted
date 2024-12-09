execute as @e[type=armor_stand,tag=automaticon] run scoreboard players add @s automaticons.tool.durability.current 0

execute as @e[type=armor_stand,tag=axe_netherite_tier] at @s if items entity @s weapon.mainhand #eden:automaticons/is_valid_axe if score @s automaticons.tool.durability.current matches 1..196 run function automaticons:farming/netherite/axe/get_data
execute as @e[type=armor_stand,tag=hoe_netherite_tier] at @s if items entity @s weapon.mainhand #eden:automaticons/is_valid_hoe if score @s automaticons.tool.durability.current matches 1..196 run function automaticons:farming/netherite/hoe/get_data
execute as @e[type=armor_stand,tag=pickaxe_netherite_tier] at @s if items entity @s weapon.mainhand #eden:automaticons/is_valid_pickaxe if score @s automaticons.tool.durability.current matches 1..196 run function automaticons:farming/netherite/pickaxe/get_data
execute as @e[type=armor_stand,tag=shovel_netherite_tier] at @s if items entity @s weapon.mainhand #eden:automaticons/is_valid_shovel if score @s automaticons.tool.durability.current matches 1..196 run function automaticons:farming/netherite/shovel/get_data
execute as @e[type=armor_stand,tag=sword_netherite_tier] at @s if items entity @s weapon.mainhand #eden:automaticons/is_valid_sword if score @s automaticons.tool.durability.current matches 1..196 run function automaticons:farming/netherite/sword/get_data