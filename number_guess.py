import random
import time

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

def get_guess(): # Gets a valid user input for the guess
    global guess
    while True:
        try:
            guess = int(input("Enter any number between 1 and 20:\n"))
            if 1 <= guess <= 20:
                return guess
            else:
                print(color.RED + "Please enter a number between 1 and 20.\n" + color.END)
        except ValueError:
            print(color.RED + "Invalid input! Please enter an integer.\n" + color.END)

    

print (color.BOLD + "Let's play a quick game of Guess the Number!\n")
time.sleep(0.5)
print ("You have to match the number that I am thinking of!\n")
time.sleep(1.5)
print ("You have 3 lives! Answer wrong and you lose a life!\n" + color.END)
time.sleep(1)
print (color.BOLD + "\nLet's Play!\n" + color.END)
    
number = random.randrange(1,20)
limit = 20
lives = 2
finish = True
get_guess()

while lives != 0 or finish == True: # Main Game Loop
            
    if guess < number: # Checks if guess is less than the number
        lives = lives - 1
        print(color.DARKCYAN + "Too low!" + color.END)
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
        print(color.DARKCYAN + "Too high!" + color.END)
        print ("Try Again\n")
        get_guess()
        if lives == 0:
            print (color.BOLD + color.UNDERLINE + color.RED + "\nGame Over!\n" + color.END)
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