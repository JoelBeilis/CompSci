__name__ = 'B. Joel'

'''
Printing
Friday, March 31, 2023
prompts the user for the number of copies to print and then displays the price per copy and the total price for the job
'''

copy = int(input('Enter the number of copies needed to print: '))

if 0 < copy < 100:
    price = 0.3
elif copy < 500:
    price = 0.28
elif copy < 750:
    price = 0.27
elif copy < 1001:
    price = 0.26
else:
    price = 0.25

cost = "${:.2f}".format(price*copy)

print('Price per copy is: $', price)
print('Total cost is:', cost)
