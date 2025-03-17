execute store result storage eden:temp trader.smptrades.diamond_price int 1 run random value 1..10
execute store result storage eden:temp trader.smptrades.emerald_price int 1 run random value 1..64

loot spawn ~ ~ ~ loot eden:item/pool/disc
data modify storage eden:temp trader.smptrades.disc set from entity @n[type=item,distance=..2,nbt={Item:{id:"minecraft:music_disc_5"}}] Item.components
kill @n[type=item,distance=..2,nbt={Item:{id:"minecraft:music_disc_5"}}]

function eden:wandering_trader/disc/add with storage eden:temp trader.smptrades

data remove storage eden:temp trader.smptrades