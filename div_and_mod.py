__name__ = 'B. Joel'
'''
div_and_mod
Wednesday, March 22, 2023
Prompts the user for two integers and then displays the result of multiplying or diving integer
'''

num1 = int(input('Enter an integer: '))
num2 = int(input('Enter a second integer: '))

print(num1, '/', num2, '=', int(num1/num2))
print(num1, '%', num2, '=', int(num1 % num2))
print(num2, '/', num1, '=', int(num2/num1))
print(num2, '%', num1, '=', int(num2 % num1))
