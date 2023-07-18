import random
rows = random.randint(1,100)
columns = random.randint(1,100)

for i in range(rows):
    for j in range(columns):
        print('*', end='  ')
    print()

for r in range(rows):
    if r == 0 or r == rows - 1:
        print('* ' * columns)
    else:
        print('* ' + '  ' * (columns - 2) + '* ')
