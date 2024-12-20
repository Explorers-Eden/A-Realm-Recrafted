data modify entity @s HandDropChances[1] set value -327.670F
execute store result score $eden.offhand eden.technical run random value 1..21

$execute if score $eden.offhand eden.technical matches 1 run return run data modify entity @s HandItems[1] set value {id:"minecraft:$(material)_sword",count:1}
$execute if score $eden.offhand eden.technical matches 2 run return run data modify entity @s HandItems[1] set value {id:"minecraft:$(material)_axe",count:1}
execute if score $eden.offhand eden.technical matches 3..10 run return run function mob_equipment:offhand/banner_shields
execute if score $eden.offhand eden.technical matches 11 run return run data modify entity @s HandItems[1] set value {id:"minecraft:experience_bottle",count:1}
execute if score $eden.offhand eden.technical matches 12 run return run data modify entity @s HandItems[1] set value {id:"minecraft:bread",count:1}
execute if score $eden.offhand eden.technical matches 13 run return run data modify entity @s HandItems[1] set value {id:"minecraft:cooked_beef",count:1}
execute if score $eden.offhand eden.technical matches 14 run return run data modify entity @s HandItems[1] set value {id:"minecraft:cooked_chicken",count:1}
execute if score $eden.offhand eden.technical matches 15 run return run data modify entity @s HandItems[1] set value {id:"minecraft:cooked_porkchop",count:1}
execute if score $eden.offhand eden.technical matches 16 run return run data modify entity @s HandItems[1] set value {id:"minecraft:cooked_mutton",count:1}
execute if score $eden.offhand eden.technical matches 17..21 run return run data modify entity @s HandItems[1] set value {id:"minecraft:totem_of_undying",count:1}