__name__ = 'B. Joel'
'''
project
Wednesday, March 22, 2023
Enter the time spent designing, coding, debugging, and testing, and then displays the percentage of time taken for each part.
'''

print('Enter the number of minutes spent on each of the following project tasks:')
designing = int(input('Designing: '))
coding = int(input('Coding: '))
debugging = int(input('Debugging: '))
testing = int(input('Testing: '))

totalTime = designing+coding+debugging+testing

print('Task        % time')
print('Designing: ', round(designing/totalTime*100, 2), '%')
print('Coding:    ', round(coding/totalTime*100, 2), '%')
print('Debugging: ', round(debugging/totalTime*100, 2), '%')
print('Testing:   ', round(testing/totalTime*100, 2), '%')
