clear @s minecraft:arms_up_pottery_sherd[minecraft:custom_data={token:dunesworn}]
clear @s minecraft:ender_eye[minecraft:custom_data={token:endling}]
clear @s minecraft:powder_snow_bucket[minecraft:custom_data={token:frostborne}]
clear @s minecraft:echo_shard[minecraft:custom_data={token:moonshroud}]
clear @s minecraft:fire_charge[minecraft:custom_data={token:netherian}]
clear @s minecraft:oak_sapling[minecraft:custom_data={token:oakhearted}]
clear @s minecraft:stone_pickaxe[minecraft:custom_data={token:orebringer}]
clear @s minecraft:nautilus_shell[minecraft:custom_data={token:turtlekin}]

give @s nautilus_shell[item_name={"bold":false,"color":"dark_aqua","italic":false,"text":"Token of a Turtlekin"},custom_data={token:turtlekin}] 1

execute as @s at @s run playsound minecraft:entity.chicken.egg neutral @s ~ ~ ~ .6 2
tellraw @s [{"text":"▊ ","color":"dark_aqua","bold":true,"italic":false},{"text":"Legend speaks of the Turtlekin, an ancient race born from the primordial energies of the sea itself. Shaped by the essence of the ocean’s currents and tides, they are one with the vast and mysterious depths.","color":"#D1D1D1","bold":false,"italic":false}]

tellraw @s [{"text":"▊ ","color":"dark_aqua","bold":true,"italic":false},{"text":" ","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_aqua","bold":true,"italic":false},{"text":"Characteristics:","color":"dark_aqua","bold":false,"italic":false,"underlined":true}]
tellraw @s [{"text":"▊ ","color":"dark_aqua","bold":true,"italic":false},{"text":"• 15 Base Oxygen Bonus","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_aqua","bold":true,"italic":false},{"text":"• 0.075 Base Movement Speed","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_aqua","bold":true,"italic":false},{"text":"• Infinite Dolphins Grace Effect","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_aqua","bold":true,"italic":false},{"text":"• Small Strength Effect When In Water","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_aqua","bold":true,"italic":false},{"text":"• Guardian Entity: Swarm of Pufferfish","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_aqua","bold":true,"italic":false},{"text":" ","color":"#D1D1D1","bold":false,"italic":false}]

tellraw @s [{"text":"▊ ","color":"dark_aqua","bold":true,"italic":false},{"text":"You can join this Heritage by giving the Token to the Villager in this room. Choose wisely! Heritages can only be changed once every month.","color":"#D1D1D1","bold":false,"italic":false}]

execute as @e[type=minecraft:interaction,tag=spawn_turtlekin_choice] if data entity @s attack at @s run data remove entity @s attack
execute as @e[type=minecraft:interaction,tag=spawn_turtlekin_choice] if data entity @s interaction at @s run data remove entity @s interaction

advancement revoke @s only eden:technical/spawn_interactions/right_turtlekin_choice