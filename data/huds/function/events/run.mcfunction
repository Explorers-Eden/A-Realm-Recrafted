##progress day
execute as @a at @s if score $24_hour huds.calendar matches 0 if score $minute huds.calendar matches 0 run function huds:events/new_day with storage eden:calendar global

##reset days/years lived counter if died
execute as @a[scores={huds.has_died_today=1..}] run scoreboard players set @s huds.days_lived.counter 0
execute as @a[scores={huds.has_died_today=1..}] run scoreboard players set @s huds.years_lived.counter 0

##april fools
execute as @a at @s if predicate eden:percentages/25 if score $day huds.calendar matches 1 if score $month huds.calendar matches 4 run function huds:events/april_fools

##valentines day
execute as @a at @s if predicate eden:percentages/25 if score $day huds.calendar matches 14 if score $month huds.calendar matches 2 run function huds:events/valentines_day

##halloween
execute as @e[type=#eden:valid_for_carved_pumpkin,tag=!eden.event.halloween] if score $day huds.calendar matches 31 if score $month huds.calendar matches 10 run function huds:events/halloween/equip_head

##new year's eve
execute as @a at @s if score $day huds.calendar matches 31 if score $month huds.calendar matches 12 if score $24_hour huds.calendar matches 23 if score $minute huds.calendar matches 50 run function huds:events/new_years_eve/10
execute as @a at @s if score $day huds.calendar matches 31 if score $month huds.calendar matches 12 if score $24_hour huds.calendar matches 23 if score $minute huds.calendar matches 51 run function huds:events/new_years_eve/9
execute as @a at @s if score $day huds.calendar matches 31 if score $month huds.calendar matches 12 if score $24_hour huds.calendar matches 23 if score $minute huds.calendar matches 52 run function huds:events/new_years_eve/8
execute as @a at @s if score $day huds.calendar matches 31 if score $month huds.calendar matches 12 if score $24_hour huds.calendar matches 23 if score $minute huds.calendar matches 53 run function huds:events/new_years_eve/7
execute as @a at @s if score $day huds.calendar matches 31 if score $month huds.calendar matches 12 if score $24_hour huds.calendar matches 23 if score $minute huds.calendar matches 54 run function huds:events/new_years_eve/6
execute as @a at @s if score $day huds.calendar matches 31 if score $month huds.calendar matches 12 if score $24_hour huds.calendar matches 23 if score $minute huds.calendar matches 55 run function huds:events/new_years_eve/5
execute as @a at @s if score $day huds.calendar matches 31 if score $month huds.calendar matches 12 if score $24_hour huds.calendar matches 23 if score $minute huds.calendar matches 56 run function huds:events/new_years_eve/4
execute as @a at @s if score $day huds.calendar matches 31 if score $month huds.calendar matches 12 if score $24_hour huds.calendar matches 23 if score $minute huds.calendar matches 57 run function huds:events/new_years_eve/3
execute as @a at @s if score $day huds.calendar matches 31 if score $month huds.calendar matches 12 if score $24_hour huds.calendar matches 23 if score $minute huds.calendar matches 58 run function huds:events/new_years_eve/2
execute as @a at @s if score $day huds.calendar matches 31 if score $month huds.calendar matches 12 if score $24_hour huds.calendar matches 23 if score $minute huds.calendar matches 59 run function huds:events/new_years_eve/1
execute as @a at @s if score $day huds.calendar matches 1 if score $month huds.calendar matches 1 if score $24_hour huds.calendar matches 0 if score $minute huds.calendar matches 0 run function huds:events/new_years_eve/launch_sound
execute as @a at @s if score $day huds.calendar matches 1 if score $month huds.calendar matches 1 if score $24_hour huds.calendar matches 0 if score $minute huds.calendar matches 2 run function huds:events/new_years_eve/message
execute as @a at @s if score $day huds.calendar matches 1 if score $month huds.calendar matches 1 run function huds:events/new_years_eve/effect

##día de muertos
execute as @e[type=#minecraft:undead] if score $day huds.calendar matches 2 if score $month huds.calendar matches 11 run function huds:events/muertos/buff_undead

##easter
execute as @e[type=rabbit] at @s if predicate eden:percentages/1 if score $day huds.calendar matches 1..3 if score $month huds.calendar matches 4 run function huds:events/easter/drop_egg

##friday 13th
execute if score $day huds.calendar matches 13 if score $24_hour huds.calendar matches 0 if score $minute huds.calendar matches 0 if data storage eden:calendar global{weekday: "Friday"} run weather thunder 1d

##disable Trap Skeleton Horses in Autumn
execute as @e[type=minecraft:skeleton_horse,tag=!trap_disabled] if data storage eden:calendar global{season: "Autumn"} run function huds:events/disable_trap_horse_in_autumn
