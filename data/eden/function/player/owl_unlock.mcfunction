execute if entity @s[advancements={eden:first_join=false}] run return fail

pets grant @s owl

tellraw @s [{"text":"▊ ","color":"aqua"},{"text":"Welcome back, ","color":"white"},{"selector":"@s","color":"white"},{"text":"! As a token of gratitude you've been gifted an Owl pet.","color":"white"}]
playsound minecraft:entity.chicken.egg neutral @s ~ ~ ~ .6 2