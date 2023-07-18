__name__ = 'B. Joel'

'''
BacteriaGrowth
Friday, March 31, 2023
Prompt the user for initial bacteria, the constant k, and the time. 
Calculates how many bacteria will be present based on this formula. 
'''

import math

bacteria = int(input('Enter initial amount of bacteria: '))
k = float(input('Enter a constant value for k: '))
hours = float(input('Enter the growth time period in hours: '))

y = bacteria * math.e**(k*hours)

print('{:.0f}'.format(y), 'bacteria will be present after', hours, 'hours.')
