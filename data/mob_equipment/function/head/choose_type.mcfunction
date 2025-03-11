execute store result score $eden.head.type eden.technical run random value 1..89
execute store result score $eden.head.trimmed eden.technical run random value 1..2

##Leather Helmet
$execute if score $eden.head.type eden.technical matches 1..30 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:leather_helmet",count:1,components:{"minecraft:dyed_color":{rgb:$(color)}}}
$execute if score $eden.head.type eden.technical matches 1..30 if score $eden.head.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[3] set value {id:"minecraft:leather_helmet",count:1,components:{"minecraft:dyed_color":{rgb:$(color)},trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

##Iron Helmet
execute if score $eden.head.type eden.technical matches 31..40 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:iron_helmet",count:1}
$execute if score $eden.head.type eden.technical matches 31..40 if score $eden.head.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[3] set value {id:"minecraft:iron_helmet",count:1,components:{trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

##Golden Helmet
execute if score $eden.head.type eden.technical matches 41..50 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:golden_helmet",count:1}
$execute if score $eden.head.type eden.technical matches 41..50 if score $eden.head.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[3] set value {id:"minecraft:golden_helmet",count:1,components:{trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

##Chainmail Helmet
execute if score $eden.head.type eden.technical matches 51..60 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:chainmail_helmet",count:1}
$execute if score $eden.head.type eden.technical matches 51..60 if score $eden.head.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[3] set value {id:"minecraft:chainmail_helmet",count:1,components:{trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

##Diamond Helmet
execute if score $eden.head.type eden.technical matches 61..65 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:diamond_helmet",count:1}
$execute if score $eden.head.type eden.technical matches 61..65 if score $eden.head.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[3] set value {id:"minecraft:diamond_helmet",count:1,components:{trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

##Netherite Helmet
execute if score $eden.head.type eden.technical matches 66..67 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:netherite_helmet",count:1}
$execute if score $eden.head.type eden.technical matches 66..67 if score $eden.head.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[3] set value {id:"minecraft:netherite_helmet",count:1,components:{trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

##Turtle Helmet
execute if score $eden.head.type eden.technical matches 66..80 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:turtle_helmet",count:1}
$execute if score $eden.head.type eden.technical matches 66..80 if score $eden.head.trimmed eden.technical matches 2 run data modify entity @s ArmorItems[3] set value {id:"minecraft:turtle_helmet",count:1,components:{trim:{material:"minecraft:$(trim_material)",pattern:"minecraft:$(trim_pattern)"}}}

##other
execute if score $eden.head.type eden.technical matches 81 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:lightning_rod",count:1}
execute if score $eden.head.type eden.technical matches 83 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:feather",count:1}
execute if score $eden.head.type eden.technical matches 85 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:bone",count:1}
execute if score $eden.head.type eden.technical matches 87 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:end_rod",count:1}
execute if score $eden.head.type eden.technical matches 89 if score $eden.head.trimmed eden.technical matches 1 run data modify entity @s ArmorItems[3] set value {id:"minecraft:cod",count:1}

execute if score $eden.feet.type eden.technical matches 1..30 run data modify entity @s ArmorDropChances[3] set value 0.025F
execute if score $eden.feet.type eden.technical matches 31..40 run data modify entity @s ArmorDropChances[3] set value 0.020F
execute if score $eden.feet.type eden.technical matches 41..50 run data modify entity @s ArmorDropChances[3] set value 0.015F
execute if score $eden.feet.type eden.technical matches 51..60 run data modify entity @s ArmorDropChances[3] set value 0.010F
execute if score $eden.feet.type eden.technical matches 61..89 run data modify entity @s ArmorDropChances[3] set value -327.670F