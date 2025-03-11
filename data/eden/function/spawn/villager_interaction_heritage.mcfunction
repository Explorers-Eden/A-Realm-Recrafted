execute as @e[type=minecraft:interaction,tag=heritage_villager] if data entity @s attack at @s run data remove entity @s attack
execute as @e[type=minecraft:interaction,tag=heritage_villager] if data entity @s interaction at @s run data remove entity @s interaction

advancement revoke @s only eden:technical/spawn_interactions/villager_heritage

execute unless items entity @s weapon.* #eden:heritage_items run return run tellraw @s [{"text":"Villager: ","color":"green","bold":true,"italic":false},{"text":"You're not holding a heritage token. Talk to me again if you made up your choice and bring me a heritage token.","color":"gray","bold":false,"italic":true}]

execute if items entity @s weapon.* minecraft:arms_up_pottery_sherd[minecraft:custom_data={token:dunesworn}] at @s run return run function heritages:dunesworn/select
execute if items entity @s weapon.* minecraft:ender_eye[minecraft:custom_data={token:endling}] at @s run return run function heritages:endling/select
execute if items entity @s weapon.* minecraft:powder_snow_bucket[minecraft:custom_data={token:frostborne}] at @s run return run function heritages:frostborne/select
execute if items entity @s weapon.* minecraft:echo_shard[minecraft:custom_data={token:moonshroud}] at @s run return run function heritages:moonshroud/select
execute if items entity @s weapon.* minecraft:blaze_powder[minecraft:custom_data={token:netherian}] at @s run return run function heritages:netherian/select
execute if items entity @s weapon.* minecraft:oak_sapling[minecraft:custom_data={token:oakhearted}] at @s run return run function heritages:oakhearted/select
execute if items entity @s weapon.* minecraft:stone_pickaxe[minecraft:custom_data={token:orebringer}] at @s run return run function heritages:orebringer/select
execute if items entity @s weapon.* minecraft:nautilus_shell[minecraft:custom_data={token:turtlekin}] at @s run return run function heritages:turtlekin/select