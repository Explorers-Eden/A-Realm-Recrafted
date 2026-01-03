schedule function eden:spawn/despawn_mobs/init 10t

execute in minecraft:overworld positioned 2 76 162 as @e[type=#eden:despawn_at_spawn,tag=!eden.spawn_entity,distance=..96] run function eden:spawn/despawn_mobs/exec