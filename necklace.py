__name__ = 'B.Joel'

'''
necklace
April 11, 2023
User enters 2 numbers and enters necklace number theory which prints numbers until returning to the original 2
'''

first = int(input("Enter the first single-digit integer: "))
second = int(input("Enter the second single-digit integer: "))

num1 = first
num2 = second

count = 0

print(num1, num2, end=" ")

while num1 != first or num2 != second or count == 0:
    a = (num1 + num2) % 10
    print(a, end=" ")
    count += 1
    num1 = num2
    num2 = a

print("\nNumber of steps:", count)
