execute in minecraft:overworld run kill @e[type=item,x=-184,y=-46,z=447,dx=-42,dy=-15,dz=-47]

execute as @e[type=#eden:hostile,tag=spawnmob,tag=!nice_mobs.base] at @s run tp @e[type=#eden:hostile,distance=..64,tag=!spawnmob] ~ ~-100 ~
execute as @e[type=#eden:hostile,tag=spawnmob,tag=!nice_mobs.base] at @s run kill @e[type=#eden:hostile,distance=..64,tag=!spawnmob]

execute in minecraft:overworld positioned -205.00 -41.46 425.51 run kill @e[type=minecraft:chicken,distance=..25]
execute in minecraft:overworld positioned -205.00 -41.46 425.51 run kill @e[type=#eden:boats,distance=..25]

function eden:spawn/particles/run

schedule function eden:spawn/run 2s