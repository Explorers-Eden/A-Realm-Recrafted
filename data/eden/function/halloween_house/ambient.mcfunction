schedule function eden:halloween_house/ambient 3s

execute in minecraft:overworld if predicate {"condition": "minecraft:random_chance","chance": 0.33} run particle minecraft:soul 205.52 90.00 -771.50 20 20 20 0 100
execute in minecraft:overworld if predicate {"condition": "minecraft:random_chance","chance": 0.33} run playsound minecraft:entity.warden.heartbeat master @a 205.53 82.00 -771.58 1 0.1