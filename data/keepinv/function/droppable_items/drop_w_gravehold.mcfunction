$summon item ~ ~.9 ~ {Age:-6000,Item:$(item)}

data remove storage eden:temp keepinv.dropped_items[0]
data modify storage eden:temp keepinv.drop.item set from storage eden:temp keepinv.dropped_items[0]

execute if data storage eden:temp keepinv.dropped_items[0] run return run function keepinv:droppable_items/drop_w_gravehold with storage eden:temp keepinv.drop