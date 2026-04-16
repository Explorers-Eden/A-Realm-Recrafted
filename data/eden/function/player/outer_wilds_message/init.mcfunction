schedule function eden:player/outer_wilds_message/init 30s
execute if score $outer_wilds_msg eden.technical matches 30.. run scoreboard players reset $outer_wilds_msg eden.technical
scoreboard players add $outer_wilds_msg eden.technical 1

execute as @a[tag=!at_outer_wilds] at @s unless predicate eden:location/in_permament_area run function eden:player/outer_wilds_message/entered
execute as @a[tag=at_outer_wilds] at @s if predicate eden:location/in_permament_area run function eden:player/outer_wilds_message/exited

execute as @a[tag=at_outer_wilds] at @s unless predicate eden:location/in_permament_area if score $outer_wilds_msg eden.technical matches 30.. run function eden:player/outer_wilds_message/repeated_message