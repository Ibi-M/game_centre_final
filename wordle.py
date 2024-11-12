import random
import time

class color:
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    GRAY = '\033[37m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    
print ("")
print (color.BOLD + "You are going to play Wordle!")
time.sleep(1)
print ("")
print ("Simply just guess a word and follow these colors:" + color.END)
print ("")
print (" - " + color.GREEN + "GREEN " + color.END + "Coloured Letters are correctly guessed in their correctly guesses positions!")
time.sleep(1)
print (" - " + color.YELLOW + "YELLOW " + color.END + "Coloured Letters are correctly guessed but they are in wrong position of the word!")
time.sleep(1)
print (" - " + color.GRAY + "GREY " + color.END + "Coloured Letters are letters which are not in the word at all!")
time.sleep(1)
print ("")


word_list = ["PASTE","TRUCK", "RINGS", "RIDGE", "KNIFE", "PAPER", "SPEAK", "LAMPS", "BRUSH", "PANTS", "CLOTH"]
word = random.choice(word_list)
letters = list(word)

max_guesses = 6
guesses = []

for guess_count in range(max_guesses):
    while True:
        try:
            guess = input(f"Guess a Word ({guess_count + 1}/{max_guesses}): ").upper()
            if len(guess) != 5:
                print(color.RED + "Your guess must have exactly 5 letters. Try again." + color.END)
                print("")
                continue
            if not guess.isalpha():
                print(color.RED + "Your guess must only contain alphabetic characters. Try again." + color.END)
                print("")
                continue
            break
        except ValueError:
            print(color.RED + "Invalid input. Please try again." + color.END)
            print("")


    letterGuess = list(guess)
    marked_as_correct = [False] * 5
    wrong_position = [False] * 5

    for index in range(5):
        if letters[index] == letterGuess[index]:
            marked_as_correct[index] = True
            wrong_position[index] = True

    output = ""

    for i in range(5):
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
    print("")

    if guess == word:
        print("You have guessed the correct word!")
        break

    if guess_count == max_guesses - 1:
        print(f"You've used all {max_guesses} guesses! The correct word was '{word}'.")