execute store result score $eden.mainhand.material eden.technical run random value 1..100

execute if score $eden.mainhand.material eden.technical matches 1..44 run return run data modify storage eden:temp mob_equipment.mainhand.material set value wooden
execute if score $eden.mainhand.material eden.technical matches 45..60 run return run data modify storage eden:temp mob_equipment.mainhand.material set value iron
execute if score $eden.mainhand.material eden.technical matches 61..80 run return run data modify storage eden:temp mob_equipment.mainhand.material set value golden
execute if score $eden.mainhand.material eden.technical matches 81..94 run return run data modify storage eden:temp mob_equipment.mainhand.material set value diamond
execute if score $eden.mainhand.material eden.technical matches 95..100 run return run data modify storage eden:temp mob_equipment.mainhand.material set value netherite