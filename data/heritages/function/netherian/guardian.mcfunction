title @s actionbar [{"bold":false,"color":"white","italic":false,"text":"- "},{"bold":false,"color":"dark_red","italic":false,"text":"Flame On!"},{"bold":false,"color":"white","italic":false,"text":" -"}]

$summon zombified_piglin ^ ^1 ^1.5 {Silent:1b,Invulnerable:1b,DeathLootTable:"eden:empty",Tags:["eden.equipped","eden.scaled","guardian","$(0)$(1)$(2)$(3)","eden.rarity_mob"],Passengers:[{id:"minecraft:area_effect_cloud",Duration:2400,Tags:["guardian.timer"]}],attributes:[{id:"minecraft:attack_damage",base:1},{id:"minecraft:scale",base:0.5}]}
$summon zombified_piglin ^1.5 ^1 ^1.5 {Silent:1b,Invulnerable:1b,DeathLootTable:"eden:empty",Tags:["eden.equipped","eden.scaled","guardian","$(0)$(1)$(2)$(3)","eden.rarity_mob"],Passengers:[{id:"minecraft:area_effect_cloud",Duration:2400,Tags:["guardian.timer"]}],attributes:[{id:"minecraft:attack_damage",base:1},{id:"minecraft:scale",base:0.5}]}
$summon zombified_piglin ^-1.5 ^1 ^1.5 {Silent:1b,Invulnerable:1b,DeathLootTable:"eden:empty",Tags:["eden.equipped","eden.scaled","guardian","$(0)$(1)$(2)$(3)","eden.rarity_mob"],Passengers:[{id:"minecraft:area_effect_cloud",Duration:2400,Tags:["guardian.timer"]}],attributes:[{id:"minecraft:attack_damage",base:1},{id:"minecraft:scale",base:0.5}]}

data remove storage eden:temp heritages.uuid
function heritages:guardians/set_anger