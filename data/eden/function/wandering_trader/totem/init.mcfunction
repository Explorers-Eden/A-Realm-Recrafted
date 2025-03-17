execute store result storage eden:temp trader.smptrades.diamond_price int 1 run random value 1..10
execute store result storage eden:temp trader.smptrades.emerald_price int 1 run random value 1..64

loot spawn ~ ~ ~ loot eden:item/pool/totem
data modify storage eden:temp trader.smptrades.totem set from entity @n[type=item,distance=..2,nbt={Item:{id:"minecraft:totem_of_undying"}}] Item.components
kill @n[type=item,distance=..2,nbt={Item:{id:"minecraft:totem_of_undying"}}]

function eden:wandering_trader/totem/add with storage eden:temp trader.smptrades

data remove storage eden:temp trader.smptrades