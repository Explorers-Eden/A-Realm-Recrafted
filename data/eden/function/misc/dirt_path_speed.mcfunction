execute as @a at @s if predicate eden:entity/stepping_on_dirt_path run attribute @s minecraft:movement_speed modifier add path_speed 0.1 add_multiplied_base
execute as @a at @s unless predicate eden:entity/stepping_on_dirt_path run attribute @s minecraft:movement_speed modifier remove path_speed

schedule function eden:misc/dirt_path_speed 3t