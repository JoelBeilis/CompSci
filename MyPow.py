__name__ = 'B. Joel'

'''
MyPow
Friday, March 31, 2023
Prompt the user for two numbers and then display the result from the formula
'''
import math

x = int(input('Enter a value for X: '))
y = int(input('Enter a value for Y: '))

formula = math.e**(y*math.log(x, math.e))

print('The result from using the formula is: ', '{:.2f}'.format(formula))
print('The result from using the math pow() method is: ', math.pow(x, y))
