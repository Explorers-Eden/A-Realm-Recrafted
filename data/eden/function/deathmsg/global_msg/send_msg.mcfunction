team leave @s

$tellraw @a $(global_msg)
execute at @a run playsound minecraft:entity.chicken.egg neutral @a ~ ~ ~ .6 2

execute as @s[tag=dunesworn] run team join eden.dunesworn @s
execute as @s[tag=endling] run team join eden.endling @s
execute as @s[tag=frostborne] run team join eden.frostborne @s
execute as @s[tag=moonshroud] run team join eden.moonshroud @s
execute as @s[tag=netherian] run team join eden.netherian @s
execute as @s[tag=oakhearted] run team join eden.oakhearted @s
execute as @s[tag=orebringer] run team join eden.orebringer @s
execute as @s[tag=turtlekin] run team join eden.turtlekin @s