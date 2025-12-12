execute in minecraft:overworld run \
    summon text_display 0.5 75 184.5 {\
        billboard:"vertical",\
        shadow:1b,\
        Rotation:[0F,0F],\
        Tags:["realmrecrafted.spawn.grave_msg"],\
        transformation:{\
            left_rotation:[0f,0f,0f,1f],\
            right_rotation:[0f,0f,0f,1f],\
            translation:[0f,0f,0f],\
            scale:[0.65f,0.65f,0.65f]\
        },\
        text:{"color":"white","text":"When you die, a Grave will appear holding all the items you would have lost.\n\nIt remains for 10 minutes before disappearing."},\
        background:16711680\
    }