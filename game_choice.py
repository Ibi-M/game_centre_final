from subprocess import call

def open_py_file():
    choose = int(input())
    
    if choose == "1":
        call(["python", "hangman.py"])
    elif choose == "2":
        call(["python", "rps.py"])

import time

print ("Welcome to the Game Centre!")
print ("")
print ("You have a choice of:")
print (" - Hangman (Type '1'")
time.sleep(1)
print (" - Rock Paper Scissors (Type '2')")
time.sleep(1)
print (" - Noughts & Crosses (Type '3')")
time.sleep(1)
print (" - Guess the Number (Type '4')")
time.sleep(1)
print (" - Card Game (Type '5')")
time.sleep(1)


open_py_file()