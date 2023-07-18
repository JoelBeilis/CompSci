__name__ = 'B.Joel'

'''
random_walk
April 11, 2023
Determines how many steps the person will walk before taking a step off the bridge
'''

import random

bridge_length = 1234567890
total_steps = 0
max_steps = 0

for i in range(50):
    steps = 0
    position = 0

    while abs(position) < bridge_length/2:
        steps += 1
        direction = random.randint(0, 1)
        if direction == 1:
            position += 1
        else:
            position -= 1

    total_steps += steps

    if steps > max_steps:
        max_steps = steps

avg_steps = total_steps / 50
print('Average number of steps: ', "{:.2f}".format(avg_steps))
print('Greatest number of steps: ', "{:.2f}".format(max_steps))

