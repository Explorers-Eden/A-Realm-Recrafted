execute in minecraft:overworld run \
    summon text_display -35.5 70.5 183.5 {\
        billboard:"fixed",\
        shadow:1b,\
        Rotation:[-90F,0F],\
        Tags:["realmrecrafted.spawn.pause_msg"],\
        transformation:{\
            left_rotation:[0f,0f,0f,1f],\
            right_rotation:[0f,0f,0f,1f],\
            translation:[0f,0f,0f],\
            scale:[0.65f,0.65f,0.65f]\
        },\
        text:{"color":"white","text":"You'll find more handy infos about items, enchantments & more in your Pause Menu (ESC)."},\
        background:16711680\
    }