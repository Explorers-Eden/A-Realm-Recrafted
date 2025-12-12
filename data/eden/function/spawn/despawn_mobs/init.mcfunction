schedule function eden:spawn/despawn_mobs/init 3s

execute in minecraft:overworld positioned 2 76 162 as @e[type=wandering_trader,tag=!eden.spawn_entity,distance=..64] run function eden:spawn/despawn_mobs/exec
execute in minecraft:overworld positioned 2 76 162 as @e[type=trader_llama,tag=!eden.spawn_entity,distance=..64] run function eden:spawn/despawn_mobs/exec
execute in minecraft:overworld positioned 2 76 162 as @e[type=pig,tag=!eden.spawn_entity,distance=..64] run function eden:spawn/despawn_mobs/exec
execute in minecraft:overworld positioned 2 76 162 as @e[type=cow,tag=!eden.spawn_entity,distance=..64] run function eden:spawn/despawn_mobs/exec
execute in minecraft:overworld positioned 2 76 162 as @e[type=chicken,tag=!eden.spawn_entity,distance=..64] run function eden:spawn/despawn_mobs/exec
execute in minecraft:overworld positioned 2 76 162 as @e[type=phantom,tag=!eden.spawn_entity,distance=..128] run function eden:spawn/despawn_mobs/exec
execute in minecraft:overworld positioned 2 76 162 as @e[type=#mob_manager:hostile_mobs,tag=!eden.spawn_entity,distance=..64] run function eden:spawn/despawn_mobs/exec