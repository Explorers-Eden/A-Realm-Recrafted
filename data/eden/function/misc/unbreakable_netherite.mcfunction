execute as @a if items entity @s weapon.mainhand #eden:netherite_equipment run item modify entity @s weapon.mainhand eden:unbreakable
execute as @a if items entity @s weapon.offhand #eden:netherite_equipment run item modify entity @s weapon.offhand eden:unbreakable

execute as @a if items entity @s armor.feet #eden:netherite_equipment run item modify entity @s armor.feet eden:unbreakable
execute as @a if items entity @s armor.legs #eden:netherite_equipment run item modify entity @s armor.legs eden:unbreakable
execute as @a if items entity @s armor.chest #eden:netherite_equipment run item modify entity @s armor.chest eden:unbreakable
execute as @a if items entity @s armor.head #eden:netherite_equipment run item modify entity @s armor.head eden:unbreakable

schedule function eden:misc/unbreakable_netherite 3s