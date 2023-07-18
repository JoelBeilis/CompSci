__name__ = 'B.Joel'

'''
digits_display
April 11, 2023
Prompts the user for a non-negative integer and then displays each digit on a separate line
'''

num = input("Enter a non-negative integer: ")

if not num.isdigit():
    print("Invalid input. Please enter a non-negative integer.")
else:
    for digit in num:
        print(digit)
