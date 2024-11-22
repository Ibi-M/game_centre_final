import random
import time

class color: # Defines all the colors used
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    GRAY = '\033[37m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

# Intro
print (color.BOLD + "\nYou are going to play Wordle!\n")
time.sleep(1)
print ("Simply just guess a word and follow these colors:\n" + color.END)
print (" - " + color.GREEN + "GREEN " + color.END + "Coloured Letters are correctly guessed in their correctly guesses positions!")
time.sleep(1)
print (" - " + color.YELLOW + "YELLOW " + color.END + "Coloured Letters are correctly guessed but they are in wrong position of the word!")
time.sleep(1)
print (" - " + color.GRAY + "GREY " + color.END + "Coloured Letters are letters which are not in the word at all!\n")
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
                print(color.RED + "Your guess must have exactly 5 letters. Try again.\n" + color.END)
                continue
            if not guess.isalpha():
                print(color.RED + "Your guess must only contain alphabetic characters. Try again.\n" + color.END)
                continue
            break
        except ValueError:
            print(color.RED + "Invalid input. Please try again.\n" + color.END)

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
            output = output + color.GREEN + letterGuess[i] + color.END
        elif letterGuess[i] in letters and not marked_as_correct[i]:
            if letterGuess[i] != letters[i] and not wrong_position[i]:
                output = output + color.YELLOW + letterGuess[i] + color.END
                wrong_position[i] = True
            else:
                output = output + color.GRAY + letterGuess[i] + color.END
        else:
            output = output + color.GRAY + letterGuess[i] + color.END

    guesses.append(output)

    for g in guesses:
        print(g)

    if guess == word:
        print("\nYou have guessed the correct word!")
        break

    if guess_count == max_guesses - 1:
        print(f"You've used all {max_guesses} guesses! The correct word was '{word}'.")