__name__ = 'B. Joel'
'''
pizza_cost
Wednesday, March, 22, 2023
Prompts user for a requested pizza size and outputs the cost
'''

diameter = float(input('Enter the diameter of the pizza in inches: '))
cost = 0.75+1.00+0.05*diameter*diameter
print('The cost of making the pizza is: $', round(cost, 2))
