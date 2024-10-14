import random
import time

def get_guess():
    global guess
    while True:
        try:
            guess = int(input("Enter any number between 1 and 20: "))
            print ("")
            if 1 <= guess <= 20:
                return guess
            else:
                print("Please enter a number between 1 and 20.")
                print ("")
        except ValueError:
            print("Invalid input! Please enter an integer.")
            print ("")

print ("Let's play a quick game of Guess the Number!")
time.sleep(0.5)
print ("")
print ("You have to match the number that I am thinking of!")
time.sleep(1.5)
print ("You have 3 lives! Answer wrong and you lose a life!")
print ("")
time.sleep(1.5)
print ("But be careful! If you guess above the number 20 then the game immediately ends!")
time.sleep(1.5)
print ("")
print ("Ready?")
time.sleep(1)
print ("")
print ("3!")
time.sleep(1)
print ("")
print ("2!")
time.sleep(1)
print ("")
print ("1!")
time.sleep(1)
print ("Let's Play!")
    
number = random.randrange(1,20)
limit = 20
lives = 2
finish = True
get_guess()

while lives != 0 or finish == True:
    if guess > 20:
        print ("You have entered a value above 20, therefore the game ends!")
        break
            
    elif guess < number:
        lives = lives - 1
        print ("")
        print("Too low!")
        print ("Enter number again: ")
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
        print ("")
        print("Too high!")
        print ("Enter number again: ")
        get_guess()
        print ("")
        if lives == 0:
            print ("Game Over!")
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