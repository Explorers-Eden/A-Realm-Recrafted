execute store result score $eden.treasure_pig.type eden.technical run random value 1..3

execute if score $eden.treasure_pig.type eden.technical matches 1 at @s run summon pig ~ ~ ~ {Tags:["eden.treasure_pig","eden.scaled"],PersistenceRequired:1b,Health:50f,Saddle:0b,attributes:[{id:"minecraft:max_absorption",base:2},{id:"minecraft:max_health",base:50},{id:"minecraft:movement_speed",base:0.4}],Passengers:[{id:"minecraft:item_display",Passengers:[{id:"minecraft:area_effect_cloud",Duration:18000,Tags:["eden.treasure_pig.timer"]}],view_range:48f,Tags:["eden.treasure_pig.head"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,.57f,-0.05f],scale:[2f,1.2f,1.4f]},item:{id:"minecraft:player_head",count:1,components:{profile:{name:"treasure",properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDhjMWUxYzYyZGM2OTVlYjkwZmExOTJkYTZhY2E0OWFiNGY5ZGZmYjZhZGI1ZDI2MjllYmZjOWIyNzg4ZmEyIn19fQ=="}]}}}}]}
execute if score $eden.treasure_pig.type eden.technical matches 2 at @s run summon pig ~ ~ ~ {Tags:["eden.treasure_pig","eden.scaled"],PersistenceRequired:1b,Health:50f,Saddle:0b,attributes:[{id:"minecraft:max_absorption",base:2},{id:"minecraft:max_health",base:50},{id:"minecraft:movement_speed",base:0.4}],Passengers:[{id:"minecraft:item_display",Passengers:[{id:"minecraft:area_effect_cloud",Duration:18000,Tags:["eden.treasure_pig.timer"]}],view_range:48f,Tags:["eden.treasure_pig.head"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,.57f,-0.05f],scale:[2f,1.2f,1.4f]},item:{id:"minecraft:player_head",count:1,components:{profile:{name:"treasure",properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzhmODhiMTYxNzYzZjYyZTRjNTFmNWViMWQzOGZhZjNiODJjNDhhODM5YWMzMTcxMjI5NTU3YWRlNDI3NDM0In19fQ=="}]}}}}]}
execute if score $eden.treasure_pig.type eden.technical matches 3 at @s run summon pig ~ ~ ~ {Tags:["eden.treasure_pig","eden.scaled"],PersistenceRequired:1b,Health:50f,Saddle:0b,attributes:[{id:"minecraft:max_absorption",base:2},{id:"minecraft:max_health",base:50},{id:"minecraft:movement_speed",base:0.4}],Passengers:[{id:"minecraft:item_display",Passengers:[{id:"minecraft:area_effect_cloud",Duration:18000,Tags:["eden.treasure_pig.timer"]}],view_range:48f,Tags:["eden.treasure_pig.head"],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,.57f,-0.05f],scale:[2f,1.2f,1.4f]},item:{id:"minecraft:player_head",count:1,components:{profile:{name:"treasure",properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGNjNzk5NTRkMzUwYTk4YzcyMTcyNTY4MzFmNjVjNjJhNDI4MDc0YjZlNGFlOWVlZGU3YTQ0ZjlkZTRhNyJ9fX0="}]}}}}]}

kill @s