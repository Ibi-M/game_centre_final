import random
import time
from colorama import *
init(autoreset=True)

class color:
    UNDERLINE = '\033[4m'

def get_guess(): # Gets a valid user input for the guess
    global guess
    while True:
        try:
            guess = int(input("Enter any number between 1 and 20:\n"))
            if 1 <= guess <= 20:
                return guess
            else:
                print(f"{Fore.RED}Please enter a number between 1 and 20.\n")
        except ValueError:
            print(f"{Fore.RED}Invalid input! Please enter an integer.\n")

    

print (f"{Style.BRIGHT}Let's play a quick game of Guess the Number!\n")
time.sleep(0.5)
print (f"{Style.BRIGHT}You have to match the number that I am thinking of!\n")
time.sleep(1.5)
print (f"{Style.BRIGHT}You have 3 lives! Answer wrong and you lose a life!\n")
time.sleep(1)
print (f"{Style.BRIGHT}\nLet's Play!\n")
    
number = random.randrange(1,20)
limit = 20
lives = 2
finish = True
get_guess()

while lives != 0 or finish == True: # Main Game Loop
            
    if guess < number: # Checks if guess is less than the number
        lives = lives - 1
        print(f"{Fore.CYAN}Too low!")
        print ("Try Again\n")
        get_guess()
        if lives == 0:
            print ("\nGame Over!\n")
            time.sleep(1)
            print ("\nThe number was...\n")
            time.sleep(1)
            print (number)
            break
                
    elif guess > number: # Checks if the guess is greater than the number
        lives = lives - 1
        print(f"{Fore.CYAN}Too high!")
        print ("Try Again\n")
        get_guess()
        if lives == 0:
            print (f"\n{Style.BRIGHT + color.UNDERLINE + Fore.RED}Game Over!\n")
            time.sleep(1)
            print ("The number was...")
            time.sleep(1)
            print (number)
            break
                
    elif guess == number: # Checks if guess equals the number
        lives = lives - 1
        print ("Yes, you got it right!")
        finish = True
        break