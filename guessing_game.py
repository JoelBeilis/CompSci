__name__ = 'B.Joel'

'''
guessing_game
April 11, 2023
Program that asks the user for an integer from 1 - 50. The  program will say too high or too low
'''

import random

num = random.randint(1, 50)
guess = 0
count = 0

while True:
    count += 1
    guess = int(input('Guess a number between 1 and 50: '))
    if guess > num:
        print('Too high guess again')
    elif guess < num:
        print('Too low guess again')
    else:
        break

print('Congrats you guessed the number', num, 'in', count, 'guesses!')
