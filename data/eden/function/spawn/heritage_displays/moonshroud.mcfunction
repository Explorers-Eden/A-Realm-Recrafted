clear @s minecraft:arms_up_pottery_sherd[minecraft:custom_data={token:dunesworn}]
clear @s minecraft:ender_eye[minecraft:custom_data={token:endling}]
clear @s minecraft:powder_snow_bucket[minecraft:custom_data={token:frostborne}]
clear @s minecraft:echo_shard[minecraft:custom_data={token:moonshroud}]
clear @s minecraft:fire_charge[minecraft:custom_data={token:netherian}]
clear @s minecraft:oak_sapling[minecraft:custom_data={token:oakhearted}]
clear @s minecraft:stone_pickaxe[minecraft:custom_data={token:orebringer}]
clear @s minecraft:nautilus_shell[minecraft:custom_data={token:turtlekin}]

give @s echo_shard[item_name={"bold":false,"color":"blue","italic":false,"text":"Token of a Moonshroud"},custom_data={token:moonshroud}] 1

execute as @s at @s run playsound minecraft:entity.chicken.egg neutral @s ~ ~ ~ .6 2
tellraw @s [{"text":"▊ ","color":"blue","bold":true,"italic":false},{"text":"The Moonshroud are beings of grace and silence, their movements fluid and almost spectral. Their skin reflects the silvered hues of moonlight, and their eyes glow faintly with the pale luminescence of the lunar surface, giving them an otherworldly, ghost-like appearance.","color":"#D1D1D1","bold":false,"italic":false}]

tellraw @s [{"text":"▊ ","color":"blue","bold":true,"italic":false},{"text":" ","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"blue","bold":true,"italic":false},{"text":"Characteristics:","color":"blue","bold":false,"italic":false,"underlined":true}]
tellraw @s [{"text":"▊ ","color":"blue","bold":true,"italic":false},{"text":"• 5.5 Base Attack Speed","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"blue","bold":true,"italic":false},{"text":"• 0.7 Base Attack Damage","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"blue","bold":true,"italic":false},{"text":"• Infinite Night Vision Effect","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"blue","bold":true,"italic":false},{"text":"• Small Strength Effect When It's Night","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"blue","bold":true,"italic":false},{"text":"• Guardian Entity: 2 Wolves","color":"#D1D1D1","bold":false,"italic":false}]
tellraw @s [{"text":"▊ ","color":"blue","bold":true,"italic":false},{"text":" ","color":"#D1D1D1","bold":false,"italic":false}]

tellraw @s [{"text":"▊ ","color":"blue","bold":true,"italic":false},{"text":"You can join this Heritage by giving the Token to the Villager in this room.","color":"#D1D1D1","bold":false,"italic":false},{"text":" Choose wisely! Heritages can only be changed once every month.","color":"#D1D1D1","bold":false,"italic":false}]

execute as @e[type=minecraft:interaction,tag=spawn_moonshroud_choice] if data entity @s attack at @s run data remove entity @s attack
execute as @e[type=minecraft:interaction,tag=spawn_moonshroud_choice] if data entity @s interaction at @s run data remove entity @s interaction

advancement revoke @s only eden:technical/spawn_interactions/right_moonshroud_choice