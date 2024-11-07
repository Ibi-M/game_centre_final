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

def progress():
    column_width = 10
    print (color.BOLD + color.UNDERLINE + " ".center(column_width) + "|" +"1".center(column_width) + "|" + "2".center(column_width) + "|" + "3".center(column_width) + "|" + "4".center(column_width) + "|" +"5".center(column_width) + color.END)
    print (color.BOLD +"1".center(column_width) + color.END + "|" + player[0][0].center(column_width) + "|" + player[0][1].center(column_width) + "|" + player[0][2].center(column_width) + "|" + player[0][3].center(column_width) + "|" + player[0][4].center(column_width))
    print (color.BOLD +"2".center(column_width) + color.END + "|" + player[1][0].center(column_width) + "|" + player[1][1].center(column_width) + "|" + player[1][2].center(column_width) + "|" + player[1][3].center(column_width) + "|" + player[1][4].center(column_width))
    print (color.BOLD +"3".center(column_width) + color.END + "|" + player[2][0].center(column_width) + "|" + player[2][1].center(column_width) + "|" + player[2][2].center(column_width) + "|" + player[2][3].center(column_width) + "|" + player[2][4].center(column_width))
    print (color.BOLD +"4".center(column_width) + color.END + "|" + player[3][0].center(column_width) + "|" + player[3][1].center(column_width) + "|" + player[3][2].center(column_width) + "|" + player[3][3].center(column_width) + "|" + player[3][4].center(column_width))
    print (color.BOLD +"5".center(column_width) + color.END + "|" + player[4][0].center(column_width) + "|" + player[4][1].center(column_width) + "|" + player[4][2].center(column_width) + "|" + player[4][3].center(column_width) + "|" + player[4][4].center(column_width))

def all_pairs_matched():
    for row in player:
        if "-" in row:
            return False
    return True

def get_valid_input():
    while True:
        row = int(input("Input the " + color.YELLOW + color.BOLD + color.UNDERLINE + "row" + color.END +": ")) - 1
        col = int(input("Input the " + color.GREEN + color.BOLD + color.UNDERLINE +  "column" + color.END + ": ")) - 1
        print ("")
        if player[col][row] == "-":
            return row, col
        else:
            print(color.RED + "This position is already revealed. Choose a different one." + color.END)
            print ("")


board = [["Cat","Seal","Dog","Pig","Elephant"],
         ["Fly","Elephant","Fly","Cat","Frog"],
         ["Rabbit","Giraffe","Swan","Turkey","Frog"],
         ["Dog","Pig","Bird","Bird","Swan"],
         ["Seal","Turkey","Toad","Toad","Rabbit"]]

player = [["-","-","-","-","-"],
          ["-","-","-","-","-"],
          ["-","-","-","-","-"],
          ["-","-","-","-","-"],
          ["-","-","-","-","-"]]

print (color.BOLD + color.UNDERLINE + "You are going to play the Memory Game!" + color.END)
print ("")
time.sleep(1)
print (color.BOLD + color.UNDERLINE + "There are 12 pairs in the table; with one having no pair!")
print ("")
time.sleep(1)
print (color.BOLD + color.UNDERLINE + "Guess by inputting the row and the column of the chosen place that you would like to reveal the word!" + color.END)
print ("")

pairs = 12

finish = False

while not finish:
    print ("") 
    print (color.PURPLE + "You have " + color.BOLD +  str(pairs) + " pairs remaining to guess." + color.END)
    pairs = int(pairs)
    print ("")
    print("Select the first word:")
    first_r, first_c = get_valid_input()
    player[first_c][first_r] = board[first_c][first_r]
    progress()

    print("Select the second word:")
    second_r, second_c = get_valid_input()
    player[second_c][second_r] = board[second_c][second_r]
    progress()

    if board[first_c][first_r] != board[second_c][second_r]:
        print(color.RED + "Not a match" + color.END)
        print ("")
        player[first_c][first_r] = "-"
        player[second_c][second_r] = "-"
    else:
        pairs = pairs - 1
        print(color.GREEN + "It's a match!" + color.END)
        print ("")

    if all_pairs_matched():
        print(color.BOLD + color.GREEN + "Congratulations! You matched all pairs!" + color.END)
        finish = True