data modify storage eden:temp death_msg.Pos0 set from entity @s LastDeathLocation.pos[0]
data modify storage eden:temp death_msg.Pos1 set from entity @s LastDeathLocation.pos[1]
data modify storage eden:temp death_msg.Pos2 set from entity @s LastDeathLocation.pos[2]
data modify storage eden:temp death_msg.Dimension set from entity @s LastDeathLocation.dimension

execute if data storage eden:temp death_msg{Dimension: "minecraft:overworld"} run data modify storage eden:temp death_msg.Dimension set value "Overworld"
execute if data storage eden:temp death_msg{Dimension: "minecraft:the_end"} run data modify storage eden:temp death_msg.Dimension set value "The End"
execute if data storage eden:temp death_msg{Dimension: "minecraft:the_nether"} run data modify storage eden:temp death_msg.Dimension set value "The Nether"
execute if data storage eden:temp death_msg{Dimension: "eden:astral_plane"} run data modify storage eden:temp death_msg.Dimension set value "Astral Plane"
execute if data storage eden:temp death_msg{Dimension: "kattersstructures:deep_blue"} run data modify storage eden:temp death_msg.Dimension set value "Deep Blue"

function eden:deathmsg/location_msg/send_msg