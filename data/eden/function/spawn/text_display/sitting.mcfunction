execute in minecraft:overworld run \
    summon text_display -11 75.25 129 {\
        billboard:"fixed",\
        shadow:1b,\
        Rotation:[-45F,0F],\
        transformation:{\
            left_rotation:[0f,0f,0f,1f],\
            right_rotation:[0f,0f,0f,1f],\
            translation:[0f,0f,0f],\
            scale:[.65f,.65f,.65f]\
        },\
        text:{"text":"Press and hold Left + Right at the same time to sit.\n\nYou can also sit down via the Quick Actions menu (Default: G)."},\
        background:16711680\
    }