clear @s minecraft:arms_up_pottery_sherd[minecraft:custom_data={token:dunesworn}]
clear @s minecraft:ender_eye[minecraft:custom_data={token:endling}]
clear @s minecraft:powder_snow_bucket[minecraft:custom_data={token:frostborne}]
clear @s minecraft:echo_shard[minecraft:custom_data={token:moonshroud}]
clear @s minecraft:blaze_powder[minecraft:custom_data={token:netherian}]
clear @s minecraft:oak_sapling[minecraft:custom_data={token:oakhearted}]
clear @s minecraft:stone_pickaxe[minecraft:custom_data={token:orebringer}]
clear @s minecraft:nautilus_shell[minecraft:custom_data={token:turtlekin}]

give @s blaze_powder[item_name={"bold":false,"color":"red","italic":false,"text":"Token of a Netherian"},custom_data={token:netherian}] 1

execute as @s at @s run playsound minecraft:entity.chicken.egg neutral @s ~ ~ ~ .6 2
tellraw @s [{"text":"▊ ","color":"red","bold":true,"italic":false},{"text":"Forged in the crucible of lava and brimstone, the Netherians are a race born from the searing heat and molten chaos of the Nether. Their homeland is a land of perpetual fire and ash, where rivers of lava flow freely and the very air is thick with the scent of sulfur.","color":"#D1D1D1","bold":false,"italic":false}]

tellraw @s [{"text":"▊ ","color":"red","bold":true,"italic":false},{"text":" ","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"red","bold":true,"italic":false},{"text":"Characteristics:","color":"red","bold":false,"italic":false,"underlined":true}]
tellraw @s [{"text":"▊ ","color":"red","bold":true,"italic":false},{"text":"• 3.0 Base Attack Speed","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"red","bold":true,"italic":false},{"text":"• 0.0 Base Burning Time","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"red","bold":true,"italic":false},{"text":"• Infinite Fire Resistance Effect","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"red","bold":true,"italic":false},{"text":"• Small Strength Effect When In The Nether","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"red","bold":true,"italic":false},{"text":"• Guardian Entity: 3 Zombified Piglin","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"red","bold":true,"italic":false},{"text":" ","color":"#D1D1D1","bold":false,"italic":false}]

tellraw @s [{"text":"▊ ","color":"red","bold":true,"italic":false},{"text":"You can join this Heritage by giving the Token to the Villager in this room.","color":"#D1D1D1","bold":false,"italic":false},{"text":" Choose wisely! Heritages can only be changed once every month.","color":"#D1D1D1","bold":false,"italic":false}]

execute as @e[type=minecraft:interaction,tag=spawn_netherian_choice] if data entity @s attack at @s run data remove entity @s attack
execute as @e[type=minecraft:interaction,tag=spawn_netherian_choice] if data entity @s interaction at @s run data remove entity @s interaction

advancement revoke @s only eden:technical/spawn_interactions/right_netherian_choice