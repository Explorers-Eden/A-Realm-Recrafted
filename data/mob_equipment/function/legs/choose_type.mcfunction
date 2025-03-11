execute store result score $eden.legs.type eden.technical run random value 1..67
execute store result score $eden.legs.trimmed eden.technical run random value 1..2

##Leather Armor
$execute if score $eden.legs.type eden.technical matches 1..30 if score $eden.legs.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[1] set value {id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":{rgb:$(color)}}}
$execute if score $eden.legs.type eden.technical matches 1..30 if score $eden.legs.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[1] set value {id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":{rgb:$(color)},trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

##Iron Armor
execute if score $eden.legs.type eden.technical matches 31..40 if score $eden.legs.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[1] set value {id:"minecraft:iron_leggings",count:1}
$execute if score $eden.legs.type eden.technical matches 31..40 if score $eden.legs.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[1] set value {id:"minecraft:iron_leggings",count:1,components:{trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

##Golden Armor
execute if score $eden.legs.type eden.technical matches 41..50 if score $eden.legs.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[1] set value {id:"minecraft:golden_leggings",count:1}
$execute if score $eden.legs.type eden.technical matches 41..50 if score $eden.legs.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[1] set value {id:"minecraft:golden_leggings",count:1,components:{trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

##Chainmail Armor
execute if score $eden.legs.type eden.technical matches 51..60 if score $eden.legs.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[1] set value {id:"minecraft:chainmail_leggings",count:1}
$execute if score $eden.legs.type eden.technical matches 51..60 if score $eden.legs.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[1] set value {id:"minecraft:chainmail_leggings",count:1,components:{trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}


##Diamond Armor
execute if score $eden.legs.type eden.technical matches 61..65 if score $eden.legs.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[1] set value {id:"minecraft:diamond_leggings",count:1}
$execute if score $eden.legs.type eden.technical matches 61..65 if score $eden.legs.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[1] set value {id:"minecraft:diamond_leggings",count:1,components:{trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

##Netherite Armor
execute if score $eden.legs.type eden.technical matches 66..67 if score $eden.legs.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[1] set value {id:"minecraft:netherite_leggings",count:1}
$execute if score $eden.legs.type eden.technical matches 66..67 if score $eden.legs.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[1] set value {id:"minecraft:netherite_leggings",count:1,components:{trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

execute if score $eden.legs.type eden.technical matches 1..30 run data modify entity @s ArmorDropChances[1] set value 0.025F
execute if score $eden.legs.type eden.technical matches 31..40 run data modify entity @s ArmorDropChances[1] set value 0.020F
execute if score $eden.legs.type eden.technical matches 41..50 run data modify entity @s ArmorDropChances[1] set value 0.015F
execute if score $eden.legs.type eden.technical matches 51..60 run data modify entity @s ArmorDropChances[1] set value 0.010F
execute if score $eden.legs.type eden.technical matches 61..67 run data modify entity @s ArmorDropChances[1] set value -327.670F