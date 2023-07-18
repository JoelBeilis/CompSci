__name__ = 'B.Joel'

'''
math_computations
April 11, 2023
User enters any non-negative value prints the sum, average (arithmetic mean), maximum, and minimum of the values entered.
'''

total = 0.0
count = 0
max_value = float('-inf')
min_value = float('inf')

while True:
    value = float(input('Enter a non-negative value: '))
    if value < 0:
        break
    total += value
    count += 1
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value

if count > 0:
    average = total / count
else:
    average = 0.0

print('Sum: ', '{:.2f}'.format(total))
print("Average: ", "{:.2f}".format(average))
print('Maximum value: ', '{:.2f}'.format(max_value))
print('Minimum value:', "{:.2f}".format(min_value))
