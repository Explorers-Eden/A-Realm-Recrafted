clear @s minecraft:arms_up_pottery_sherd[minecraft:custom_data={token:dunesworn}]
clear @s minecraft:ender_eye[minecraft:custom_data={token:endling}]
clear @s minecraft:powder_snow_bucket[minecraft:custom_data={token:frostborne}]
clear @s minecraft:echo_shard[minecraft:custom_data={token:moonshroud}]
clear @s minecraft:fire_charge[minecraft:custom_data={token:netherian}]
clear @s minecraft:oak_sapling[minecraft:custom_data={token:oakhearted}]
clear @s minecraft:stone_pickaxe[minecraft:custom_data={token:orebringer}]
clear @s minecraft:nautilus_shell[minecraft:custom_data={token:turtlekin}]

give @s ender_eye[item_name={"bold":false,"color":"dark_purple","italic":false,"text":"Token of an Endling"},custom_data={token:endling}] 1

execute as @s at @s run playsound minecraft:entity.chicken.egg neutral @s ~ ~ ~ .6 2
tellraw @s [{"text":"▊ ","color":"dark_purple","bold":true,"italic":false},{"text":"Legends whisper of the Endlings, the last surviving echoes of a once-great and now forgotten civilization, living on the Fringes of Reality, where the boundaries between worlds blur and twist.","color":"#D1D1D1","bold":false,"italic":false}]

tellraw @s [{"text":"▊ ","color":"dark_purple","bold":true,"italic":false},{"text":" ","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_purple","bold":true,"italic":false},{"text":"Characteristics:","color":"dark_purple","bold":false,"italic":false,"underlined":true}]
tellraw @s [{"text":"▊ ","color":"dark_purple","bold":true,"italic":false},{"text":"• 0.04 Base Gravity","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_purple","bold":true,"italic":false},{"text":"• 1.5 Base Fall Damage Multiplier","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_purple","bold":true,"italic":false},{"text":"• Infinite Trial Omen Effect","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_purple","bold":true,"italic":false},{"text":"• Small Strength Effect When In The End","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_purple","bold":true,"italic":false},{"text":"• Guardian Entity: Enderman","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"dark_purple","bold":true,"italic":false},{"text":" ","color":"#D1D1D1","bold":false,"italic":false}]

tellraw @s [{"text":"▊ ","color":"dark_purple","bold":true,"italic":false},{"text":"You can join this Heritage by giving the Token to the Villager in this room.","color":"#D1D1D1","bold":false,"italic":false},{"text":" Choose wisely! Heritages can only be changed once every month.","color":"#D1D1D1","bold":false,"italic":false}]

execute as @e[type=minecraft:interaction,tag=spawn_endling_choice] if data entity @s attack at @s run data remove entity @s attack
execute as @e[type=minecraft:interaction,tag=spawn_endling_choice] if data entity @s interaction at @s run data remove entity @s interaction

advancement revoke @s only eden:technical/spawn_interactions/right_endling_choice