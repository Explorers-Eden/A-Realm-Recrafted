execute if items entity @p[distance=..8] weapon.mainhand minecraft:trial_key[minecraft:custom_data={item:key_golem}] unless items entity @p[distance=..8] weapon.offhand minecraft:trial_key[minecraft:custom_data={item:key_golem}] run data modify block ~ ~ ~ config.key_item.components set from entity @p[distance=..8] SelectedItem.components
execute if items entity @p[distance=..8] weapon.mainhand minecraft:trial_key[minecraft:custom_data={item:key_golem}] if items entity @p[distance=..8] weapon.offhand minecraft:trial_key[minecraft:custom_data={item:key_golem}] run data modify block ~ ~ ~ config.key_item.components set from entity @p[distance=..8] SelectedItem.components
execute unless items entity @p[distance=..8] weapon.mainhand minecraft:trial_key[minecraft:custom_data={item:key_golem}] if items entity @p[distance=..8] weapon.offhand minecraft:trial_key[minecraft:custom_data={item:key_golem}] run data modify block ~ ~ ~ config.key_item.components set from entity @p[distance=..8] Inventory[{Slot:-106b}].components

execute unless block ~ ~ ~ minecraft:vault run kill @n[type=item,tag=key_golem_vault]
execute unless block ~ ~ ~ minecraft:vault run kill @s