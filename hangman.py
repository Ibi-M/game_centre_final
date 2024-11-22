import random
import time

class color: #Defines colors
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

hangman = [            # Default Layout for whole game
    "-------------",
    "|",
    "|",
    "|",
    "|",
    "|",
    "|",
    "-------------"
]

def print_hangman():       # Displays the current hangman layout
    for line in hangman:
        print(color.BOLD + line + color.END)

def update_hangman(wrong): # Updates the hangman display if the player has got it wrong
    if wrong == 1:
        hangman[1] = "|       |"  
    elif wrong == 2:
        hangman[2] = "|       " + color.RED + "O" + color.END  
    elif wrong == 3:
        hangman[3] = "|       " + color.RED + "|" + color.END
    elif wrong == 4:
        hangman[4] = "|      " + color.RED + "/|" + color.END  
    elif wrong == 5:
        hangman[4] = "|      " + color.RED + "/|\\" + color.END  
    elif wrong == 6:
        hangman[5] = "|      " + color.RED + "/" + color.END  
    elif wrong == 7:
        hangman[5] = "|      " + color.RED + "/ \\" + color.END  
        hangman[6] = "|   GAME OVER"  

def valid_guess(guess, used):  # Checks if the guess inputted is valid or not
    if len(guess) != 1 or guess.isalpha() == False:
        print(color.RED + "Invalid input! Please enter a single letter (a-z).\n" + color.END)
        return False

    if guess in used:
        print("You've already tried this letter. Choose another.\n")
        return False
    return True

print(color.BOLD + "You are going to play Hangman...\n" + color.END) # Primary Display for the Game
list = ["remote", "toothpaste", "picture", "glass", "puddle", "truck", "ring", "fridge", "knife", "candle", "newspaper", "speakers", "lamp", "toothbrush", "window", "pants", "clothes", "blouse", "button"]
word = random.choice(list)
used = []
so_far = ("-") * len(word) # Variable that is used to record player progress 
wrong = 0                  
length = len(word)
dash = "-"
g_word = dash * length
guesses = 1
round = 0
max_guesses = 7

print("You are going to guess the following word: ")
print(g_word)

finish = False

while finish == False: # Loops the game until the player guesses the word or runs out of guesses
    round = round + 1
    time.sleep(1)
    print((color.YELLOW + color.BOLD + color.UNDERLINE) + "\nGuess:", round, "" + color.END)
    print(f"Used Letters {used}")
    guess = input("\nGuess a letter: ")

    guess = guess.lower()
    while valid_guess(guess, used) == False:
        guess = input("\nGuess a letter: ")

    used.append(guess)

    if guess in word:
        print(color.GREEN + "\nYes, that letter is in the word\n" + color.END)
        new = ""

        for i in range(len(word)): #Updates the variable of the player progress
            if guess == word[i]:
                new = new + guess    
            else:
                new = new + so_far[i] 
        so_far = new 

    else:
        print(color.RED + "Nope, that letter is not in the word\n" + color.END)
        wrong = wrong + 1

    print(so_far)
    confirm = False

    update_hangman(wrong)
    print_hangman()

    time.sleep(1)

    print(color.CYAN + "--------------------------------------------------" + color.END)
    print("")
    guesses = guesses + 1

    if wrong == 7:
        print("\nYou have lost as you have guessed the maximum amount of letters that you're allowed to guess!\n")
        finish = True
        print("The word was", (color.BOLD + color.UNDERLINE + color.BLUE) + word + color.END)

    if so_far == word:
        finish = True
        left = max_guesses - guesses
        if left < 0:
            left = 0
        print(f"You have guessed the word correctly in {guesses} guesses")
