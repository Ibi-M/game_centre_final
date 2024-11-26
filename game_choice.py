import time
from subprocess import call

def open_py_file(): # Opens the game which relates to the user input
    choose = int(input())
    print ("")
        
    if choose == 1:
        call(["python", "hangman.py"])

    elif choose == 2:
        call(["python", "rps.py"])

    elif choose == 3:
        call(["python",  "n&s.py" ])

    elif choose == 4:
        call(["python",  "number_guess.py" ])

    elif choose == 5:
        call(["python",  "card_game.py" ])   
    
    elif choose == 6:
        call(["python", "connect_four.py"])

    elif choose == 7:
        call(["python", "bingo.py"])
    
    elif choose == 8:
        call(["python", "21.py"])
    
    elif choose == 9:
        call(["python", "memory_match.py"])
    
    elif choose == 10:
        call(["python", "wordle.py"])
    
    else:
        print ("Invalid!")
    

def choices(): # Displays the game choices
    print (" - Hangman (Type '1')")
    time.sleep(1)
    print (" - Rock Paper Scissors (Type '2')")
    time.sleep(1)
    print (" - Noughts & Crosses (Type '3')")
    time.sleep(1)
    print (" - Guess the Number (Type '4')")
    time.sleep(1)
    print (" - Card Game (Type '5')")
    time.sleep(1)
    print (" - Connect Four (Type '6')")
    time.sleep(1)
    print (" - Bingo (Type '7')")
    time.sleep(1)
    print (" - 21 (Type '8')")
    time.sleep(1)
    print (" - Memory Game ('Type '9')")
    time.sleep(1)
    print (" - Wordle (Type '10')")
    open_py_file()
  
def final(): # Asks the user at the end of their gane if they would like to play an another game
    global finish
    finish = False

    while finish == False:
        print ("----------------------------------------------")
        print ("Would you like to play another game?")
        again = input()
        again = again.lower()


        if again == "yes":
            print ("")
            print ("Sure! Choose a game: ")
            choices()

        elif again == "no":
            print ("")
            print ("------------------------------")
            print ("Thanks for playing on Ibi's Game Centre! ")
            finish = True

print ("Welcome to the Game Centre!\n")
print ("You have a choice of:")
choices()
final()
