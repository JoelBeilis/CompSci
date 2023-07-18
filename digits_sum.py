__name__ = 'B.Joel'

'''
digits_sum
April 11, 2023
Prompts the user for a non-negative integer and then displays the sum of the digits
'''

num = input("Enter a non-negative integer: ")
sum = 0

if not num.isdigit():
    print("Invalid input. Please enter a non-negative integer.")
else:
    for digit in num:
        sum += int(digit)
print('The sum of the digits is: ', sum)
