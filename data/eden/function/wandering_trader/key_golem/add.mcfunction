execute store result score $smptrade eden.technical run random value 1..2

$execute if score $smptrade eden.technical matches 1 run data modify entity @s Offers.Recipes prepend value {maxUses:1,buy:{id:"minecraft:emerald",count:32},sell:{id:"minecraft:trial_key",count:1,components:$(key_golem)}}
$execute if score $smptrade eden.technical matches 2 run data modify entity @s Offers.Recipes prepend value {maxUses:1,buy:{id:"minecraft:diamond",count:2},sell:{id:"minecraft:trial_key",count:1,components:$(key_golem)}}

say key