from colorama import *
init(autoreset=True)

class color:
    UNDERLINE = '\033[4m'

def turns(): # The Player Board
    print(f"{Fore.CYAN + Style.BRIGHT}  0 1 2")
    print(f"{Fore.GREEN + Style.BRIGHT} 0 {Fore.RESET} {game[0][0] + game[0][1] + game[0][2]}")
    print(f"{Fore.GREEN + Style.BRIGHT} 1 {Fore.RESET} {game[1][0] + game[1][1] + game[1][2]}")
    print(f"{Fore.GREEN + Style.BRIGHT} 2 {Fore.RESET} {game[2][0] + game[2][1] + game[2][2]}")
    print ("-----------------------------------------")

def player_move(player_number, symbol): # Gets a valid player input
    print(f"{Fore.YELLOW + color.UNDERLINE}Player {player_number + Fore.RESET} : Input your input")
    
    while True:
        try:
            row = int(input("\nWhat row would you want your input (0, 1, or 2)? "))
            column = int(input("What column would you want your input (0, 1, or 2)?\n"))
            if row in rows and column in rows and game[row][column] == ".":
                game[row][column] = symbol
                break
            else:
                print(f"{Fore.RED}Invalid move! Try again.\n")
        except ValueError:
            print(f"{Fore.RED}Please enter valid integers.\n")

def win(): # Checks all the winning combos
    global stop

    # ------------------- PLAYER 1: HORIZONTAL -------------------
    if game[0][0] == p1 and game[0][1] == p1 and game[0][2] == p1:
        stop = True
            
    elif game[1][0] == p1 and game[1][1] == p1 and game[1][2] == p1:
        stop = True
    
    elif game[2][0] == p1 and game[2][1] == p1 and game[2][2] == p1:
        stop = True

    # ------------------- PLAYER 1: VERTICAL -------------------
    
    elif game[0][0] == p1 and game[1][0] == p1 and game[2][0] == p1:
        stop = True
    
    elif game[0][1] == p1 and game[1][1] == p1 and game[2][1] == p1:
        stop = True

    elif game[0][2] == p1 and game[1][2] == p1 and game[2][2] == p1:
        stop = True

    # ------------------- PLAYER 1: DIAGONAL -------------------
            
    elif game[0][0] == p1 and game[1][1] == p1 and game[2][2] == p1:
        stop = True
            
    elif game[0][2] == p1 and game[1][1] == p1 and game[2][0] == p1:
        stop = True

    
    # ------------------- PLAYER 2: HORIZONTAL -------------------

    elif game[0][0] == p2 and game[0][1] == p2 and game[0][2] == p2:
        stop = True
                
    elif game[1][0] == p2 and game[1][1] == p2 and game[1][2] == p2:
        stop = True
        
    elif game[2][0] == p2 and game[2][1] == p2 and game[2][2] == p2:
        stop = True

    # ------------------- PLAYER 2: VERTICAL -------------------

    elif game[0][0] == p2 and game[1][0] == p2 and game[2][0] == p2:
        stop = True
    
    elif game[0][1] == p2 and game[1][1] == p2 and game[2][1] == p2:
        stop = True

    elif game[0][2] == p2 and game[1][2] == p2 and game[2][2] == p2:
        stop = True
    # ------------------- PLAYER 2: HORIZONTAL -------------------
        
    elif game[0][0] == p2 and game[1][1] == p2 and game[2][2] == p2:
        stop = True
        
    elif game[0][2] == p2 and game[1][1] == p2 and game[2][0] == p2:
        stop = True
    
    # If no matches are found
    else:
        stop = False
    return stop   

print (f"{Style.BRIGHT}You are going to play Noughts and Crosses with the Computer!\n")

game = [[".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]]

rows = [0, 1, 2]

stop = False

turns()
print("")

p1 = Fore.RED + "O" + Fore.RESET
p2 = Fore.BLUE + "X" + Fore.RESET

while stop == False: # Displays the correct winning player 
    player_move("1", p1)
    turns()
    win()    
    if stop:
        print("\nPlayer 1 has won!")
        break

    player_move("2", p2)
    turns()
    win()
    if stop:
        print("\nPlayer 2 has won!")
        break

print("Game Over!")