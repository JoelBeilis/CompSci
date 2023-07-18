__name__ = 'B. Joel'
'''
Digits
Wednesday, March 22, 2023
Outputs the digit of any entered three_digit number
'''

number = int(input('Enter a three-digit number: '))

hundreds = (number % 1000) // 100
print('The hundreds-place digit is:', hundreds)
tens = (number % 100) // 10
print('The tens-place digit is:', tens)
ones = number % 10
print('The ones-place digit is:', ones)
