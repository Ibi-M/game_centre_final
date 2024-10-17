import random
import time


def correct():
  global score
  global round
  score = score + 1
  round = round - 1
  time.sleep(1)
  print ("You have guessed correctly!")
  print ("Your score is now", score)
  
def incorrect():
  print ("")
  time.sleep(1)
  print ("You are wrong!")

def info():
  print ("Answer by typing either:")
  time.sleep (1)
  print ("- 'h' for Higher")
  time.sleep(1)
  print ("- 'l' for lower")
  time.sleep(1)
  print ("- 's' for the same")
  time.sleep(1)

def valid_predict(card_number):
    answers = ["h", "l", "s"]
    prompt_message = f"Do you think the {card_number} card is higher, lower or the same value? Type your answer: "
    info()
    predict = input(prompt_message).strip().lower()
   
    while predict not in answers:
        print("Invalid Answer!")
        info()
        predict = input(prompt_message).strip().lower()
   
    return predict

def checking(card1,card2,predict):
    print ("The next card is:", card2, random.choice(type))
    if card2 < card1 and predict == "l":
        correct()
    elif card2 > card1 and predict == "h":
        correct()
    elif card2 == card1 and predict == "s":
        correct()
    else:
        incorrect()
        


print ("Hello! Welcome to this Card Game!")
time.sleep (1)
print ("")
print ("You will be given a selection of cards.")
time.sleep (1)
print("")
print ("You will draw the 1st card...")
time.sleep (1)
print ("")
print ("Next, you will determine whether the following card will be higher or lower than the card that has been drawed...")
print ("")
time.sleep (1)
print ("Note that the game is to guess THE 'VALUE' OF THE CARD, NOT THE TYPE!")
print ("e.g: 2 Diamonds. Make sure you only predict whether the value (the number) of the card, not the type, (Diamonds, Spades, etc) or else you will lose!")
print ("Draw the next card...")
time.sleep (1)
print ("If you were correct, then your score will increase by 1.")
time.sleep (1)
print ("")
print ("If you are incorrect, well then, your score is not affected and that is just bad luck :-)")
time.sleep (1)
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
round = 4
score = 0
type = ("Hearts", "Spades", "Clubs", "Diamonds")
print ("Choose a card deck selection difficulty!")
print ("Type the letter 'e' for easy!")
print ("Type the letter 'h' for hard!")
deck_choice = input()

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

answers = ["h", "l", "s"]
while round != 0:

  if deck_choice == "e":
      easy_deck = random.randrange(5)
      time.sleep(1)
      print ("OK! Since you have chosen the 'easy' level, you will have 5 cards to guess...")
      time.sleep(1)
      print ("")
      ready = input("Type the word 'Ready' when you are prepared to play!")
      time.sleep(1)
      print ("")
      print ("Your first card is", easy_deck1, random.choice(type))
      time.sleep(1)
      print("")
      time.sleep(1)
      print ("")

      predict1 = valid_predict("second")
      checking(easy_deck2,easy_deck3,predict1)

      predict2 = valid_predict("third")
      checking(easy_deck3,easy_deck4,predict2)
        
      predict3 = valid_predict("fourth")
      checking(easy_deck4,easy_deck5,predict3)

      predict4 = valid_predict("fifth")
      checking(easy_deck5,easy_deck6,predict4)
      
      predict5 = valid_predict("sixth")
      checking(easy_deck6,easy_deck7,predict5)

      time.sleep(1)
      print ("")
      print ("AND...")
      time.sleep(1)
      print ("")
      print ("That is the end of the game! You achieved a score of", score, "/5!")
      break
  
  if deck_choice == "h":
    print ("OK! Since you have chosen the 'hard' level, you will have 10 cards to guess...")
    print ("")
    print ("Note this before you start...")
    print ("")
    time.sleep(2)
    print ("As this is a 'hard' level, then instead of a normal card deck which has the range of 2 to 10...")
    print ("")
    time.sleep(1.5)
    print ("There will be a range between 2 and 20!")
    time.sleep(1)
    print ("")
    ready = input("Type the word 'Ready' when you are prepared to play!")
    time.sleep(1)
    print ("")
    print ("Your first card is", hard_deck1, random.choice(type))
    time.sleep(1)
    print("")
    time.sleep(1)
    print ("")

    predict1 = valid_predict("second")
    checking(hard_deck2,hard_deck3,predict1)

    predict2 = valid_predict("third")
    checking(hard_deck3,hard_deck4,predict2)

    predict3 = valid_predict("fourth")
    checking(hard_deck4,hard_deck5,predict3)

    predict4 = valid_predict("fifth")
    checking(hard_deck5,hard_deck6,predict4)

    predict5 = valid_predict("sixth")
    checking(hard_deck6,hard_deck7,predict5)

    predict6 = valid_predict("seventh")
    checking(hard_deck7,hard_deck8,predict6)

    predict7 = valid_predict("eigth")
    checking(hard_deck8,hard_deck9,predict7)

    predict8 = valid_predict("ninth")
    checking(hard_deck9,hard_deck10,predict8)

    predict9 = valid_predict("final")
    checking(hard_deck10,hard_deck11,predict9)

    print ("AND...")
    time.sleep(1)
    print ("")
    print ("That is the end of the game! You achieved a score of", score, "/10!")
    break