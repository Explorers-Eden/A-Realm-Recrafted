execute as @e[type=pig,tag=!nice_mobs.base] at @s if block ~ ~0.0625 ~ minecraft:potatoes[age=7] if predicate eden:percentages/30 run setblock ~ ~0.0625 ~ minecraft:potatoes[age=0] destroy
execute as @e[type=pig,tag=!nice_mobs.base] at @s if block ~ ~0.0625 ~ minecraft:beetroots[age=3] if predicate eden:percentages/30 run setblock ~ ~0.0625 ~ minecraft:beetroots[age=0] destroy

execute as @a[predicate=eden:entity/is_riding_pig] run effect give @s minecraft:resistance 10 2 true

schedule function pig_tweaks:run 1s