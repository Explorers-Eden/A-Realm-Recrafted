item replace block ~ ~ ~ container.22 with minecraft:player_head[custom_name='{"bold":false,"fallback":"This Waypoint:","italic":false,"translate":"gui.eden.waypoint_hub.this_waypoint"}',custom_data={wawo:waypoint_gui_item},profile={id:[I;1731215105,-1235661595,-2029603293,-1586750030],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvY2Y3Y2RlZWZjNmQzN2ZlY2FiNjc2YzU4NGJmNjIwODMyYWFhYzg1Mzc1ZTlmY2JmZjI3MzcyNDkyZDY5ZiJ9fX0="}]}]
$item modify block ~ ~ ~ container.22 [{"function":"minecraft:set_lore","entity":"this","lore":[[{"text":"X: ","color":"dark_gray","bold":false,"italic":false},{"nbt":"waypoints.$(entry_id).pos.x","storage":"eden:waypoint_db","color":"gray","bold":false,"italic":false},{"text":" | Y: ","color":"dark_gray","bold":false,"italic":false},{"nbt":"waypoints.$(entry_id).pos.y","storage":"eden:waypoint_db","color":"gray","bold":false,"italic":false},{"text":" | Z: ","color":"dark_gray","bold":false,"italic":false},{"nbt":"waypoints.$(entry_id).pos.z","storage":"eden:waypoint_db","color":"gray","bold":false,"italic":false}],[{"translate":"gui.eden.waypoint_hub.dimension","fallback":"Dimension: ","color":"dark_gray","bold":false,"italic":false},{"nbt":"waypoints.$(entry_id).dimension_name","storage":"eden:waypoint_db","color":"gray","bold":false,"italic":false}],[{"text":"  "}],[{"translate":"gui.eden.waypoint_hub.owner","fallback":"Owner: ","color":"dark_gray","bold":false,"italic":false},{"nbt":"waypoints.$(entry_id).profile.name","storage":"eden:waypoint_db","color":"gray","bold":false,"italic":false},{"text":" | ID: ","color":"dark_gray","bold":false,"italic":false},{"nbt":"waypoint.entry_id","storage":"eden:temp","color":"gray","bold":false,"italic":false}]],"mode":"replace_all"}]
