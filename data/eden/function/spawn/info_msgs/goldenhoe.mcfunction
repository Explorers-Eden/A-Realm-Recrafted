execute as @s at @s run playsound minecraft:entity.chicken.egg neutral @s ~ ~ ~ .6 2

tellraw @s {"text":" ","color":"gray","bold":false,"italic":false}
tellraw @s [{"text":"▊ ","color":"aqua","bold":true,"italic":false},{"text":"Golden Hoes are the go-to tool to create a claim for all your stuff so nobody can steal from you. It also comes with the super handy ","color":"gray","bold":false,"italic":false},{"text":"/flan ","color":"green","bold":false,"italic":false},{"text":"command.","color":"gray","bold":false,"italic":false}]

execute as @e[type=minecraft:interaction,tag=spawn_goldenhoe_display] if data entity @s attack at @s run data remove entity @s attack
execute as @e[type=minecraft:interaction,tag=spawn_goldenhoe_display] if data entity @s interaction at @s run data remove entity @s interaction
advancement revoke @s only eden:technical/spawn_interactions/right_goldenhoe_display