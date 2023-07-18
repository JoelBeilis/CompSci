__name__ = 'B. Joel'
'''
Object Height
Wednesday, March 22, 2023
Prompts user to enter a time and outputs a height in response to how high the object will be at that time
'''

time = float(input('Enter a time less than 4.5 seconds: '))
if time > 4.5:
    time = float(input('Enter a time less than 4.5 seconds: '))

height = float(100-4.9*time*time)
print('The height of the object at ', time, 'seconds is: ', round(height, 2), 'meters')
