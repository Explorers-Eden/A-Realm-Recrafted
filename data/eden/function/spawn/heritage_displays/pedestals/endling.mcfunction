execute in minecraft:overworld positioned -215 -58 441 run summon block_display ~-0.5 ~ ~-0.5 {Passengers:[{id:"minecraft:item_display",item:{id:"minecraft:player_head",Count:1,components:{"minecraft:profile":{id:[I;2101094900,905849537,-434913699,1556670494],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDIxNmFmMjliMTlhNmZmNzUyNWQxODUzYjgxNDI3MGI4ZjA2ODU4MTBiMDg4NzBkY2UxNGJjOGYxZWE5NzQzZCJ9fX0="}]}}},item_display:"none",transformation:[0f,0f,-2f,0.5f,0f,2f,0f,1f,2f,0f,0f,0.5f,0f,0f,0f,1f]},{id:"minecraft:text_display",text:'[{"text":"CLICK FOR INFO","color":"#f5e8c9","bold":true,"italic":false,"underlined":false,"strikethrough":false,"obfuscated":false,"font":"minecraft:uniform"}]',text_opacity:255,background:0,alignment:"center",line_width:210,default_background:false,transformation:[0f,0f,0.4f,1.0625f,0f,0.4f,0f,0.875f,-0.4f,0f,0f,0.5f,0f,0f,0f,1f],shadow:1b}]}
execute in minecraft:overworld positioned -215 -56.5 441 run summon item_display ~ ~ ~ {billboard:"vertical",Passengers:[{id:"minecraft:text_display",billboard:"vertical",shadow:1b,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,.3f,0f],scale:[.6f,.6f,.6f]},text:{"bold":false,"color":"#f5e8c9","italic":false,"text":"Endling"},background:16711680}],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[.6f,.6f,.6f]},item:{id:"minecraft:ender_eye",count:1}}
execute in minecraft:overworld positioned -215 -58 441 run setblock ~ ~ ~ barrier
execute in minecraft:overworld positioned -215 -57 441 run setblock ~ ~ ~ light[level=13]
execute in minecraft:overworld positioned -215 -58 441 run summon interaction ~ ~ ~ {width:1.2f,height:2.2f,Tags:["spawn_endling_display"]}