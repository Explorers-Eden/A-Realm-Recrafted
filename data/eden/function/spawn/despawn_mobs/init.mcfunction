schedule function eden:spawn/despawn_mobs/init 3s

execute in minecraft:overworld positioned 2 76 162 as @e[type=wandering_trader,distance=..64] run function eden:spawn/despawn_mobs/exec
execute in minecraft:overworld positioned 2 76 162 as @e[type=trader_llama,distance=..64] run function eden:spawn/despawn_mobs/exec
execute in minecraft:overworld positioned 2 76 162 as @e[type=pig,distance=..64] run function eden:spawn/despawn_mobs/exec
execute in minecraft:overworld positioned 2 76 162 as @e[type=cow,distance=..64] run function eden:spawn/despawn_mobs/exec
execute in minecraft:overworld positioned 2 76 162 as @e[type=chicken,distance=..64] run function eden:spawn/despawn_mobs/exec