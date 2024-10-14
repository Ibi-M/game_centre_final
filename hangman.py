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
    
def wrong1():
    print (color.BOLD + "---------" + color.END)
    print (color.BOLD + "|" + color.RED+ "       |" + color.END)
    print (color.BOLD + "|" + color.END)
    print (color.BOLD + "|" + color.END)
    print (color.BOLD + "|" + color.END)
    print (color.BOLD + "|" + color.END)

def wrong2():
    print (color.BOLD + "---------" + color.END)
    print (color.BOLD + "|" + color.RED+ "       |" + color.END)
    print (color.BOLD + "|" + color.RED+ "       O" + color.END)
    print (color.BOLD + "|" + color.END)
    print (color.BOLD + "|" + color.END)
    print (color.BOLD + "|" + color.END)

def wrong3():
    print (color.BOLD + "---------" + color.END)
    print (color.BOLD + "|" + color.RED+ "       |" + color.END)
    print (color.BOLD + "|" + color.RED+ "       O" + color.END)
    print (color.BOLD + "|" + color.RED+ "       | " + color.END)
    print (color.BOLD + "|" + color.END)
    print (color.BOLD + "|" + color.END)

def wrong4():
    print (color.BOLD + "---------" + color.END)
    print (color.BOLD + "|" + color.RED+ "       |" + color.END)
    print (color.BOLD + "|" + color.RED+ "       O" + color.END)
    print (color.BOLD + "|" + color.RED+ "      /| " + color.END)
    print (color.BOLD + "|" + color.END)
    print (color.BOLD + "|" + color.END)

def wrong5():
    print (color.BOLD + "---------" + color.END)
    print (color.BOLD + "|" + color.RED+ "       |" + color.END)
    print (color.BOLD + "|" + color.RED+ "       O" + color.END)
    print (color.BOLD + "|" + color.RED+ "      /|\ " + color.END)
    print (color.BOLD + "|" + color.END)
    print (color.BOLD + "|" + color.END)


def wrong6():
    print (color.BOLD + "---------" + color.END)
    print (color.BOLD + "|" + color.RED+ "       |" + color.END)
    print (color.BOLD + "|" + color.RED+ "       O" + color.END)
    print (color.BOLD + "|" + color.RED+ "      /|\ " + color.END)
    print (color.BOLD + "|" + color.RED+ "       |  " + color.END)
    print (color.BOLD + "|" + color.END)

def wrong7():
    print (color.BOLD + "---------" + color.END)
    print (color.BOLD + "|" + color.RED+ "       |" + color.END)
    print (color.BOLD + "|" + color.RED+ "       O" + color.END)
    print (color.BOLD + "|" + color.RED+ "      /|\ " + color.END)
    print (color.BOLD + "|" + color.RED+ "       |  " + color.END)
    print (color.BOLD + "|" + color.RED+ "      /  " + color.END)

def wrong8():
    print (color.BOLD + "---------" + color.END)
    print (color.BOLD + "|" + color.RED+ "       |" + color.END)
    print (color.BOLD + "|" + color.RED+ "       O" + color.END)
    print (color.BOLD + "|" + color.RED+ "      /|\ " + color.END)
    print (color.BOLD + "|" + color.RED+ "       |  " + color.END)
    print (color.BOLD + "|" + color.RED+ "      / \ " + color.END)

def valid_guess(guess, used):

    if len(guess) != 1 or guess.isalpha() == False:
        print("Invalid input! Please enter a single letter (a-z).")
        print ("")
        return False

    if guess in used:
        print("You've already tried this letter. Choose another.")
        print ("")
        return False
    return True


print ("You are going to play Hangman...")
print ("")
list = ["remote", "toothpaste", "picture", "glass", "puddle", "truck", "ring", "fridge", "knife", "candle", "newspaper", "speakers", "lamp" ,"toothbrush","window","pants","clothes","blouse","button"]
word = random.choice(list)
used = []
so_far = ("-") * len(word) 
wrong = 0                 

length = len(word)
dash = "-"
g_word = dash*length
guesses = 1
round = 0
max_guesses = 7

print ("You are going to guess the following word: ")
print (g_word)
print ("")

finish = False

while finish == False:
    round = round + 1
    time.sleep(1)
    print((color.YELLOW + color.BOLD + color.UNDERLINE) + "Guess:",round,"" + color.END)
    print ("")
    print ("Used Letters", used)
    guess = input("Guess a letter: ")

    guess = guess.lower()
    while valid_guess(guess,used) == False:
        guess = input("Guess a letter")

    
    used.append(guess)  
    
    if guess in word:
        print ("")
        print ("Yes, that letter is in the word")
        new = ""       
        
        for i in range (len(word)):
            if guess == word[i]:
                new = new + guess    
            else:
                new = new + so_far[i] 
        so_far = new 
        
    else:
        print ("")
        print("Nope, that letter is not in the word")
        wrong = wrong + 1

    print ("")
    print (so_far)
    print ("")
    confirm = False
    if wrong == 0:
        wrong1()
    elif wrong == 1:
        wrong2()
    elif wrong == 2:
        wrong3()
    elif wrong == 3:
        wrong4()
    elif wrong == 4:
        wrong5()
    elif wrong == 5:
        wrong6()
    elif wrong == 6:
        wrong7()
    elif wrong == 7:
        wrong8()

    time.sleep(1)
        
    print (color.CYAN + "--------------------------------------------------" + color.END)
    print ("")
    guesses = guesses + 1

    if wrong == 7:
        print ("You have lost as you have guessed the maximum amount of letters that you're allowed to guess!")
        finish = True
        print ("")
        print ("The word was", (color.BOLD + color.UNDERLINE + color.BLUE) + word + color.END)
        
    if so_far == word:
        finish = True
        left = max_guesses - guesses
        if left <0:
            left = 0
        print ("You have guessed the word correctly in", guesses, "guesses")