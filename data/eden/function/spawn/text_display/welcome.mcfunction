execute in minecraft:overworld run \
    summon text_display 22 74.5 188.2 {\
        billboard:"fixed",\
        shadow:1b,\
        Rotation:[-135F,0F],\
        Tags:["realmrecrafted.spawn.welcome_msg"],\
        Passengers:[\
            {\
                id:"minecraft:text_display",\
                billboard:"fixed",\
                shadow:1b,\
                Rotation:[-135F,0F],\
                Tags:["realmrecrafted.spawn.welcome_msg"],\
                transformation:{\
                    left_rotation:[0f,0f,0f,1f],\
                    right_rotation:[0f,0f,0f,1f],\
                    translation:[0f,0f,0f],\
                    scale:[0.85f,0.85f,0.85f]\
                },\
                text:{"color":"white","text":"- WELCOME TO A REALM RECRAFTED -\n"},\
                background:16711680\
            }\
        ],\
        transformation:{\
            left_rotation:[0f,0f,0f,1f],\
            right_rotation:[0f,0f,0f,1f],\
            translation:[0f,-0.5f,0f],\
            scale:[0.65f,0.65f,0.65f]\
        },\
        text:{"color":"white","text":"Before you head out on your adventure, take a minute to look around the island and get familiar with the important stuff."},\
        background:16711680\
    }