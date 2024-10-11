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
    

game = [[".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]]

stop = False

def turns():
    print ((color.CYAN + color.BOLD), "   0 1 2", color.END)
    print ((color.GREEN + color.BOLD), "0", color.END, game[0][0], game[0][1], game[0][2])
    print ((color.GREEN + color.BOLD), "1", color.END, game[1][0], game[1][1], game[1][2])
    print ((color.GREEN + color.BOLD), "2", color.END, game[2][0], game[2][1], game[2][2])

turns()
print ("")


p1 = color.RED + "O" + color.END
p2 = color.BLUE +"X" + color.END


def check1():
    global confirm
    confirm = False
    while confirm != True:
        if game[row1][column1] != ".":
            confirm = False
            print ("You cannot do that move!")
            print ("")
            player1()
        else:
            confirm = True
            

def check2():
    global confirm
    confirm = False
    while confirm != True:
        if game[row2][column2] != ".":
            confirm = False
            print ("You cannot do that move!")
            print ("")
            player2()
        else:
            confirm = True
            
            
def player1():
    global row1
    global column1
    print (stop)
    print ("Player 1, Input your input")
    row1 = int(input("What row would you want your input (0,1 or 2)?"))
    column1 = int(input("What column would you want your input (0,1 or 2)?"))    
    check1()
    print ("")
    game [row1][column1] = p1

def player2():
    global row2
    global column2
    print (stop)
    print ("Player 2, Input your input")
    row2 = int(input("What row would you want your input (0,1 or 2)?"))
    column2 = int(input("What column would you want your input (0,1 or 2)?"))
    check2()
    print ("")
    game [row2][column2] = p2


def win():
    global stop
    if game[0][0] == p1 and game[0][1] == p1 and game[0][2] == p1:
        stop = True
            
    elif game[1][0] == p1 and game[1][1] == p1 and game[1][2] == p1:
        stop = True
    
    elif game[2][0] == p1 and game[2][1] == p1 and game[2][2] == p1:
        stop = True
    
    elif game[0][0] == p1 and game[1][0] == p1 and game[2][0] == p1:
        stop = True
    
    elif game[0][1] == p1 and game[1][1] == p1 and game[2][1] == p1:
        stop = True

    elif game[0][2] == p1 and game[1][2] == p1 and game[2][2] == p1:
        stop = True
            
    elif game[0][0] == p1 and game[1][1] == p1 and game[2][2] == p1:
        stop = True
            
    elif game[0][2] == p1 and game[1][1] == p1 and game[2][0] == p1:
        stop = True
    
        
    elif game[0][0] == p2 and game[0][1] == p2 and game[0][2] == p2:
        stop = True
                
    elif game[1][0] == p2 and game[1][1] == p2 and game[1][2] == p2:
        stop = True
        
    elif game[2][0] == p2 and game[2][1] == p2 and game[2][2] == p2:
        stop = True
    
    elif game[0][0] == p2 and game[1][0] == p2 and game[2][0] == p2:
        stop = True
    
    elif game[0][1] == p2 and game[1][1] == p2 and game[2][1] == p2:
        stop = True

    elif game[0][2] == p2 and game[1][2] == p2 and game[2][2] == p2:
        stop = True
        
    elif game[0][0] == p2 and game[1][1] == p2 and game[2][2] == p2:
        stop = True
        
    elif game[0][2] == p2 and game[1][1] == p2 and game[2][0] == p2:
        stop = True
        
    else:
        stop = False
        
    return stop   

while stop == False:
    player1()
    turns()
    win()    
    if stop == True:
        print ("")
        print ("You have won!")
        break
    else:
        print ("")

    print ("")
    player2()
    turns()
    win()
            
    if stop == True:
        print ("")
        print ("You have won!")
        break
    else:
        print ("")
        
    print("")
    