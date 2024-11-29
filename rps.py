import random
import time
from colorama import *
init(autoreset=True)

class color:
    UNDERLINE = '\033[4m'

print (f"\n{Style.BRIGHT}You are going to play Rock, Paper, Scissors with 3 rounds with the Computer\n")
rounds = 3
turns = ["first", "second", "final"]
no_turns = 0
win = 0
    
while rounds != 0: # Displays the options to the user
    fine = True
    print (" Input one of the following: (Only Input in CAPS")
    print (" - 'R' for Rock")
    print (" - 'P' for Paper")
    print (" - 'S' for Scissors\n")
    
    choice = ""
    ok = False
    
    while ok != True: #Gets a valid input
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
            print (f"{Fore.RED}You have entered an invalid input")
            ok = False

            
    options = ["Rock", "Paper", "Scissors"]
    
    index = random.randint(0,2)
    
    c_choice = options[index]
    c_choice = c_choice.upper()
    
    print ("You chose ", choice)
    print ("The computer chose...")
    time.sleep(1)
    print (c_choice)
    time.sleep(1)

    # Checks if the guess matches the computer
    if answer == "R" and index == 0:
        print (f"\n{Fore.YELLOW}You have chose the same as the computer")
        print (f"{Fore.YELLOW}This will not count as a round")
        fine = False
        print ("--------------------------------------------------")
        time.sleep(1)
            
    elif answer == "P" and index == 1:
        print (f"\n{Fore.YELLOW}You have chose the same as the computer")
        print (f"{Fore.YELLOW}This will not count as a round")
        fine = False
        print ("-----------------------------------------")
        time.sleep(1)
            
    elif answer == "S" and index == 2:
        print (f"\n{Fore.YELLOW}You have chose the same as the computer")
        print (f"{Fore.YELLOW}This will not count as a round")
        fine = False
        print ("-----------------------------------------")
        time.sleep(1)
        
    # Checks the winning combos
    if answer == "R" and index == 2:
        print (f"You have{Fore.GREEN} won{Fore.RESET} the {turns[no_turns]} round!")
        win = win + 1
        rounds = rounds - 1
        
    elif answer == "P" and index == 0:
        print (f"You have{Fore.GREEN} won{Fore.RESET} the {turns[no_turns]} round!")
        win = win + 1
        rounds = rounds - 1
            
    elif answer == "S" and index == 1:
        print (f"You have{Fore.GREEN} won{Fore.RESET} the {turns[no_turns]} round!")
        win = win + 1
        rounds = rounds - 1

    # Checks the losing combos        
    elif answer == "R" and index == 1:
        print (f"You have{Fore.RED} lost{Fore.RESET} the {turns[no_turns]} round!")
        rounds = rounds - 1
    
    elif answer == "S" and index == 0:
        print (f"You have{Fore.RED} lost{Fore.RESET} the {turns[no_turns]} round!")
        rounds = rounds - 1
    
    elif answer == "P" and index == 2:
        print (f"You have{Fore.RED} lost{Fore.RESET} the {turns[no_turns]} round!")
        rounds = rounds - 1
    
    if no_turns == 3: 
        break
    print ("")
    
    if fine != False and no_turns != 2:
        no_turns = no_turns + 1
        print ("Time for the next round!")
        print ("-------------------------------------------------\n")
        time.sleep(1)
    
if win == 0:
    word = "rounds"
if win == 1:
    word = "round"
elif win > 1:
    word = "rounds"
        
time.sleep(1)
print (f"\nThe 3 rounds are finished, and you have won {win , word}")
if win > 1:
    result = Fore.GREEN + "won"
elif win <= 1:
    result = Fore.RED + "lost"

print ("\nWhich means you have", result, "!")
    