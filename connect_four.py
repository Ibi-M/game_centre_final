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
   
p1 = color.RED + "O" + color.END
p2 = color.BLUE + "O" + color.END



players = [p1,p2]
row1 = ""
row2 = ""

rows = 5
columns = [1,2,3,4,5,6]

players_row = [row1,row2]

value = " "

game = [[(value), (value),(value),(value), (value),(value),(value)],
        [(value), (value),(value),(value), (value),(value),(value)],
        [(value), (value),(value),(value), (value),(value),(value)],
        [(value), (value),(value),(value), (value),(value),(value)],
        [(value), (value),(value),(value), (value),(value),(value)],
        [(value), (value),(value),(value), (value),(value),(value)]]


def turns():
    print ((color.CYAN + color.BOLD), "    1   2   3   4   5   6   7", color.END)
    print ((color.GREEN + color.BOLD), "1", color.END,("["+game[0][0]+"]"), ("["+game[0][1]+"]"), ("["+game[0][2]+"]"), ("["+game[0][3]+"]"), ("["+game[0][4]+"]"), ("["+game[0][5]+"]"),("["+game[0][6]+"]"))
    print ((color.GREEN + color.BOLD), "2", color.END,("["+game[1][0]+"]"), ("["+game[1][1]+"]"), ("["+game[1][2]+"]"), ("["+game[1][3]+"]"), ("["+game[1][4]+"]"), ("["+game[1][5]+"]"),("["+game[1][6]+"]"))
    print ((color.GREEN + color.BOLD), "3", color.END,("["+game[2][0]+"]"), ("["+game[2][1]+"]"), ("["+game[2][2]+"]"), ("["+game[2][3]+"]"), ("["+game[2][4]+"]"), ("["+game[2][5]+"]"),("["+game[2][6]+"]"))
    print ((color.GREEN + color.BOLD), "4", color.END,("["+game[3][0]+"]"), ("["+game[3][1]+"]"), ("["+game[3][2]+"]"), ("["+game[3][3]+"]"), ("["+game[3][4]+"]"), ("["+game[3][5]+"]"),("["+game[3][6]+"]"))
    print ((color.GREEN + color.BOLD), "5", color.END,("["+game[4][0]+"]"), ("["+game[4][1]+"]"), ("["+game[4][2]+"]"), ("["+game[4][3]+"]"), ("["+game[4][4]+"]"), ("["+game[4][5]+"]"),("["+game[4][6]+"]"))
    print ((color.GREEN + color.BOLD), "6", color.END,("["+game[5][0]+"]"), ("["+game[5][1]+"]"), ("["+game[5][2]+"]"), ("["+game[5][3]+"]"), ("["+game[5][4]+"]"), ("["+game[5][5]+"]"),("["+game[5][6]+"]"))



   

print("Welcome to Connect Four!")
print("Player 1 will be RED and Player 2 will be BLUE")

end = False
while end == False:
    fine = False

    while fine != True:
        try:
            print("Player 1: Choose a column (1-7)")
            row1 = int(input()) - 1  
            if row1 > 6:
                print ("You have entered outside the range!")
                print ("")
            else:
                fine = True
        except ValueError:
            print ("Only input a number for a row, not a string!")
            print ("")


    placed = False
    for i in range(5, -1, -1): 
        if game[i][row1] == value:  
            game[i][row1] = p1  
            placed = True
            break

    if placed == False:
        print("Column is full! Try a different column.")

    turns() 

    if game[i][row1] and game[i-1][row1] and game[i-2][row1] and game[i-3][row1] == p1:
        print ("You have won!")
        end = True
    
    if row1 == 1 or 2 or 3 or 4:
        for c in columns:
            if game[c][row1] and game[c][row1 + 1] and game[c][row1+ 2] and game[c][row1 + 3] == p1:
                print ("You have won!")

    fine = False

    while fine != True:
        try:
            print("Player 2: Choose a column (1-7)")
            row2 = int(input()) - 1  
            if row2 > 6:
                print ("You have entered outside the range!")
                print ("")
            else:
                fine = True
        except ValueError:
            print ("Only input a number for a row, not a string!")
            print ("")
    
    placed = False

    for i in range(5, -1, -1):
        if game[i][row2] == value:
            game[i][row2] = p2  
            placed = True
            break

    if placed == False:
        print("Column is full! Try a different column.")

    turns() 

    if game[i][row2] and game[i-1][row2] and game[i-2][row2] and game[i-3][row2] == p2:
        print ("You have won!")
        end = True