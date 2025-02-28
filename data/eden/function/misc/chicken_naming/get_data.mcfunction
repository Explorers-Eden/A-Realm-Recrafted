execute as @p[distance=..25] run loot spawn ~ ~ ~ loot {"type":"minecraft:entity","pools":[{"rolls": 1,"entries":[{"type": "minecraft:item","name": "minecraft:player_head","functions":[{"function": "minecraft:fill_player_head","entity": "this"}]}]}]}
data modify storage eden:temp heritage_chicken.profile_name set from entity @n[type=item,nbt={Item:{id:"minecraft:player_head"}}] Item.components.minecraft:profile.name
kill @n[type=item,nbt={Item:{id:"minecraft:player_head"}}]

execute as @n[type=chicken,tag=!name_set,distance=..25] at @s run function eden:misc/chicken_naming/set_name with storage eden:temp heritage_chicken