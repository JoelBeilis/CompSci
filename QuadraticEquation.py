__name__ = 'B. Joel'

'''
QuadraticEquation
Friday, March 31, 2023
Quadratic Equation application that gives the solution to any quadratic equation
'''

import math

a = float(input('Enter value for a: '))
b = float(input('Enter value for b: '))
c = float(input('Enter value for c: '))

d = (b**2) - (4*a*c)
e = 2*a

x1 = (-b+math.sqrt(d))/e
x2 = (-b-math.sqrt(d))/e

roots = b**2 - 4*a*c

if roots == 0:
    print('1 real root')
elif roots > 0:
    print('2 real roots')
else:
    print('No real roots')

print('The roots are ', "{:.2f}".format(x1), 'and', "{:.2f}".format(x2))
