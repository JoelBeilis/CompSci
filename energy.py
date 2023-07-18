__name__ = 'B. Joel'
'''
energy
Wednesday, March 22, 2023
User enters a mass in kg and program outputs the number of light bulbs tht can be powered 
'''

mass = float(input('Enter the mass in kilograms (kg): '))
energy = mass*9*10**16
bulbs = energy/360000
print('The energy produced in Joules is = ', energy)
print('The number of 100-watt light bulbs powered = ', round(bulbs, 1))
