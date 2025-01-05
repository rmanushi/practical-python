# bounce.py
#
# Exercise 1.5

#Variables.
ball_bounce_back_rate = 0.6

initial_height = 100

num_bounce = 0

while num_bounce < 10:
    if num_bounce == 0:
        new_height = ball_bounce_back_rate * initial_height
        num_bounce = num_bounce + 1
        print(round(new_height,4))
    else:
        new_height = new_height * ball_bounce_back_rate
        num_bounce = num_bounce + 1
        print(round(new_height,4))


