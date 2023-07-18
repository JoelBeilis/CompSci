__name__ = 'B. Joel'
'''
penny_pitch
Friday, May 26, 2023
Creates a table with 5 different prizes if 3 pennies land on 1 prize you win. To stop playing input QUIT. 
'''

import random

# Function to create a random board with prizes
def create_board():
    prizes = ['PUZZLE', 'GAME', 'BALL', 'POSTER', 'DOLL']
    board = [['   ' for _ in range(5)] for _ in range(5)]
    prize_counts = {prize: 0 for prize in prizes}

    for reward in prizes:
        for _ in range(3):
            while True:
                row = random.randint(0, 4)
                col = random.randint(0, 4)
                if board[row][col] == '   ':
                    board[row][col] = '{}'.format(reward)
                    prize_counts[reward] += 1
                    break
    return board, prize_counts

# Function to simulate penny pitches
def penny_pitches(board):
    prizes_won = []

    for _ in range(10):
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            if board[row][col].count('*') < 3:
                board[row][col] += '*'
                break

    for row in board:
        for col in row:
            if col.count('*') >= 3:
                reward = col.strip('*')
                if reward not in prizes_won:
                    prizes_won.append(reward)

    return prizes_won

while True:
    board, prize_counts = create_board()

    # Determine the maximum length of a prize string for proper spacing
    max_prize_length = max([len(reward) for reward in prize_counts.keys()])

    print('\nInitial Board:')
    for row in board:
        print('| {} |'.format(' | '.join([cell.center(max_prize_length + 2) for cell in row])))

    play = input("\nEnter 'QUIT' to end the game or press any key to play again: ")
    if play == "QUIT":
        break

    prizes_won = penny_pitches(board)

    print('\nFinal Board:')
    for row in board:
        print('| {} |'.format(' | '.join([cell.center(max_prize_length + 2) for cell in row])))

    if prizes_won:
        print('\nYou Won:')
        for reward in prizes_won:
            print(reward)
    else:
        print('\nYou did not win. :(')