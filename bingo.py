import random
import time
from colorama import *
init(autoreset=True)

class color:
    UNDERLINE = '\033[4m'

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

# Intro
print (f"{Style.BRIGHT}You are going to play Bingo!\n")
time.sleep(1)
print (f"{Style.BRIGHT}Get 3 in a row to win!\n")
time.sleep(1)
print (f"{Style.BRIGHT}You can win: vertically, horizontally or diagonally!\n")
time.sleep(1)
print (f"{Style.BRIGHT}You have 9 guesses in total!")
print (f"{Style.BRIGHT}- - - - - - - - - - - - - - - - - - - - - - - - - - \n")

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

colours = [[Fore.CYAN, Fore.BLUE, Fore.GREEN],
           [Fore.YELLOW, Fore.WHITE, Fore.YELLOW], # Colors the ticket to make readability easier
           [Fore.GREEN, Fore.BLUE, Fore.CYAN]]


def print_ticket(ticket): #Procedure - Prints the player ticket
    column_width = 15

    print (f"{(colours[0][0] + ticket[0][0]).center(column_width)} | {(colours[0][1] + ticket[0][1]).center(column_width)} | {(colours[0][2] + ticket[0][2]).center(column_width)}")
    print (f"{(colours[1][0] + ticket[1][0]).center(column_width)} | {(colours[1][1] + ticket[1][1]).center(column_width)} | {(colours[1][2] + ticket[1][2]).center(column_width)}")
    print (f"{(colours[2][0] + ticket[2][0]).center(column_width)} | {(colours[2][1] + ticket[2][1]).center(column_width)} | {(colours[2][2] + ticket[2][2]).center(column_width)}")


finish = False
guesses = 9

def output():
     print (f"{Style.BRIGHT + Fore.GREEN + color.UNDERLINE}You have won!")  

while finish == False and guesses != 0: # Game Loop
    guesses = guesses - 1
    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
            if 1 <= guess <= 20:
                break
            else:
                print(f"\n{Fore.RED}Please enter a number between 1 and 20.\n")
        except ValueError:
            print(f"\n{Fore.RED} Invalid input. Please enter a number between 1 and 20.\n")

    if guess in ans:
        print(f"\n{Fore.GREEN} Correct!\n")
        place = ans.index(guess)
        row = place // 3
        col = place % 3
        guess = str(guess)
        ticket[row][col] = guess

        print_ticket(ticket) 

        # ------------------ CHECKING OF HORIZONTAL ------------------

        if ticket[0][0] == str(solutions[0][0]) and ticket[0][1] == str(solutions[0][1]) and ticket[0][2] == str(solutions[0][2]):
            finish = True
            output()

        elif ticket[1][0] == str(solutions[1][0]) and ticket[1][1] == str(solutions[1][1]) and ticket[1][2] == str(solutions[1][2]):
            finish = True
            output()

        elif ticket[2][0] == str(solutions[2][0]) and ticket[2][1] == str(solutions[2][1]) and ticket[2][2] == str(solutions[2][2]):
            finish = True
            output()

        # ------------------ CHECKING OF VERTICAL ------------------       

        elif ticket[0][0] == str(solutions[0][0]) and ticket[1][0] == str(solutions[1][0]) and ticket[2][0] == str(solutions[2][0]):
            finish = True
            output()

        elif ticket[0][1] == str(solutions[0][1]) and ticket[1][1] == str(solutions[1][1]) and ticket[2][1] == str(solutions[2][1]):
            finish = True
            output()

        elif ticket[0][2] == str(solutions[0][2]) and ticket[1][2] == str(solutions[1][2]) and ticket[2][2] == str(solutions[2][2]):
            finish = True
            output()

        # ------------------ CHECKING OF DIAGONAL ------------------

        elif ticket[0][0] == str(solutions[0][0]) and ticket[1][1] == str(solutions[1][1]) and ticket[2][2] == str(solutions[2][2]):
            finish = True
            output()

        elif ticket[0][2] == str(solutions[0][2]) and ticket[1][1] == str(solutions[1][1]) and ticket[2][0] == str(solutions[2][0]):
            finish = True
            output()

    else: # If no matches have been found
        print (f"{Fore.RED + Style.BRIGHT} Incorrect!\n")

if guesses == 0: # If player has run out of guesses
    print (Fore.RED + Style.BRIGHT + color.UNDERLINE + "You have lost!")
    print ("\nThe numbers were:\n")
    print (solutions)