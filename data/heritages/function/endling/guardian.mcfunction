title @s actionbar [{"bold":false,"color":"white","italic":false,"text":"- "},{"bold":false,"color":"gray","italic":false,"text":"Guardian Awakened"},{"bold":false,"color":"white","italic":false,"text":" -"}]

$summon enderman ^ ^1 ^1.5 {Silent:1b,Invulnerable:1b,DeathLootTable:"eden:empty",Tags:["eden.scaled","guardian","$(0)$(1)$(2)$(3)","eden.rarity_mob"],Passengers:[{id:"minecraft:area_effect_cloud",Duration:2400,Particle:{type:"block",block_state:"minecraft:air"},Tags:["guardian.timer"]}],attributes:[{id:"minecraft:attack_damage",base:3},{id:"minecraft:scale",base:.6}]}

data remove storage eden:temp heritages.uuid
function heritages:guardians/set_anger