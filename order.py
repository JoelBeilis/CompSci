__name__ = 'B. Joel'
'''
order
Wednesday, March 22, 2023
Program calculates the price of an order, including tax, and change
'''

burger = int(input('Enter the number of burgers: '))
fries = int(input('Enter the number of fries: '))
soda = int(input('Enter the number of sodas: '))

burger = burger*1.69
fries = fries*1.09
soda = soda*0.99
total = burger+fries+soda
tax = total*0.065
finalTotal = total+tax
print('Total before tax: $', round(total, 2))
print('Tax: $', round(tax, 2))
print('Final total: $', round(finalTotal, 2))

tendered = float(input('Enter amount tendered: '))
change = tendered-finalTotal
print('Change: $', round(change, 2))
