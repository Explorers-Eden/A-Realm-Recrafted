execute as @e[type=#eden:is_guardian,tag=guardian] unless data entity @s Passengers run kill @s
execute as @a at @s if entity @e[type=minecraft:pufferfish,tag=guardian,distance=..3.5] run effect clear @s minecraft:poison

execute as @a[tag=has_heritage,scores={heritages.guardians=1..}] if score @s heritages.guardians.on_cooldown matches 1 run scoreboard players remove @s heritages.guardians 1
execute as @a[tag=has_heritage,scores={heritages.guardians=..0}] run scoreboard players set @s heritages.guardians.on_cooldown 0 

schedule function heritages:guardians/run 1s
