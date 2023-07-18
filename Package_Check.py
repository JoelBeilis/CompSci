__name__ = 'B. Joel'

'''
PackageCheck
Friday, March 31, 2023
Prompts the user for the weight of a package and its dimensions. 
Displays an appropriate message if the package does not meet the requirements
'''

weight = float(input('Enter package weight in kilograms: '))
length = float(input('Enter package length in centimeters: '))
width = float(input('Enter package width in centimeters: '))
height = float(input('Enter package height in centimeters: '))

volume = length*width*height

if volume > 100000:
    print('Package is too large')
else:
    print('Package is acceptable size')

if weight > 27:
    print('Package is too heavy')
else:
    print('Package is acceptable weight')
