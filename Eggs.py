__name__ = 'B. Joel'

'''
Eggs
Friday, March 31, 2023
Prompts the user for the number of eggs, and then calculates the bill.
'''

eggs = int(input("Please enter the amount of eggs you have: "))

if 0 < eggs < 48:
    dozen = int(eggs) // 12
    dozenPrice = float(dozen) * 0.50
    extra = float(eggs) % 12
    extraPrice = float(extra)*((1/12)*0.50)
    total = float(dozenPrice) + float(extraPrice)
    print("Your total is ", total)

elif eggs < 72:
    dozen = int(eggs) // 12
    dozenPrice = float(dozen) * 0.45
    extra = float(eggs) % 12
    extraPrice = float(extra)*((1/12)*0.45)
    total = float(dozenPrice) + int(extraPrice)
    print("Your total is ", total)

elif eggs < 132:
    dozen = int(eggs) // 12
    dozenPrice = float(dozen) * 0.40
    extra = float(eggs) % 12
    extraPrice = float(extra)*((1/12)*0.40)
    total = float(dozenPrice) + int(extraPrice)
    print("Your total is ", total)

else:
    dozen = int(eggs) // 12
    dozenPrice = float(dozen) * 0.35
    extra = float(eggs) % 12
    extraPrice = float(extra)*((1/12)*0.35)
    total = float(dozenPrice) + int(extraPrice)
    print("Your total is ", total)
