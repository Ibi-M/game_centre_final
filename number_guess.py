import random
import time
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

def get_guess():
    global guess
    while True:
        try:
            guess = int(input("Enter any number between 1 and 20: "))
            print ("")
            if 1 <= guess <= 20:
                return guess
            else:
                print(color.RED + "Please enter a number between 1 and 20." + color.END)
                print ("")
        except ValueError:
            print(color.RED + "Invalid input! Please enter an integer." + color.END)
            print ("")

print (color.BOLD + "Let's play a quick game of Guess the Number!")
time.sleep(0.5)
print ("")
print ("You have to match the number that I am thinking of!")
time.sleep(1.5)
print ("")
print ("You have 3 lives! Answer wrong and you lose a life!" + color.END)
print ("")
time.sleep(1.5)
print ("")
time.sleep(1)
print (color.BOLD + "Let's Play!" + color.END)
print ("")

    
number = random.randrange(1,20)
limit = 20
lives = 2
finish = True
get_guess()

while lives != 0 or finish == True:
            
    if guess < number:
        lives = lives - 1
        print(color.DARKCYAN + "Too low!" + color.END)
        print ("Try Again")
        print ("")
        get_guess()
        print ("")
        if lives == 0:
            print ("Game Over!")
            time.sleep(1)
            print ("The number was...")
            time.sleep(1)
            print (number)
            break
                
    elif guess > number:
        lives = lives - 1
        print(color.DARKCYAN + "Too high!" + color.END)
        print ("Try Again")
        print ("")
        get_guess()
        print ("")
        if lives == 0:
            print (color.BOLD + color.UNDERLINE + color.RED + "Game Over!" + color.END)
            time.sleep(1)
            print ("The number was...")
            time.sleep(1)
            print (number)
            break
                
    elif guess == number:
        lives = lives - 1
        print ("Yes, you got it right!")
        finish = True
        break