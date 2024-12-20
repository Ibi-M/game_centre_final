import random
import time
from colorama import *
init(autoreset=True)

class color:
    UNDERLINE = '\033[4m'


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
        print(Style.BRIGHT + line + Fore.RESET)

def update_hangman(wrong): # Updates the hangman display if the player has got it wrong
    if wrong == 1:
        hangman[1] = "|       |"  
    elif wrong == 2:
        hangman[2] = f"|      {Fore.RED} O"  
    elif wrong == 3:
        hangman[3] = f"|      {Fore.RED} |" 
    elif wrong == 4:
        hangman[4] = f"|     {Fore.RED} /|"  
    elif wrong == 5:
        hangman[4] = f"|     {Fore.RED} /|\\"
    elif wrong == 6:
        hangman[5] = f"|     {Fore.RED} /" 
    elif wrong == 7:
        hangman[5] = f"|     {Fore.RED} / \\"
        hangman[6] = "|   GAME OVER"  

def valid_guess(guess, used):  # Checks if the guess inputted is valid or not
    if len(guess) != 1 or guess.isalpha() == False:
        print(f"{Fore.RED} Invalid input! Please enter a single letter (a-z).\n")
        return False

    if guess in used:
        print("You've already tried this letter. Choose another.\n")
        return False
    return True

print(f"{Style.BRIGHT}You are going to play Hangman...\n") # Primary Display for the Game
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
    print(f"\n{Fore.YELLOW + Style.BRIGHT + color.UNDERLINE} Guess: {round}")
    print(f"Used Letters {used}")
    guess = input("\nGuess a letter: ")

    guess = guess.lower()
    while valid_guess(guess, used) == False:
        guess = input("\nGuess a letter: ")

    used.append(guess)

    if guess in word:
        print(f"\n{Fore.GREEN}Yes, that letter is in the word\n")
        new = ""

        for i in range(len(word)): #Updates the variable of the player progress
            if guess == word[i]:
                new = new + guess    
            else:
                new = new + so_far[i] 
        so_far = new 

    else:
        print(f"{Fore.RED}Nope, that letter is not in the word\n")
        wrong = wrong + 1

    print(so_far)
    confirm = False

    update_hangman(wrong)
    print_hangman()

    time.sleep(1)

    print(f"{Fore.CYAN}--------------------------------------------------\n")
    guesses = guesses + 1

    if wrong == 7:
        print("\nYou have lost as you have guessed the maximum amount of letters that you're allowed to guess!\n")
        finish = True
        print(f"The word was {Style.BRIGHT + color.UNDERLINE + Fore.BLUE + word}")

    if so_far == word:
        finish = True
        left = max_guesses - guesses
        if left < 0:
            left = 0
        print(f"You have guessed the word correctly in {guesses} guesses")
