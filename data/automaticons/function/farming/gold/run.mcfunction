execute as @e[type=armor_stand,tag=automaticon] run scoreboard players add @s automaticons.tool.durability.current 0

execute as @e[type=armor_stand,tag=axe_gold_tier] at @s if items entity @s weapon.mainhand #eden:automaticons/is_valid_axe if score @s automaticons.tool.durability.current matches 1..96 run function automaticons:farming/gold/axe/get_data
execute as @e[type=armor_stand,tag=hoe_gold_tier] at @s if items entity @s weapon.mainhand #eden:automaticons/is_valid_hoe if score @s automaticons.tool.durability.current matches 1..96 run function automaticons:farming/gold/hoe/get_data
execute as @e[type=armor_stand,tag=pickaxe_gold_tier] at @s if items entity @s weapon.mainhand #eden:automaticons/is_valid_pickaxe if score @s automaticons.tool.durability.current matches 1..96 run function automaticons:farming/gold/pickaxe/get_data
execute as @e[type=armor_stand,tag=shovel_gold_tier] at @s if items entity @s weapon.mainhand #eden:automaticons/is_valid_shovel if score @s automaticons.tool.durability.current matches 1..96 run function automaticons:farming/gold/shovel/get_data
execute as @e[type=armor_stand,tag=sword_gold_tier] at @s if items entity @s weapon.mainhand #eden:automaticons/is_valid_sword if score @s automaticons.tool.durability.current matches 1..96 run function automaticons:farming/gold/sword/get_data