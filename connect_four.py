from colorama import *
init(autoreset=True)

class color:
    UNDERLINE = '\033[4m'

p1 = Fore.RED + "O" + Fore.RESET
p2 = Fore.BLUE + "O" + Fore.RESET

winp1 = Style.BRIGHT + Fore.RED + "O" + Fore.RESET
winp2 = Style.BRIGHT + Fore.BLUE + "O" + Fore.RESET

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
    print (f"{Fore.CYAN + Style.BRIGHT}     1   2   3   4   5   6   7")
    print (f"{Fore.CYAN + Style.BRIGHT} 1 {Fore.RESET} [{game[0][0]}] [{game[0][1]}] [{game[0][2]}] [{game[0][3]}] [{game[0][4]}] [{game[0][5]}] [{game[0][6]}]")
    print (f"{Fore.CYAN + Style.BRIGHT} 2 {Fore.RESET} [{game[1][0]}] [{game[1][1]}] [{game[1][2]}] [{game[1][3]}] [{game[1][4]}] [{game[1][5]}] [{game[1][6]}]") 
    print (f"{Fore.CYAN + Style.BRIGHT} 3 {Fore.RESET} [{game[2][0]}] [{game[2][1]}] [{game[2][2]}] [{game[2][3]}] [{game[2][4]}] [{game[2][5]}] [{game[2][6]}]")
    print (f"{Fore.CYAN + Style.BRIGHT} 4 {Fore.RESET} [{game[3][0]}] [{game[3][1]}] [{game[3][2]}] [{game[3][3]}] [{game[3][4]}] [{game[3][5]}] [{game[3][6]}]")
    print (f"{Fore.CYAN + Style.BRIGHT} 5 {Fore.RESET} [{game[4][0]}] [{game[4][1]}] [{game[4][2]}] [{game[4][3]}] [{game[4][4]}] [{game[4][5]}] [{game[4][6]}]")
    print (f"{Fore.CYAN + Style.BRIGHT} 6 {Fore.RESET} [{game[5][0]}] [{game[5][1]}] [{game[5][2]}] [{game[5][3]}] [{game[5][4]}] [{game[5][5]}] [{game[5][6]}]")
    
def choice(check): # Displays the output of who wins
    if check == p1:
        print (f"\n{color.RED + color.BOLD}Player 1 wins!")
    elif check == p2:
        print (f"{color.BLUE + color.BOLD} Player 2 wins!")

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

print(f"{Style.BRIGHT}Welcome to Connect Four!")
print(f"{Style.BRIGHT}Player 1 will be RED and Player 2 will be BLUE")
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
                print (f"{Fore.RED}You have entered outside the range!\n")
            else:
                fine = True
        except ValueError:
            print (f"{Fore.RED}Only input a number for a row, not a string!\n")

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
    print (f"{Fore.BLUE}----------------------------------------------------------------------------")

# ------------------------------------------------ PLAYER 2 -------------------------------------------------- 
    fine = False
    while fine != True: # Loop to check for a valid input
        try:
            print("Player 2: Choose a column (1-7)")
            row2 = int(input()) - 1  
            if row2 > 6:                   
                print (f"{Fore.RED} You have entered outside the range!")
            else:
                fine = True
        except ValueError:
            print ("Only input a number for a row, not a string!\n")
    
    placed = False

    for i in range(5, -1, -1):
        if game[i][row2] == value:
            game[i][row2] = p2  
            placed = True
            break

    if placed == False:
        print(f"{Fore.RED}Column is full! Try a different column.")

    turns() 
    win(p2)
    if win(p2) == True:
        break
    print (f"{Fore.RED}----------------------------------------------------------------------------")
