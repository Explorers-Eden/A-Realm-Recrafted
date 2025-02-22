## migrate spawners
execute as @e[type=marker,tag=nmr_amemasu_spawner_1] at @s run summon marker ~ ~ ~ {Tags:["eden.amemasu.spawner"]} 
execute as @e[type=marker,tag=nmr_amemasu_spawner_1] at @s run kill @s
execute as @e[type=marker,tag=nmr_amemasu_spawner_2] at @s run kill @s
execute as @e[type=marker,tag=nmr_boo_spawner] at @s run summon marker ~ ~ ~ {Tags:["eden.boo.spawner"]} 
execute as @e[type=marker,tag=nmr_boo_spawner] at @s run kill @s
execute as @e[type=marker,tag=nmr_penguin_spawner] at @s run summon marker ~ ~ ~ {Tags:["eden.penguin.spawner"]} 
execute as @e[type=marker,tag=nmr_penguin_spawner] at @s run kill @s
execute as @e[type=marker,tag=nmr_hedgehog_spawner] at @s run summon marker ~ ~ ~ {Tags:["eden.hedgehog.spawner"]} 
execute as @e[type=marker,tag=nmr_hedgehog_spawner] at @s run kill @s
execute as @e[type=marker,tag=nmr_hermit_crab_spawner] at @s run summon marker ~ ~ ~ {Tags:["eden.hermit_crab.spawner"]} 
execute as @e[type=marker,tag=nmr_hermit_crab_spawner] at @s run kill @s
execute as @e[type=marker,tag=nmr_ladybug_spawner] at @s run summon marker ~ ~ ~ {Tags:["eden.ladybug.spawner"]} 
execute as @e[type=marker,tag=nmr_ladybug_spawner] at @s run kill @s
execute as @e[type=marker,tag=nmr_penguin_spawner] at @s run summon marker ~ ~ ~ {Tags:["eden.penguin.spawner"]} 
execute as @e[type=marker,tag=nmr_penguin_spawner] at @s run kill @s
execute as @e[type=marker,tag=nmr_nautilus_spawner] at @s run summon marker ~ ~ ~ {Tags:["eden.nautilus.spawner"]} 
execute as @e[type=marker,tag=nmr_nautilus_spawner] at @s run kill @s
execute as @e[type=marker,tag=nmr_rats_spawner] at @s run summon marker ~ ~ ~ {Tags:["eden.rat.spawner"]} 
execute as @e[type=marker,tag=nmr_rats_spawner] at @s run kill @s
execute as @e[type=marker,tag=nmr_snail_spawner] at @s run summon marker ~ ~ ~ {Tags:["eden.snail.spawner"]} 
execute as @e[type=marker,tag=nmr_snail_spawner] at @s run kill @s

## migrate mobs
execute as @e[type=vex,tag=nmr_amemasu] run kill @s
execute as @e[type=item_display,tag=nmr_amemasu_head] run kill @s
execute as @e[type=vex,tag=nmr_boo] at @s run function blockhead_mobs:boo/spawn
execute as @e[type=vex,tag=nmr_boo] run kill @s
execute as @e[type=item_display,tag=nmr_boo_head] run kill @s
execute as @e[type=polar_bear,tag=nmr_hedgehog] at @s run function blockhead_mobs:hedgehog/spawn
execute as @e[type=polar_bear,tag=nmr_hedgehog] run kill @s
execute as @e[type=item_display,tag=nmr_hedgehog_head] run kill @s
execute as @e[type=ocelot,tag=nmr_hermit_crab] at @s run function blockhead_mobs:hermit_crab/spawn
execute as @e[type=ocelot,tag=nmr_hermit_crab] run kill @s
execute as @e[type=item_display,tag=nmr_hermit_crab_head] run kill @s
execute as @e[type=allay,tag=nmr_ladybug] at @s run function blockhead_mobs:ladybug/spawn
execute as @e[type=allay,tag=nmr_ladybug] run kill @s
execute as @e[type=item_display,tag=nmr_ladybug_head] run kill @s
execute as @e[type=axolotl,tag=nmr_nautilus] at @s run function blockhead_mobs:nautilus/spawn
execute as @e[type=axolotl,tag=nmr_nautilus] run kill @s
execute as @e[type=item_display,tag=nmr_nautilus_head] run kill @s
execute as @e[type=pillager,tag=nmr_penguin] at @s run function blockhead_mobs:penguin/spawn
execute as @e[type=pillager,tag=nmr_penguin] run kill @s
execute as @e[type=item_display,tag=nmr_penguin_head] run kill @s
execute as @e[type=interaction,tag=nmr_penguin_interaction] run kill @s
execute as @e[type=creeper,tag=nmr_rat] at @s run function blockhead_mobs:rat/spawn
execute as @e[type=creeper,tag=nmr_rat] run kill @s
execute as @e[type=item_display,tag=nmr_rat_head] run kill @s
execute as @e[type=panda,tag=nmr_snail] at @s run function blockhead_mobs:snail/spawn
execute as @e[type=panda,tag=nmr_snail] run kill @s
execute as @e[type=item_display,tag=nmr_snail_head] run kill @s

#schedule function migration:blockhead_mobs 10s