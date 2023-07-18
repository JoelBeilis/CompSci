__name__ = 'B. Joel'
'''
Change
Wednesday, March 22, 2023
User enters an amount in cents and then displays the minimum number of coins necessary to make the change.
'''

change = int(input('Enter the change in cents: '))
Quarters = 25
Dimes = 10
Nickels = 5

numberQ = int((change - (change % Quarters))/Quarters)
change = change % Quarters

numberD = int((change - (change % Dimes))/Dimes)
change = change % Dimes

numberN = int((change - (change % Nickels))/Nickels)

pennies = int(change % Nickels)
print('Quarters: ', numberQ)
print('Dimes: ', numberD)
print('Nickels: ', numberN)
print('Pennies: ', pennies)
