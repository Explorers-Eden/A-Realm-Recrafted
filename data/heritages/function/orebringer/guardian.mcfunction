title @s actionbar [{"bold":false,"color":"white","italic":false,"text":"- "},{"bold":false,"color":"gray","italic":false,"text":"Guardian Awakened"},{"bold":false,"color":"white","italic":false,"text":" -"}]

$summon iron_golem ^ ^1 ^1.5 {Silent:1b,Invulnerable:1b,DeathLootTable:"eden:empty",Tags:["eden.scaled","guardian","$(0)$(1)$(2)$(3)","eden.rarity_mob"],Passengers:[{id:"minecraft:area_effect_cloud",Duration:2400,Tags:["guardian.timer"]}],attributes:[{id:"minecraft:attack_damage",base:4},{id:"minecraft:scale",base:.75}]}

data remove storage eden:temp heritages.uuid
function heritages:guardians/set_anger