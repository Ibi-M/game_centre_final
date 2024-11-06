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

def progress():
    column_width = 10
    print (color.BOLD + color.UNDERLINE + " ".center(column_width) + "|" +"1".center(column_width) + "|" + "2".center(column_width) + "|" + "3".center(column_width) + "|" + "4".center(column_width) + "|" +"5".center(column_width) + color.END)
    print (color.BOLD +"1".center(column_width) + color.END + "|" + player[0][0].center(column_width) + "|" + player[0][1].center(column_width) + "|" + player[0][2].center(column_width) + "|" + player[0][3].center(column_width) + "|" + player[0][4].center(column_width))
    print (color.BOLD +"2".center(column_width) + color.END + "|" + player[1][0].center(column_width) + "|" + player[1][1].center(column_width) + "|" + player[1][2].center(column_width) + "|" + player[1][3].center(column_width) + "|" + player[1][4].center(column_width))
    print (color.BOLD +"3".center(column_width) + color.END + "|" + player[2][0].center(column_width) + "|" + player[2][1].center(column_width) + "|" + player[2][2].center(column_width) + "|" + player[2][3].center(column_width) + "|" + player[2][4].center(column_width))
    print (color.BOLD +"4".center(column_width) + color.END + "|" + player[3][0].center(column_width) + "|" + player[3][1].center(column_width) + "|" + player[3][2].center(column_width) + "|" + player[3][3].center(column_width) + "|" + player[3][4].center(column_width))
    print (color.BOLD +"5".center(column_width) + color.END + "|" + player[4][0].center(column_width) + "|" + player[4][1].center(column_width) + "|" + player[4][2].center(column_width) + "|" + player[4][3].center(column_width) + "|" + player[4][4].center(column_width))

finish = False

while finish != True:

    first_r = int(input("Input the row of the first word: ")) - 1
    first_c = int(input("Input the column of the first word ")) - 1

    player[first_c][first_r] = board[first_c][first_r]

    progress()

    second_r = int(input("Input the row of the second word: ")) - 1
    second_c = int(input("Input the column of the second word: ")) - 1

    player[second_c][second_r] = board[second_c][second_r]

    progress()

    if board[first_c][first_r] != board[second_c][second_r]:
        print (color.RED + "Not a match" + color.END)
        player[first_c][first_r] = "-"
        player[second_c][second_r] = "-"
    else:
        print (color.GREEN + "It's a match!" + color.END)




