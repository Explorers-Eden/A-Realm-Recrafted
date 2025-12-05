schedule function eden:spawn/conveyor 2s

execute store result score $conveyor_item eden.technical run random value 1..4
execute if score $conveyor_item eden.technical matches 1 in minecraft:overworld run summon item 49 65 153 {PickupDelay:32767,Invulnerable:1b,Rotation:[-135F,0F],Tags:["realmrecrafted.spawn.conveyor_item"],Item:{id:"minecraft:cod",count:1}}
execute if score $conveyor_item eden.technical matches 2 in minecraft:overworld run summon item 49 65 153 {PickupDelay:32767,Invulnerable:1b,Rotation:[-135F,0F],Tags:["realmrecrafted.spawn.conveyor_item"],Item:{id:"minecraft:salmon",count:1}}
execute if score $conveyor_item eden.technical matches 3 in minecraft:overworld run summon item 49 65 153 {PickupDelay:32767,Invulnerable:1b,Rotation:[-135F,0F],Tags:["realmrecrafted.spawn.conveyor_item"],Item:{id:"minecraft:pufferfish",count:1}}
execute if score $conveyor_item eden.technical matches 4 in minecraft:overworld run summon item 49 65 153 {PickupDelay:32767,Invulnerable:1b,Rotation:[-135F,0F],Tags:["realmrecrafted.spawn.conveyor_item"],Item:{id:"minecraft:tropical_fish",count:1}}

execute as @e[type=item,tag=realmrecrafted.spawn.conveyor_item] at @s if block ~ ~ ~ minecraft:polished_blackstone_pressure_plate run particle minecraft:poof ~ ~ ~ 0.1 0.1 0.1 0.1 3
execute as @e[type=item,tag=realmrecrafted.spawn.conveyor_item] at @s if block ~ ~ ~ minecraft:polished_blackstone_pressure_plate run kill @s