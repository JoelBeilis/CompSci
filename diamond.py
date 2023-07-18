r =6
c=10

for i in range(0,r):
    for j in range(0,c):
        if j == 0 or j == c-1 and i != 0 and i != r-1:
            print('*', end='  ')
        elif i == 0 or i == r-1 and j > 0 and j < c-1:
            print('*', end='  ')
        else:
            print(end='  ')
    print()
