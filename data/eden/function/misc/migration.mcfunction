function nice_mobs:remove/blockhead_mobs
kill @e[type=interaction,tag=eden.quest.interaction]
kill @e[type=text_display,tag=eden.quest.text]
kill @e[type=item_display,tag=eden.quest.item]
kill @e[type=pig,tag=eden.treasure_pig]
kill @e[type=area_effect_cloud,tag=eden.treasure_pig.timer]
kill @e[type=item_display,tag=eden.treasure_pig.head]

scoreboard objectives remove eden.quest.item.count
scoreboard objectives remove eden.quest.completed.count
scoreboard objectives remove eden.penguin.breathing

schedule function eden:misc/migration 11s