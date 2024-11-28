import random
import time
from colorama import *
init(autoreset=True)

class color:
    UNDERLINE = '\033[4m'

# Intro
print (f"\n{Style.BRIGHT}You are going to play Wordle!\n")
time.sleep(1)
print (f"\n{Style.BRIGHT}Simply just guess a word and follow these colors:\n")
print (f" - {Fore.GREEN} GREEN {Fore.RESET} Coloured Letters are correctly guessed in their correctly guesses positions!")
time.sleep(1)
print (f" - {Fore.YELLOW} YELLOW {Fore.RESET} Coloured Letters are correctly guessed but they are in wrong position of the word!")
time.sleep(1)
print (f" - {Fore.BLACK} GREY {Fore.RESET} Coloured Letters are letters which are not in the word at all!\n")
time.sleep(1)

word_list = ["PASTE","TRUCK", "RINGS", "RIDGE", "KNIFE", "PAPER", "SPEAK", "LAMPS", "BRUSH", "PANTS", "CLOTH"]
word = random.choice(word_list)
letters = list(word)

max_guesses = 6
guesses = []

for guess_count in range(max_guesses): # Game Loop until number of guesses reaches 6
    while True:
        try:
            guess = input(f"Guess a Word ({guess_count + 1}/{max_guesses}): ").upper()
            if len(guess) != 5:
                print(f"{Fore.RED}Your guess must have exactly 5 letters. Try again.\n")
                continue
            if not guess.isalpha():
                print(f"{Fore.RED} Your guess must only contain alphabetic characters. Try again.\n")
                continue
            break
        except ValueError:
            print(f"{Fore.RED} Invalid input. Please try again.\n")

    letterGuess = list(guess)
    marked_as_correct = [False] * 5
    wrong_position = [False] * 5

    for index in range(5):
        if letters[index] == letterGuess[index]:
            marked_as_correct[index] = True
            wrong_position[index] = True

    output = ""

    for i in range(5): # Marks each letter their co-ordinated color based on the word
        if marked_as_correct[i]:
            output = output + Fore.GREEN + letterGuess[i] 
        elif letterGuess[i] in letters and not marked_as_correct[i]:
            if letterGuess[i] != letters[i] and not wrong_position[i]:
                output = output + Fore.YELLOW + letterGuess[i]
                wrong_position[i] = True
            else:
                output = output + Fore.BLACK + letterGuess[i] 
        else:
            output = output + Fore.BLACK + letterGuess[i]

    guesses.append(output)

    for g in guesses:
        print(g)

    if guess == word:
        print("\nYou have guessed the correct word!")
        break

    if guess_count == max_guesses - 1:
        print(f"You've used all {max_guesses} guesses! The correct word was '{word}'.")