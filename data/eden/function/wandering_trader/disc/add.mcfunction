execute store result score $smptrade eden.technical run random value 1..2

$execute if score $smptrade eden.technical matches 1 run data modify entity @s Offers.Recipes prepend value {maxUses:1,buy:{id:"minecraft:diamond",count:$(diamond_price)},sell:{id:"minecraft:music_disc_5",count:1,components:$(disc)}}
$execute if score $smptrade eden.technical matches 2 run data modify entity @s Offers.Recipes prepend value {maxUses:1,buy:{id:"minecraft:emerald",count:$(emerald_price)},sell:{id:"minecraft:music_disc_5",count:1,components:$(disc)}}
