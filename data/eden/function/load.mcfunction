##del scoreboards as garbage collection
scoreboard objectives remove eden.digsite.placed
scoreboard objectives remove eden.digsite.attempts

##default technical scoreboard
scoreboard objectives add eden.technical dummy

##additional scoreboards
scoreboard objectives add rtp trigger {"text": "RTP"}
scoreboard objectives add eden.rtp.cooldown dummy
scoreboard objectives add eden.rtp.counter dummy
scoreboard objectives add eden.joined.game minecraft.custom:minecraft.leave_game
scoreboard objectives add eden.joined.key dummy
scoreboard objectives add tp_heritage_harbor trigger {"text": "Heritage Harbor"}
scoreboard objectives add eden.digsite.placed dummy
scoreboard objectives add eden.digsite.attempts dummy
scoreboard objectives add eden.digsite.age dummy
scoreboard objectives add eden.digsite.type dummy

##init schedules
schedule function eden:rtp/run 2s
schedule function eden:player_joined/run 5t
schedule function eden:spawn/run 2s
schedule function eden:misc/dirt_path_speed 3t
schedule function eden:heritage_harbor/run 2s
schedule function eden:digsites/run_clear 60s
schedule function eden:digsites/run 4t
schedule function eden:key_golem/run 3s
schedule function eden:key_golem/vault/run 9t
schedule function eden:misc/cauldron_convertible 1s
schedule function eden:wandering_trader/run 3s
schedule function eden:misc/update_material_lore 5s
schedule function eden:villager/run 9t
schedule function eden:migrate/init 11s
schedule function eden:misc/kill_entities_at_spawn 8s

##gamerules
difficulty hard
gamerule disableElytraMovementCheck true
gamerule disablePlayerMovementCheck true
gamerule doFireTick false
gamerule globalSoundEvents false
gamerule waterSourceConversion true
gamerule snowAccumulationHeight 4
gamerule lavaSourceConversion true
gamerule playersNetherPortalDefaultDelay 1
gamerule commandBlockOutput false
gamerule playersSleepingPercentage 66
gamerule announceAdvancements false
gamerule enderPearlsVanishOnDeath true
#gamerule sendCommandFeedback false