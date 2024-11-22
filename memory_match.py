import time

class color: # Defines all the colors used
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

def progress(): # Displays the current player progress board
    column_width = 10
    print("____________________________________________________________________")
    print(color.BOLD + color.UNDERLINE + "|" + " ".center(column_width) + "|" + color.CYAN + "1".center(column_width) + "|" + "2".center(column_width) + "|" + "3".center(column_width) + "|" + "4".center(column_width) + "|" + "5".center(column_width) + color.END)
    print(color.BOLD + color.YELLOW + "|" + "1".center(column_width) + "|" + color.END + player[0][0].center(column_width) + "|" + player[0][1].center(column_width) + "|" + player[0][2].center(column_width) + "|" + player[0][3].center(column_width) + "|" + player[0][4].center(column_width) + "|")
    print(color.BOLD + color.YELLOW + "|" + "2".center(column_width) + "|" + color.END + player[1][0].center(column_width) + "|" + player[1][1].center(column_width) + "|" + player[1][2].center(column_width) + "|" + player[1][3].center(column_width) + "|" + player[1][4].center(column_width) + "|")
    print(color.BOLD + color.YELLOW + "|" + "3".center(column_width) + "|" + color.END + player[2][0].center(column_width) + "|" + player[2][1].center(column_width) + "|" + player[2][2].center(column_width) + "|" + player[2][3].center(column_width) + "|" + player[2][4].center(column_width) + "|")
    print(color.BOLD + color.YELLOW + "|" + "4".center(column_width) + "|" + color.END + player[3][0].center(column_width) + "|" + player[3][1].center(column_width) + "|" + player[3][2].center(column_width) + "|" + player[3][3].center(column_width) + "|" + player[3][4].center(column_width) + "|")
    print(color.BOLD + color.YELLOW + "|" + "5".center(column_width) + "|" + color.END + player[4][0].center(column_width) + "|" + player[4][1].center(column_width) + "|" + player[4][2].center(column_width) + "|" + player[4][3].center(column_width) + "|" + player[4][4].center(column_width) + "|")
    print("-----------------------------------------------------------------")

def get_valid_input(prompt_row, prompt_col): # Gets a valid input from the user
    while True:
        try:
            row = int(input(prompt_row)) - 1
            col = int(input(prompt_col)) - 1
            if row < 0 or row >= 5 or col < 0 or col >= 5:
                print(color.RED + "\nInvalid position. Please choose a row and column between 1 and 5.\n" + color.END)
                continue
            if player[row][col] != "-":
                print(color.RED + "\nThis position is already revealed or guessed. Choose a different one.\n" + color.END)
                continue
            return row, col
        except ValueError:
            print(color.RED + "\nInvalid input. Please enter integers for row and column.\n" + color.END)

def all_pairs_matched(): # Checks if all pairs are matched
    for row in player:
        if "-" in row:
            return False
    return True

board = [["Cat", "Seal", "Dog", "Pig", "Elephant"],
         ["Fly", "Elephant", "Fly", "Cat", "Frog"],
         ["Rabbit", "Giraffe", "Swan", "Turkey", "Frog"],
         ["Dog", "Pig", "Bird", "Bird", "Swan"],
         ["Seal", "Turkey", "Toad", "Toad", "Rabbit"]]

player = [["-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-"],
          ["-", "-", "-", "-", "-"]]

# Intro
print(color.BOLD + color.UNDERLINE + "You are going to play the Memory Game!\n" + color.END)
time.sleep(1)
print(color.BOLD + color.UNDERLINE + "There are 12 pairs in the table; with one having no pair!\n")
time.sleep(1)
print(color.BOLD + color.UNDERLINE + "Guess by inputting the row and the column of the chosen place that you would like to reveal the word!\n" + color.END)
#------------------------
pairs = 12
finish = False

while finish != True: # Main Game Loop
    print(color.PURPLE + "You have " + color.BOLD + str(pairs) + " pairs remaining to guess.\n" + color.END)
    pairs = int(pairs)
    first_r, first_c = get_valid_input(("Input the" + color.YELLOW + " row " + color.END + "of the first word: "), ("Input the" + color.CYAN + " column " + color.END + "of the first word: "))
    player[first_r][first_c] = board[first_r][first_c]
    progress()

    second_r, second_c = get_valid_input(("\nInput the" + color.YELLOW + " row " + color.END + "of the second word: "), ("Input the" + color.CYAN + " column " + color.END + "of the second word: "))
    player[second_r][second_c] = board[second_r][second_c]
    progress()
    
    # Checks if two pairs do not match
    if board[first_r][first_c] != board[second_r][second_c]:
        print(color.RED + "Not a match" + color.END)
        
        # Checks if the extra word has been revealed in the first guess
        if board[first_r][first_c] == "Giraffe":
            player[first_r][first_c] = "Giraffe"
            print (color.YELLOW + color.BOLD + "You have revealed the extra word which has no pair!" + color.END)
        else:
            player[first_r][first_c] = "-"

        # Checks if the extra word has been revealed in the second guess
        if board[second_r][second_c] == "Giraffe":
            player[second_r][second_c] = "Giraffe"
            print (color.YELLOW + color.BOLD + "You have revealed the extra word which has no pair!" + color.END)
        else:
            player[second_r][second_c] = "-"
    else:
        pairs -= 1
        print(color.GREEN + "It's a match!" + color.END)

    if all_pairs_matched(): # For when all pairs are matched
        print(color.BOLD + color.GREEN + "\nCongratulations! You matched all pairs!\n" + color.END)
        finish = True