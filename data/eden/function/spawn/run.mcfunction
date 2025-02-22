execute in minecraft:overworld run kill @e[type=item,x=-184,y=-46,z=447,dx=-42,dy=-15,dz=-47]

execute as @e[type=#eden:hostile,tag=spawnmob,tag=!eden.penguin] at @s run tp @e[type=#eden:hostile,distance=..64,tag=!spawnmob] ~ ~-100 ~
execute as @e[type=#eden:hostile,tag=spawnmob,tag=!eden.penguin] at @s run kill @e[type=#eden:hostile,distance=..64,tag=!spawnmob]

function eden:spawn/particles/run

schedule function eden:spawn/run 2s