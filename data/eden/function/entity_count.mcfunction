playsound minecraft:entity.chicken.egg neutral @s ~ ~ ~ .5 2

scoreboard players set $entity_count eden.technical 0
$execute at @s as @e[type=$(type),distance=..$(distance)] run scoreboard players add $entity_count eden.technical 1

$tellraw @s [{"color":"#69FF5E","text":"▊ "},{"bold":false,"color":"white","score":{"name":"$entity_count","objective":"eden.technical"}},{"color":"white","text":" Entities ($(type)) counted in a $(distance) Block radius."}]

$data modify storage eden:temp glowing set value $(glowing)
$execute at @s as @e[type=$(type),distance=..$(distance)] if data storage eden:temp {glowing:1} run effect give @s minecraft:glowing 30 1 true