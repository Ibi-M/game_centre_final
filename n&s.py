def turns(): # The Player Board
    print((color.CYAN + color.BOLD), "   0 1 2", color.END)
    print((color.GREEN + color.BOLD), "0", color.END, game[0][0], game[0][1], game[0][2])
    print((color.GREEN + color.BOLD), "1", color.END, game[1][0], game[1][1], game[1][2])
    print((color.GREEN + color.BOLD), "2", color.END, game[2][0], game[2][1], game[2][2])
    print ("-----------------------------------------")

def player_move(player_number, symbol): # Gets a valid player input
    print(color.YELLOW + color.UNDERLINE +"Player " + player_number + color.END + ": Input your input")
    
    while True:
        try:
            row = int(input("\nWhat row would you want your input (0, 1, or 2)? "))
            column = int(input("What column would you want your input (0, 1, or 2)?\n"))
            if row in rows and column in rows and game[row][column] == ".":
                game[row][column] = symbol
                break
            else:
                print(color.RED + "Invalid move! Try again.\n" + color.END)
        except ValueError:
            print(color.RED + "Please enter valid integers.\n" + color.END)

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

class color: # Defines all colors used
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

print (color.BOLD + "You are going to play Noughts and Crosses with the Computer!" + color.END)
print ("")

game = [[".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]]

rows = [0, 1, 2]

stop = False

turns()
print("")

p1 = color.RED + "O" + color.END
p2 = color.BLUE + "X" + color.END

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