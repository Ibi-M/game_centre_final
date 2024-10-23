import time

from subprocess import call

def open_py_file():
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
    
    else:
        print ("Invalid!")
    

def choices():
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
    print ("- Bingo (Type '7')")

    open_py_file()
  


def final():
    global finish
    finish = False

    while finish == False:
        print ("")
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
       
        


print ("Welcome to the Game Centre!")
print ("")
print ("You have a choice of:")

choices()

final()
