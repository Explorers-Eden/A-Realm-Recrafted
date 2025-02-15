execute if predicate eden:time/night_time run effect give @s minecraft:night_vision 60 0 true
execute if entity @e[type=player,tag=moonshroud,distance=1..24] run effect give @s minecraft:regeneration 10 0 true
execute if predicate eden:time/night_time run effect give @s minecraft:strength 15 0 true
execute if predicate eden:location/in_astral_plane run effect give @s minecraft:strength 15 0 true