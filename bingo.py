import random
import time

class color: # Class - Defines all colors used
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Intro
print (color.BOLD + "You are going to play Bingo!\n")
time.sleep(1)
print ("Get 3 in a row to win!\n")
time.sleep(1)
print ("You can win: vertically, horizontally or diagonally!\n")
time.sleep(1)
print ("You have 9 guesses in total!")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - \n" + color.END)

ans = []

while len(ans) < 9: # Generates 10 random numbers
    num = random.randint(1, 20)
    if num not in ans:
        ans.append(num)

solutions = [[ans[0], ans[1], ans[2]],
             [ans[3], ans[4], ans[5]], # Stores all the generated answers
             [ans[6], ans[7], ans[8]]]

pos1 = "*"
pos2 = "*"
pos3 = "*"
pos4 = "*"
pos5 = "*"
pos6 = "*"
pos7 = "*"
pos8 = "*"
pos9 = "*"

ticket = [[pos1, pos2, pos3],
          [pos4, pos5, pos6], # The player's ticket
          [pos7, pos8, pos9]]

colours = [[color.DARKCYAN, color.BLUE, color.YELLOW],
           [color.PURPLE, color.GREEN, color.CYAN], # Colors the ticket to make readability easier
           [color.YELLOW, color.DARKCYAN, color.PURPLE]]


def print_ticket(ticket): #Procedure - Prints the player ticket
    column_width = 15

    print ((colours[0][0] + ticket[0][0] + color.END).center(column_width) + "|" + (colours[0][1] + ticket[0][1] + color.END).center(column_width) + "|" + (colours[0][2] + ticket[0][2] + color.END).center(column_width) )
    print ((colours[1][0] + ticket[1][0] + color.END).center(column_width) + "|" + (colours[1][1] + ticket[1][1] + color.END).center(column_width) + "|" + (colours[1][2] + ticket[1][2] + color.END).center(column_width) )
    print ((colours[2][0] + ticket[2][0] + color.END).center(column_width) + "|" + (colours[2][1] + ticket[2][1] + color.END).center(column_width) + "|" + (colours[2][2] + ticket[2][2] + color.END).center(column_width) )


finish = False
guesses = 9

while finish == False and guesses != 0: # Game Loop
    guesses = guesses - 1
    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
            if 1 <= guess <= 20:
                break
            else:
                print(color.RED + "\nPlease enter a number between 1 and 20.\n" + color.END)
        except ValueError:
            print(color.RED + "\nInvalid input. Please enter a number between 1 and 20.\n" + color.END)

    if guess in ans:
        print(color.GREEN + "\nCorrect!\n" + color.END)
        place = ans.index(guess)

        row = place // 3
        col = place % 3

        guess = str(guess)
        ticket[row][col] = guess

        print_ticket(ticket)

        # ------------------ CHECKING OF HORIZONTAL ------------------

        if ticket[0][0] == str(solutions[0][0]) and ticket[0][1] == str(solutions[0][1]) and ticket[0][2] == str(solutions[0][2]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[1][0] == str(solutions[1][0]) and ticket[1][1] == str(solutions[1][1]) and ticket[1][2] == str(solutions[1][2]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[2][0] == str(solutions[2][0]) and ticket[2][1] == str(solutions[2][1]) and ticket[2][2] == str(solutions[2][2]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        # ------------------ CHECKING OF VERTICAL ------------------       

        elif ticket[0][0] == str(solutions[0][0]) and ticket[1][0] == str(solutions[1][0]) and ticket[2][0] == str(solutions[2][0]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[0][1] == str(solutions[0][1]) and ticket[1][1] == str(solutions[1][1]) and ticket[2][1] == str(solutions[2][1]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[0][2] == str(solutions[0][2]) and ticket[1][2] == str(solutions[1][2]) and ticket[2][2] == str(solutions[2][2]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        # ------------------ CHECKING OF DIAGONAL ------------------

        elif ticket[0][0] == str(solutions[0][0]) and ticket[1][1] == str(solutions[1][1]) and ticket[2][2] == str(solutions[2][2]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[0][2] == str(solutions[0][2]) and ticket[1][1] == str(solutions[1][1]) and ticket[2][0] == str(solutions[2][0]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

    else: # If no matches have been found
        print (color.RED + color.BOLD + "Incorrect!\n" + color.END)

if guesses == 0: # If player has run out of guesses
    print (color.RED + color.BOLD + color.UNDERLINE + "You have lost!" + color.END)
    print ("\nThe numbers were:\n")
    print (solutions)