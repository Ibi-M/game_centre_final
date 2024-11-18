import random
import time

class color:
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    END = '\033[0m'
     
print (color.BOLD + "You are going to play Rock, Paper, Scissors with 3 rounds with the Computer" + color.END)
print ("")
rounds = 3
turns = ["first", "second", "final"]
no_turns = 0
win = 0
    
while rounds != 0:
    fine = True
    
    print (" Input one of the following: (Only Input in CAPS")
    print (" - 'R' for Rock")
    print (" - 'P' for Paper")
    print (" - 'S' for Scissors")
    print ("")
    
    choice = ""
    ok = False
    
    while ok != True:
        answer = input()
        answer = answer.upper()
    
        if answer == "R":
                choice = "Rock"
                ok = True
        elif answer == "P":
                choice = "Paper"
                ok = True
            
        elif answer == "S":
                choice = "Scissors"
                ok = True
    
        else:
            print (color.RED + "You have entered an invalid input" + color.END)
            ok = False
            
    options = ["Rock", "Paper", "Scissors"]
    
    index = random.randint(0,2)
    
    c_choice = options[index]
    c_choice = c_choice.upper()
    
    print ("You chose ", choice)
    print ("The computer chose...")
    time.sleep(1)
    print (c_choice)
    print ("")
    time.sleep(1)
        
    if answer == "R" and index == 0:
        print (color.YELLOW + "You have chose the same as the computer")
        print ("This will not count as a round" + color.END)
        fine = False
        print ("--------------------------------------------------")
        time.sleep(1)
            
    elif answer == "P" and index == 1:
        print (color.YELLOW + "You have chose the same as the computer")
        print ("This will not count as a round" + color.END)
        fine = False
        print ("-----------------------------------------")
        time.sleep(1)
            
    elif answer == "S" and index == 2:
        print (color.YELLOW + "You have chose the same as the computer")
        print ("This will not count as a round" + color.END)
        fine = False
        print ("-----------------------------------------")
        time.sleep(1)
        

    if answer == "R" and index == 2:
        print ("You have " + color.GREEN + "won" + color.END + " the ", turns[no_turns],"round!")
        win = win + 1
        rounds = rounds - 1
        
    elif answer == "P" and index == 0:
        print ("You have " + color.GREEN + "won" + color.END + " the ", turns[no_turns],"round!")
        win = win + 1
        rounds = rounds - 1
            
    elif answer == "S" and index == 1:
        print ("You have " + color.GREEN + "won" + color.END + " the ", turns[no_turns],"round!")
        win = win + 1
        rounds = rounds - 1
            
    elif answer == "R" and index == 1:
        print ("You have " + color.RED + "lost" + color.END + " the ", turns[no_turns],"round!")
        rounds = rounds - 1
    
    elif answer == "S" and index == 0:
        print ("You have " + color.RED + "lost" + color.END + " the ", turns[no_turns],"round!")
        rounds = rounds - 1
    
    elif answer == "P" and index == 2:
        print ("You have " + color.RED + "lost" + color.END + " the ", turns[no_turns],"round!")
        rounds = rounds - 1
    
    if no_turns == 3:
        break
    print ("")
    
    if fine != False and no_turns != 2:
        no_turns = no_turns + 1
        print ("Time for the next round!")
        print ("-------------------------------------------------")
        time.sleep(1)
        print ("")
    
if win == 0:
    word = "rounds"
if win == 1:
    word = "round"
elif win > 1:
    word = "rounds"
        
print ("")
time.sleep(1)
print ("The 3 rounds are finished, and you have" + color.GREEN +  " won " + color.END, win, word)
print ("")
if win > 1:
    result = "won"
elif win <= 1:
    result = "lost"

print ("Which means you have", result, "!")
    