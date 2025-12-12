schedule function eden:spawn/particles 10t

execute in minecraft:overworld run particle minecraft:portal 26 73 185 0.35 1 0.35 0.2 15
execute in minecraft:overworld run particle minecraft:end_rod 2 80 162 10 10 10 0.0025 5 
execute in minecraft:overworld if predicate {"condition":"minecraft:random_chance","chance":0.25} run particle minecraft:note -1.58 75.00 130.01 0.1 0.1 0.1 0.1 1