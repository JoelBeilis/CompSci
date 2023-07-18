__name__ = 'B. Joel'

'''
Friday, April 28, 2023
calendar
Use Zeller's rule to print a full calendar of any inputted month and year
'''

import math

def valid_month_input():
    while True:
        try:
            date = int(input('Enter a month: '))
            if 13 > date > 0:
                return date
            else:
                print('Please enter a month between 1 and 12.')
        except ValueError:
            print('Invalid Input! Try Again.')

def valid_year_input():
    while True:
        try:
            date = int(input('Enter a year: '))
            if date >= 1000:
                return date
            else:
                print('Please enter a 4 digit year.')
        except ValueError:
            print('Invalid Input! Try Again.')

def days_in_month(month, year):
    # Determines the number of days in the month using if statements. Accounts for leap years
    if month == 1:
        return 31
    # February leap year calculations below
    elif month == 2:
        if year % 400 == 0:
            return 29
        elif year % 4 == 0 and year % 100 != 0:
            return 29
        else:
            return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31


def name_of_month(month):
    # Finds the corresponding month using if statements month name as string

    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'August'
    elif month == 9:
        return 'September'
    elif month == 10:
        return 'October'
    elif month == 11:
        return 'November'
    elif month == 12:
        return 'December'


def calendar(month, year):
    print('              {0:^9} {1:^4}                '.format(name_of_month(month), year))
    print('| Sun | Mon | Tue | Wed | Thu | Fri | Sat |')

    first_day = find_Day(1, month, year)
    last_day = days_in_month(month, year)
    day = 1

    for x in range(0, 6):
        if day > last_day:
            break

        for y in range(1, 8):
            print(' ', end='')
            if x == 0 and y > first_day or x > 0 and day <= last_day:
                print('  {0:>2} '.format(day), end='')
                day += 1
            else:
                print('     ', end='')
        print(' ')

def find_Day(day, month, year):
    if month <= 2:
        month += 10
        year -= 1
    else:
        month -= 2

    century = year // 100
    year %= 100

    formula = day + math.floor((13 * month - 1) / 5) + year + math.floor(year / 4) + math.floor(century / 4) - 2 * century
    return formula % 7

month = valid_month_input()
year = valid_year_input()
calendar(month, year)

'''
Pseudo-code (Algorithm):
Functions:

valid_month_input()
valid_year_input()
days_in_month(month, year):
name_of_month(month):
calendar(month, year):
find_Day(day, month, year)

function valid_month_input()
    loop while True:
        try:
            read date
            if 13 > date > 0:
                return date
            else:
                print "Please enter a month between 1 and 12."
        except ValueError:
            print "Invalid Input! Try Again."
    end loop

function valid_year_input()
    loop while True:
        try:
            read date
            if date >= 1000:
                return date
            else:
                print "Please enter a month between 1 and 12."
        except ValueError:
            print "Invalid Input! Try Again."
    end loop
    
def days_in_month(month, year):
    # Determines the number of days in the month using if statements. Accounts for leap years
    if month == 1:
        return 31
    # February leap year calculations below
    elif month == 2:
        if year % 400 == 0:
            return 29
        elif year % 4 == 0 and year % 100 != 0:
            return 29
        else:
            return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31


def name_of_month(month):
    # Finds the corresponding month using if statements month name as string

    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'August'
    elif month == 9:
        return 'September'
    elif month == 10:
        return 'October'
    elif month == 11:
        return 'November'
    elif month == 12:
        return 'December'


def calendar(month, year):
    print('              {0:^9} {1:^4}                '.format(name_of_month(month), year))
    print('| Sun | Mon | Tue | Wed | Thu | Fri | Sat |')

    read first_day = find_Day(1, month, year)
    read last_day = days_in_month(month, year)
    day = 1
    
    for x in range(0, 6):
        if day > last_day:
            break

        for y in range(1, 8):
            print(' ', end='')
            if x == 0 and y > first_day or x > 0 and day <= last_day:
                print('  {0:>2} '.format(day), end='')
                day += 1
            else:
                print('     ', end='')
        print(' ')

def find_Day(day, month, year):
    if month <= 2:
        month += 10
        year -= 1
    else:
        month -= 2

    century = year // 100
    year %= 100

    formula = day + math.floor((13 * month - 1) / 5) + year + math.floor(year / 4) + math.floor(century / 4) - 2 * century
    return formula % 7

read month = valid_month_input()
read year = valid_year_input()
calendar(month, year)
'''