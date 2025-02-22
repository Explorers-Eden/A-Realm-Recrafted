advancement revoke @s only heritages:used_horn_dunesworn
advancement revoke @s only heritages:used_horn_endling
advancement revoke @s only heritages:used_horn_frostborne
advancement revoke @s only heritages:used_horn_moonshroud
advancement revoke @s only heritages:used_horn_netherian
advancement revoke @s only heritages:used_horn_oakhearted
advancement revoke @s only heritages:used_horn_orebringer
advancement revoke @s only heritages:used_horn_turtlekin

execute if predicate eden:entity/max_2_level run return run title @s actionbar [{"bold":false,"color":"white","italic":false,"text":"- "},{"bold":false,"color":"red","italic":false,"text":"3 EXP Levels Needed"},{"bold":false,"color":"white","italic":false,"text":" -"}]

execute if score @s heritages.guardians.on_cooldown matches 1.. run return fail

data modify storage eden:temp heritages.uuid.0 set from entity @s UUID[0]
data modify storage eden:temp heritages.uuid.1 set from entity @s UUID[1]
data modify storage eden:temp heritages.uuid.2 set from entity @s UUID[2]
data modify storage eden:temp heritages.uuid.3 set from entity @s UUID[3]

execute as @s[tag=dunesworn] run function heritages:dunesworn/guardian with storage eden:temp heritages.uuid
execute as @s[tag=endling] run function heritages:endling/guardian with storage eden:temp heritages.uuid
execute as @s[tag=moonshroud] run function heritages:moonshroud/guardian with storage eden:temp heritages.uuid
execute as @s[tag=netherian] run function heritages:netherian/guardian with storage eden:temp heritages.uuid
execute as @s[tag=oakhearted] run function heritages:oakhearted/guardian with storage eden:temp heritages.uuid
execute as @s[tag=orebringer] run function heritages:orebringer/guardian with storage eden:temp heritages.uuid
execute as @s[tag=turtlekin] run function heritages:turtlekin/guardian with storage eden:temp heritages.uuid
execute as @s[tag=frostborne] run function heritages:frostborne/guardian with storage eden:temp heritages.uuid

particle minecraft:trial_spawner_detection_ominous ~ ~.3 ~ .5 .5 .5 0 50
scoreboard players set @s heritages.guardians.on_cooldown 1
scoreboard players set @s heritages.guardians 180
experience add @s -3 levels