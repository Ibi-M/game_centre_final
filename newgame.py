board = [["Cat","Seal","Dog","Pig","Elephant"],
         ["Fly","Elephant","Fly","Cat","Frog"],
         ["Rabbit","Giraffe","Swan","Turkey","Frog"],
         ["Dog","Pig","Bird","Bird","Swan"],
         ["Seal","Turkey","Toad","Toad","Rabbit"]]

player = [[" "," "," "," "," "],
          [" "," "," "," "," "],
          [" "," "," "," "," "],
          [" "," "," "," "," "],
          [" "," "," "," "," "]]

def progress():
    column_width = 15   
    print (player[0][0].center(column_width) + "|" + player[0][1].center(column_width) + "|" + player[0][2].center(column_width) + player[0][3].center(column_width) + "|" + player[0][4].center(column_width))
    print (player[1][0].center(column_width) + "|" + player[1][1].center(column_width) + "|" + player[1][2].center(column_width) + player[1][3].center(column_width) + "|" + player[1][4].center(column_width))
    print (player[2][0].center(column_width) + "|" + player[2][1].center(column_width) + "|" + player[2][2].center(column_width) + player[2][3].center(column_width) + "|" + player[2][4].center(column_width))
    print (player[3][0].center(column_width) + "|" + player[3][1].center(column_width) + "|" + player[3][2].center(column_width) + player[3][3].center(column_width) + "|" + player[3][4].center(column_width))
    print (player[4][0].center(column_width) + "|" + player[4][1].center(column_width) + "|" + player[4][2].center(column_width) + player[4][3].center(column_width) + "|" + player[4][4].center(column_width))

finish = False

while finish != True:

    first_r = int(input("Input the row of the first word: "))
    first_c = int(input("Input the column of the first word "))

    player[first_r][first_c] = board[first_r][first_c]

    print (player)

    second_r = int(input("Input the row of the second word: "))
    second_c = int(input("Input the column of the second word: "))

    player[second_r][second_c] = board[second_r][second_c]

    print (player)

    if board[first_r][first_c] != board[second_r][second_c]:
        print ("Not a match")
        player[first_r][first_c] = " "
        player[second_r][second_c] = " "
        print (player)
    else:
        print ("It's a match!")




