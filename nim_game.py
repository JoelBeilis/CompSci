__name__ = 'B. Joel'

'''
Friday, April 28, 2023
nim_game
Use of functions to repeat stone grabbing game uses random function to play for computer
'''

import random

def is_valid_entry(entry):
    # Check if the user's entry is valid.
    if entry.isdigit():
        num_stones = int(entry)
        if 0 < num_stones < 4:
            return True
        else:
            return False
    return False

def draw_stones(stones):
    # Handle the user's turn.
    print("\nCurrent number of stones:", stones)
    while True:
        entry = input("Enter the number of stones you want to take (1-3): ")
        if is_valid_entry(entry):
            return int(entry)
        else:
            print("\nPlease enter a valid number of stones! NO CHEATING.")

def computer_turn(stones):
    # Handle the computer's turn.
    cpu_stones = random.randint(1, min(stones, 3)) #uses random to generate a random number of stones to take
    print("The computer takes", cpu_stones, "stone(s).") #outputs for player how many stones were taken by computer
    return cpu_stones

# Runs game and main code below
stones = random.randint(15, 30) #uses random to choose starting number of stones for game
while stones > 0:
    user_stones = draw_stones(stones)
    stones -= user_stones
    if stones <= 0: #checks if player lost
        print("You took the last stone. You lose!")
        break
    else: #check if computer lost
        comp_stones = computer_turn(stones)
        stones -= comp_stones
        if stones <= 0:
            print("The computer took the last stone. You win!")
            break

'''
Pseudo-code (Algorithm):
Functions:

is_valid_entry(entry, stones):
draw_stones(stones):
computer_turn(stones):

function is_valid_entry(entry, max_stones):
   if entered value is a digit:
       read num_stones
       if 0 < num_stones <= stones:
           return True
   return False
end is_valid_entry

function draw_stones(stones):
    print("Current number of stones:", stones) # on a new line
    Loop while True: 
        # Get input from user and store it in entry
       if is_valid_entry(entry, stones):
           return entry as an integer
       else:
           print("Invalid entry. Please enter a valid number of stones.")
    end loop
end draw_stones(stones) 

function computer_turn(stones):
   print "Current number of stones: stones"
   num_stones = rand(1, 3)
   print "The computer takes num_stones stone(s)."
   return num_stones
end computer_turn(stones) 

**** Main Game Code ****

stones = rand(15, 30)
Loop while stones > 0:
   user_stones = user_turn(stones)
   stones -= user_stones
   if stones == 0:
       print"You took the last stone. You lose!"
       end loop
   else:
       comp_stones = computer_turn(stones)
       stones = stones - comp_stones
       if stones == 0:
           Display "The computer took the last stone. You win!"
           end loop
'''