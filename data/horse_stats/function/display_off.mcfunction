scoreboard players set @s horse_stats 1

execute as @s at @s run playsound minecraft:entity.chicken.egg neutral @s ~ ~ ~ .6 2
execute unless score @s horse_stats_msg_off matches 1 run tellraw @s [{"text":"▊ ","color":"dark_aqua","bold":true,"italic":false},{"text":"Horse Stats messages have been ","color":"gray","bold":false,"italic":false},{"text":"disabled","color":"red","bold":false,"italic":false},{"text":".","color":"gray","bold":false,"italic":false}]
scoreboard players set @s horse_stats_msg_off 1
scoreboard players set @s horse_stats_msg_on 0