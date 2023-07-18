__name__ = 'B. Joel'
'''
simple_interest
Wednesday, March 22, 2023
User enters principle, rate, and years program calculates value after the term using simple interest.
'''

principal = float(input('Enter the principal: '))
rate = float(input('Enter the number of years: '))
years = float(input('Enter the interest rate: '))

amount = principal*(1+years*rate)

print('The value after the term is: $', amount)
