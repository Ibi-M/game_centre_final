import random
import time

class color:
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


print (color.BOLD + "You are going to play Bingo!")
time.sleep(1)
print ("")
print ("Get 3 in a row to win!")
time.sleep(1)
print ("")
print ("You can win: vertically, horizontally or diagonally!")
print ("")
time.sleep(1)
print ("You have 9 guesses in total!")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - " + color.END)
print ("")

ans = []

while len(ans) < 9:
    num = random.randint(1, 20)
    if num not in ans:
        ans.append(num)

solutions = [[ans[0], ans[1], ans[2]],
             [ans[3], ans[4], ans[5]],
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
          [pos4, pos5, pos6],
          [pos7, pos8, pos9]]

colours = [[color.DARKCYAN, color.BLUE, color.YELLOW],
           [color.PURPLE, color.GREEN, color.CYAN],
           [color.YELLOW, color.DARKCYAN, color.PURPLE]]


def print_ticket(ticket):
    column_width = 15

    print ((colours[0][0] + ticket[0][0] + color.END).center(column_width) + "|" + (colours[0][1] + ticket[0][1] + color.END).center(column_width) + "|" + (colours[0][2] + ticket[0][2] + color.END).center(column_width) )
    print ((colours[1][0] + ticket[1][0] + color.END).center(column_width) + "|" + (colours[1][1] + ticket[1][1] + color.END).center(column_width) + "|" + (colours[1][2] + ticket[1][2] + color.END).center(column_width) )
    print ((colours[2][0] + ticket[2][0] + color.END).center(column_width) + "|" + (colours[2][1] + ticket[2][1] + color.END).center(column_width) + "|" + (colours[2][2] + ticket[2][2] + color.END).center(column_width) )


finish = False
guesses = 9

while finish == False and guesses != 0:
    guesses = guesses - 1
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
            if 1 <= guess <= 20:
                break
            else:
                print ("")
                print(color.RED + "Please enter a number between 1 and 20." + color.END)
                print ("")
        except ValueError:
            print ("")
            print(color.RED + "Invalid input. Please enter a number between 1 and 20." + color.END)
            print ("")

    if guess in ans:
        print ("")
        print(color.GREEN + "Correct!" + color.END)
        print ("")
        place = ans.index(guess)

        row = place // 3
        col = place % 3

        guess = str(guess)
        ticket[row][col] = guess

        print_ticket(ticket)

        if ticket[0][0] == str(solutions[0][0]) and ticket[0][1] == str(solutions[0][1]) and ticket[0][2] == str(solutions[0][2]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[1][0] == str(solutions[1][0]) and ticket[1][1] == str(solutions[1][1]) and ticket[1][2] == str(solutions[1][2]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[2][0] == str(solutions[2][0]) and ticket[2][1] == str(solutions[2][1]) and ticket[2][2] == str(solutions[2][2]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[0][0] == str(solutions[0][0]) and ticket[1][0] == str(solutions[1][0]) and ticket[2][0] == str(solutions[2][0]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[0][1] == str(solutions[0][1]) and ticket[1][1] == str(solutions[1][1]) and ticket[2][1] == str(solutions[2][1]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[0][2] == str(solutions[0][2]) and ticket[1][2] == str(solutions[1][2]) and ticket[2][2] == str(solutions[2][2]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[0][0] == str(solutions[0][0]) and ticket[1][1] == str(solutions[1][1]) and ticket[2][2] == str(solutions[2][2]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)

        elif ticket[0][2] == str(solutions[0][2]) and ticket[1][1] == str(solutions[1][1]) and ticket[2][0] == str(solutions[2][0]):
            finish = True
            print (color.BOLD + color.UNDERLINE + "You have won!" + color.END)
    else:
        print (color.RED + color.BOLD + "Incorrect!" + color.END)
        print ("")

if guesses == 0:
    print (color.RED + color.BOLD + color.UNDERLINE + "You have lost!" + color.END)
    print ("")
    print ("The numbers were:")
    print ("")
    print (solutions)
