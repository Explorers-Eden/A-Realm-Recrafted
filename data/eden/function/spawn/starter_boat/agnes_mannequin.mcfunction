execute in minecraft:overworld run \
summon mannequin 67 64.5 150.7 {\
    Rotation:[77.9F,2.3F],\
    Invulnerable:1b,\
    immovable:true,\
    hide_description:true,\
    Tags:["eden.spawn.boat"],\
    profile:"ladyagnes"\
}

execute in minecraft:overworld run \
    summon interaction 67 64.5 150.7 {\
        width:1.1f,\
        height:2.1f,\
        response:1b,\
        Tags:["eden.spawn.boat"]\
    }