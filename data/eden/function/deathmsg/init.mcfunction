advancement revoke @s only eden:technical/has_died
execute store result storage eden:temp death_msg.id int 1 run random value 1..248

function eden:deathmsg/global_msg/get_msg with storage eden:temp death_msg
function eden:deathmsg/location_msg/get_loc

data remove storage eden:temp death_msg