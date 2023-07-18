__name__ = 'B. Joel'

'''
TrigFunctions
Friday, March 31, 2023
Prompts the user for an angle in degrees and then displays the sine, cosine, and tangent of the angle
'''
import math

degrees = int(input('Enter an angle in degrees: '))
radians = degrees*(math.pi/180)

sin = math.sin(radians)
print('{:.4f}'.format(sin))

cos = math.cos(radians)
print('{:.4f}'.format(cos))

tan = math.tan(radians)
print('{:.4f}'.format(tan))
