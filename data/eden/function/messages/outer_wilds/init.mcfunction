schedule function eden:messages/outer_wilds/init 30s

execute as @a[tag=!at_outer_wilds] at @s unless predicate eden:location/in_permament_area run function eden:messages/outer_wilds/entered
execute as @a[tag=at_outer_wilds] at @s if predicate eden:location/in_permament_area run function eden:messages/outer_wilds/exited