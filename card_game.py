import random
import time

class color: # Class - Defines all colors used
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def correct(): # For when the player has guessed correctly
  global score
  global round
  score = score + 1
  round = round - 1
  time.sleep(1)
  print (color.GREEN + "\nYou have guessed correctly!" + color.END)
  score = str(score)
  print (color.BOLD + "Your score is now\n", score + color.END)
  score = int(score)

def incorrect(): # For when the player has guessed incorrectly
  time.sleep(1)
  print (color.RED + "\nYou are wrong!\n" + color.END)

def info(): # Displays the input instructions
  print ("Answer by typing either:")
  time.sleep (1)
  print ("- 'h' for Higher")
  time.sleep(1)
  print ("- 'l' for lower")
  time.sleep(1)
  print ("- 's' for the same\n")
  time.sleep(1)

def valid_predict(card_number): # Checks if the input is valid or not
    answers = ["h", "l", "s"]
    print ("---------------------------------------------------------------------------------------------------")
    print (f"Do you think the {card_number} card is higher, lower or the same value?\n")
    info()
    predict = input("Type your answer: ").lower()
   
    while predict not in answers:                           
        print ("")
        print(color.RED + "Invalid Answer!" + color.END)
        print ("")
        info()
        predict = input()
    return predict

def checking(card1,card2,predict): # Checks if the guessed card matches the generated one
    print ("The next card is: " +color.YELLOW + str(card2) + color.END + " " + random.choice(type))
    if card2 < card1 and predict == "l":
        correct()
    elif card2 > card1 and predict == "h":
        correct()
    elif card2 == card1 and predict == "s":
        correct()
    else:
        incorrect()
# ---------------------------- INTRO ----------------------------
print (color.BOLD + "You are going to play the Card Game!\n")
time.sleep (1)
print ("You will be given a selection of cards.\n")
time.sleep (1)
print ("You will draw the 1st card...\n")
time.sleep (1)
print ("Next, you will determine whether the following card will be higher or lower than the card that has been drawed...\n")
time.sleep (1)
print ("Note that the game is to guess THE 'VALUE' OF THE CARD, NOT THE TYPE!\n")
print ("e.g: 2 Diamonds. Make sure you only predict whether the value (the number) of the card, not the type, (Diamonds, Spades, etc) or else you will lose!\n")
print ("You will draw the next card...\n")
time.sleep (1)
print ("If you were correct, then your score will increase by 1.\n")
time.sleep (1)
print ("If you are incorrect, well then, your score is not affected and that is just bad luck :-)\n" + color.END)
time.sleep (1)
# ---------------------------------------------------------------

round = 4
score = 0
type = ("Hearts", "Spades", "Clubs", "Diamonds")
print ("Choose a card deck selection difficulty!")
print ("Type the letter 'e' for easy!")
print ("Type the letter 'h' for hard!")
deck_choice = input()

# Gives all the cards a random generated number
easy_deck1 = random.randint(2,10)
easy_deck2 = random.randint(2,10)
easy_deck3 = random.randint(2,10)
easy_deck4 = random.randint(2,10)
easy_deck5 = random.randint(2,10)
easy_deck6 = random.randint(2,10)
easy_deck7 = random.randint(2,10)

hard_deck1 = random.randint(2,20)
hard_deck2 = random.randint(2,20)
hard_deck3 = random.randint(2,20)
hard_deck4 = random.randint(2,20)
hard_deck5 = random.randint(2,20)
hard_deck6 = random.randint(2,20)
hard_deck7 = random.randint(2,20)
hard_deck8 = random.randint(2,20)
hard_deck9 = random.randint(2,20)
hard_deck10 = random.randint(2,20)
hard_deck11 = random.randint(2,20)
hard_deck12 = random.randint(2,20)
#----------------------------------------------------

answers = ["h", "l", "s"]

while round != 0:
  if deck_choice == "e":
      easy_deck = random.randrange(5)
      time.sleep(1)
      print ("OK! Since you have chosen the 'easy' level, you will have 5 cards to guess...\n")
      time.sleep(1)
      print ("Your first card is", color.YELLOW + str(easy_deck1) + color.END + " " + random.choice(type))
      time.sleep(1)
      print("") 

 # --------- Performs the subroutines for the easy level; each card for the player to guess----------
      predict1 = valid_predict("second")
      checking(easy_deck1,easy_deck2,predict1)

      predict2 = valid_predict("third")
      checking(easy_deck2,easy_deck3,predict2)
        
      predict3 = valid_predict("fourth")
      checking(easy_deck3,easy_deck5,predict3)

      predict4 = valid_predict("fifth")
      checking(easy_deck4,easy_deck5,predict4)
      
      predict5 = valid_predict("final")
      checking(easy_deck5,easy_deck6,predict5)
      #--------------------------------------------------------------


      time.sleep(1)
      print ("\nAND...")
      time.sleep(1)
      print ("\nThat is the end of the game! You achieved a score of", score, "/5!")
      break
  
  if deck_choice == "h":
    print ("OK! Since you have chosen the 'hard' level, you will have 10 cards to guess...\n")
    print ("Note this before you start...\n")
    time.sleep(2)
    print ("As this is a 'hard' level, then instead of a normal card deck which has the range of 2 to 10...\n")
    time.sleep(1.5)
    print ("There will be a range between 2 and 20!\n")
    time.sleep(1)
    print ("Your first card is", color.YELLOW + hard_deck1 + color.YELLOW + " " + random.choice(type))
    time.sleep(1)
    print("")

    # --------- Performs the subroutines for the difficult level; each card for the player to guess----------

    predict1 = valid_predict("second")
    checking(hard_deck1,hard_deck2,predict1)

    predict2 = valid_predict("third")
    checking(hard_deck2,hard_deck3,predict2)

    predict3 = valid_predict("fourth")
    checking(hard_deck3,hard_deck4,predict3)

    predict4 = valid_predict("fifth")
    checking(hard_deck4,hard_deck5,predict4)

    predict5 = valid_predict("sixth")
    checking(hard_deck5,hard_deck6,predict5)

    predict6 = valid_predict("seventh")
    checking(hard_deck6,hard_deck7,predict6)

    predict7 = valid_predict("eigth")
    checking(hard_deck7,hard_deck8,predict7)

    predict8 = valid_predict("ninth")
    checking(hard_deck8,hard_deck9,predict8)

    predict9 = valid_predict("tenth")
    checking(hard_deck9,hard_deck10,predict9)

    predict10 = valid_predict("final")
    checking(hard_deck10,hard_deck11,predict10)

    # ----------------------------------------------------------------------------------
    print ("\nAND...\n")
    time.sleep(1)
    print (color.BOLD + "That is the end of the game! You achieved a score of", score, "/10!" + color.END)
    break
