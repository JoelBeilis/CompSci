__name__ = 'B. Joel'
'''
Spending
Wednesday, March 22, 2023
Prompt the user for the amount spent last month on food, clothing, entertainment, and rent, 
and then displays a table showing the percentage of expenditures in each category.
'''

print('Enter the amount spent last month on the following items:')
food = int(input('Food: '))
clothing = int(input('Clothing: '))
entertainment = int(input('Entertainment: '))
rent = int(input('Rent: '))
totalTime = food+clothing+entertainment+rent

print('Category        Budget')
print('Food:          ', round(food/totalTime*100, 2), '%')
print('Clothing:      ', round(clothing/totalTime*100, 2), '%')
print('Entertainment: ', round(entertainment/totalTime*100, 2), '%')
print('Rent:          ', round(rent/totalTime*100, 2), '%')
