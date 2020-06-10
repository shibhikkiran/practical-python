# bounce.py
#
# Exercise 1.5

drop_height = 100
bounce = 0.6
bounce_total = 0

for drop in range(10):
    bounce_height = drop_height * bounce
    bounce_total = bounce_total + bounce_height
    drop_height = bounce_height
    print(f"drop : {drop}, bounce height : {round(bounce_height, 4)}, bounce total : {round(bounce_total, 4)}")
 
