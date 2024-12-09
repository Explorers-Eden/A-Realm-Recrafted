$execute if score $minute huds.calendar matches 0..9 run data modify entity @s text set value '{"bold":false,"color":"white","italic":false,"text":"$(24_hour):0$(minute)\\n$(month_name) $(day), $(year)"}'
$execute unless score $minute huds.calendar matches 0..9 run data modify entity @s text set value '{"bold":false,"color":"white","italic":false,"text":"$(24_hour):$(minute)\\n$(month_name) $(day), $(year)"}'

data remove storage eden:temp huds