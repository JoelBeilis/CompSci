__name__ = 'B. Joel'
'''
gallon_converter
Wednesday, March 22, 2023
Prompts the user for the number of gallons
then displays the equivalent number of quarts, pints, cups, and tablespoons.
'''

gallons = int(input('Enter the number of gallons: '))
print('In', gallons, 'gallons there are:')

quarts = gallons*4
pints = quarts*2
cups = pints*2
tablespoons = cups*16

print(quarts, 'quarts')
print(pints, 'pints')
print(cups, 'cups')
print(tablespoons, 'tablespoons')
