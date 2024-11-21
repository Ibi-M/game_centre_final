class color:  # Defines all the colors used
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
   
p1 = color.RED + "O" + color.END
p2 = color.BLUE + "O" + color.END

winp1 = color.BOLD + color.RED + "O" + color.END
winp2 = color.BOLD + color.BLUE + "O" + color.END

players = [p1,p2]
row1 = ""
row2 = ""

rows = 5
columns = [0,1,2,3,4,5]

players_row = [row1,row2]
players = ["Player 1", "Player 2"]


value = " "

game = [[(value), (value),(value),(value), (value),(value),(value)],
        [(value), (value),(value),(value), (value),(value),(value)],
        [(value), (value),(value),(value), (value),(value),(value)],
        [(value), (value),(value),(value), (value),(value),(value)],
        [(value), (value),(value),(value), (value),(value),(value)],
        [(value), (value),(value),(value), (value),(value),(value)]]


def turns(): # Board which changes after each move
    print ((color.CYAN + color.BOLD), "    1   2   3   4   5   6   7", color.END)
    print ((color.GREEN + color.BOLD), "1", color.END,("["+game[0][0]+"]"), ("["+game[0][1]+"]"), ("["+game[0][2]+"]"), ("["+game[0][3]+"]"), ("["+game[0][4]+"]"), ("["+game[0][5]+"]"),("["+game[0][6]+"]"))
    print ((color.GREEN + color.BOLD), "2", color.END,("["+game[1][0]+"]"), ("["+game[1][1]+"]"), ("["+game[1][2]+"]"), ("["+game[1][3]+"]"), ("["+game[1][4]+"]"), ("["+game[1][5]+"]"),("["+game[1][6]+"]"))
    print ((color.GREEN + color.BOLD), "3", color.END,("["+game[2][0]+"]"), ("["+game[2][1]+"]"), ("["+game[2][2]+"]"), ("["+game[2][3]+"]"), ("["+game[2][4]+"]"), ("["+game[2][5]+"]"),("["+game[2][6]+"]"))
    print ((color.GREEN + color.BOLD), "4", color.END,("["+game[3][0]+"]"), ("["+game[3][1]+"]"), ("["+game[3][2]+"]"), ("["+game[3][3]+"]"), ("["+game[3][4]+"]"), ("["+game[3][5]+"]"),("["+game[3][6]+"]"))
    print ((color.GREEN + color.BOLD), "5", color.END,("["+game[4][0]+"]"), ("["+game[4][1]+"]"), ("["+game[4][2]+"]"), ("["+game[4][3]+"]"), ("["+game[4][4]+"]"), ("["+game[4][5]+"]"),("["+game[4][6]+"]"))
    print ((color.GREEN + color.BOLD), "6", color.END,("["+game[5][0]+"]"), ("["+game[5][1]+"]"), ("["+game[5][2]+"]"), ("["+game[5][3]+"]"), ("["+game[5][4]+"]"), ("["+game[5][5]+"]"),("["+game[5][6]+"]"))

def choice(check): # Displays the output of who wins
    if check == p1:
        print (color.RED + color.BOLD + "\nPlayer 1 wins!" + color.END)
    elif check == p2:
        print (color.BLUE + color.BOLD + "\nPlayer 2 wins!" + color.END)

def win(p): # Checks all the winning combos
    check = p
    # Checks the horizontal winning
    for r in range(6):
        for c in range(4):
            if game[r][c] == p and game[r][c + 1] == p and game[r][c + 2] == p and game[r][c + 3] == p:
                choice(check)
                return True
            
     # Checks the vertical winning
    for c in range(7):
        for r in range(3):
            if game[r][c] == p and game[r + 1][c] == p and game[r + 2][c] == p and game[r + 3][c] == p:
                choice(check)
                return True
            
    # Checks the Diagonal winning of bottom left to top right   
    for r in range(3):
        for c in range(4):
            if game[r][c] == p and game[r + 1][c + 1] == p and game[r + 2][c + 2] == p and game[r + 3][c + 3] == p:
                choice(check)
                return True

    # Checks the diagonal winning of bottom right to top left
    for r in range(3, 6):
        for c in range(4):
            if game[r][c] == p and game[r - 1][c + 1] == p and game[r - 2][c + 2] == p and game[r - 3][c + 3] == p:
                choice(check)
                return True
    return False

print(color.BOLD + "Welcome to Connect Four!")
print("Player 1 will be RED and Player 2 will be BLUE" + color.END)
print ("")

end = False
while end == False: # Game Loop

    # ------------------------------------------------ PLAYER 1 -------------------------------------------------- 
    fine = False
    while fine != True:
        try:
            print("Player 1: Choose a column (1-7)")
            row1 = int(input()) - 1  
            if row1 > 6:
                print (color.RED + "You have entered outside the range!" + color.END)
                print ("")
            else:
                fine = True
        except ValueError:
            print (color.RED + "Only input a number for a row, not a string!" + color.END)
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
    win(p1)

    if win (p1) == True:
        break
    print (color.BLUE + "----------------------------------------------------------------------------" + color.END)

# ------------------------------------------------ PLAYER 2 -------------------------------------------------- 
    fine = False
    while fine != True: # Loop to check for a valid input
        try:
            print("Player 2: Choose a column (1-7)")
            row2 = int(input()) - 1  
            if row2 > 6:
                print (color.RED + "You have entered outside the range!" + color.END)
                print ("")
            else:
                fine = True
        except ValueError:
            print (color.RED + "Only input a number for a row, not a string!" + color.END)
            print ("")
    
    placed = False

    for i in range(5, -1, -1):
        if game[i][row2] == value:
            game[i][row2] = p2  
            placed = True
            break

    if placed == False:
        print(color.RED + "Column is full! Try a different column." + color.END)

    turns() 
    win(p2)
    if win(p2) == True:
        break
    print (color.RED + "----------------------------------------------------------------------------" + color.END)
