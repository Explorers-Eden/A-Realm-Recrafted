advancement revoke @s only eden:starter_boat/left_click
advancement revoke @s only eden:starter_boat/right_click

playsound minecraft:entity.chicken.egg neutral @s ~ ~ ~ .5 2
execute if score @s eden.spawn.starter_boat matches 1.. run return run tellraw @s "LadyAgnes: I already gave you a starter boat!"

loot spawn ~ ~ ~ loot eden:item/starter_boat
tellraw @s "LadyAgnes: Off you go! Have Fun exploring!"

scoreboard players set @s eden.spawn.starter_boat 1