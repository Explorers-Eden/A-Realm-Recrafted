execute store result score $weather eden.technical run random value 1..100

execute if score $weather eden.technical matches 1..80 run weather clear 1d
execute if score $weather eden.technical matches 81..85 run weather thunder 1d
execute if score $weather eden.technical matches 86..100 run weather rain 1d