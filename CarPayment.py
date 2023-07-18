__name__ = 'B. Joel'

'''
CarPayment
Friday, March 31, 2023
Calculates a monthly car payment after prompting the user for the principal owing, the interest rate,
and the number of monthly payments.
'''

principal = float(input('Principle: '))
rate = float(input('Interest Rate: '))
monthly = float(input('Number of monthly payments: '))

x = rate/12

payment = (principal*x) / (1-(1+x)**-monthly)

print('The monthly payment is: ${:.2f}'. format(payment))
