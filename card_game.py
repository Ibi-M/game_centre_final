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
        print("\nInvalid Answer!")
        info()
        predict = input(prompt_message).strip().lower()
   
    return predict


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

      predict2 = valid_predict("second")

      print ("")
      print ("The next card is:", easy_deck3, random.choice(type))
      print ("")
      if easy_deck3 < easy_deck1 and predict2 == "l":
        correct()
      elif easy_deck3 > easy_deck1 and predict2 == "h":
        correct()
      elif easy_deck3 == easy_deck1 and predict2 == "s":
        correct()
      else:
        incorrect()
        
      time.sleep(1)
      print ("")

      predict3 = valid_predict("third")

      print ("")
      print ("The next card is:", easy_deck4, random.choice(type))
      print ("")
      if easy_deck4 < easy_deck3 and predict3 == "l":
        correct()
      elif easy_deck4 > easy_deck3 and predict3 == "h":
        correct()
      elif easy_deck4 == easy_deck3 and predict3 == "s":
        correct()
      else:
        incorrect()
        
      time.sleep(1)
      print ("")

      predict4 = valid_predict("fourth")

      print ("")
      print ("The next card is:", easy_deck5, random.choice(type))
      print ("")
      if easy_deck5 < easy_deck4 and predict4 == "l":
        correct()
      elif easy_deck5 > easy_deck4 and predict4 == "h":
        correct()
      elif easy_deck5 == easy_deck4 and predict4 == "s":
        correct()
      else:
        incorrect()
        
      time.sleep(1)
      print ("")

      predict5 = valid_predict("fifth")

      print ("")
      print ("The next card is:", easy_deck6, random.choice(type))
      print ("")
      if easy_deck6 < easy_deck5 and predict5 == "l":
        score = score + 1
        round = round - 1
        time.sleep(1)
        print ("You have guessed correctly!")
        print ("Your score is now", score)
      elif easy_deck6 > easy_deck5 and predict5 == "h":
        correct()
      elif easy_deck6 == easy_deck5 and predict5 == "s":
        correct()
      else:
        incorrect()
        
      time.sleep(1)
      print ("")
      
      predict6 = valid_predict("sixth")

      print ("")
      print ("The next card is:", easy_deck7, random.choice(type))
      print ("")
      if easy_deck7 < easy_deck6 and predict6 == "l":
        correct()
      elif easy_deck7 > easy_deck6 and predict6 == "h":
        correct()
      elif easy_deck7 == easy_deck6 and predict6 == "s":
        correct()
      else:
        incorrect()
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

    predict2 = valid_predict("second")

    print ("The next card is:", hard_deck3, random.choice(type))
    print ("")
    if hard_deck3 < hard_deck1 and predict2 == "l":
      correct()
    elif hard_deck3 > hard_deck1 and predict2 == "h":
      correct()
    elif hard_deck3 == hard_deck1 and predict2 == "s":
      correct()
    else:
      incorrect()
        
    time.sleep(1)
    print ("")

    predict3 = valid_predict("third")

    print ("The next card is:", hard_deck4, random.choice(type))
    print ("")
    if hard_deck4 < hard_deck3 and predict3 == "l":
      correct()
    elif hard_deck4 > hard_deck3 and predict3 == "h":
      correct()
    elif hard_deck4 == hard_deck3 and predict3 == "s":
      correct()
    else:
      incorrect()
        
    time.sleep(1)
    print ("")

    predict4 = valid_predict("fourth")

    print ("The next card is:", hard_deck5, random.choice(type))
    print ("")
    if hard_deck5 < hard_deck4 and predict4 == "l":
      correct()
    elif hard_deck5 > hard_deck4 and predict4 == "h":
      correct()
    elif hard_deck5 == hard_deck4 and predict4 == "s":
      correct()
    else:
      incorrect()
        
    time.sleep(1)
    print ("")

    predict5 = valid_predict("fifth")

    print ("The next card is:", hard_deck6, random.choice(type))
    print ("")
    if hard_deck6 < hard_deck5 and predict5 == "l":
      correct()
    elif hard_deck6 > hard_deck5 and predict5 == "h":
      correct()
    elif hard_deck6 == hard_deck5 and predict5 == "s":
      correct()
    else:
      incorrect()

    time.sleep(1)
    print ("")

    predict6 = valid_predict("sixth")

    print ("The next card is:", hard_deck8, random.choice(type))
    print ("")
    if hard_deck8 < hard_deck7 and predict6 == "l":
      correct()
    elif hard_deck8 > hard_deck7 and predict6 == "h":
      correct()
    elif hard_deck8 == hard_deck7 and predict6 == "s":
      correct()
    else:
      incorrect()
      
    time.sleep(1)
    print ("")

    predict7 = valid_predict("seventh")

    print ("The next card is:", hard_deck9, random.choice(type))
    print ("")
    if hard_deck9 < hard_deck8 and predict7 == "l":
      correct()
    elif hard_deck9 > hard_deck8 and predict7 == "h":
      correct()
    elif hard_deck9 == hard_deck8 and predict7 == "s":
      correct()
    else:
      incorrect()
        
    time.sleep(1)
    print ("")

    predict8 = valid_predict("eigth")

    print ("The next card is:", hard_deck10, random.choice(type))
    print ("")
    if hard_deck10 < hard_deck9 and predict8 == "l":
      correct()
    elif hard_deck10 > hard_deck9 and predict8 == "h":
      correct()
    elif hard_deck10 == hard_deck9 and predict8 == "s":
      correct()
    else:
      incorrect()
      
    time.sleep(1)
    print ("")

    predict9 = valid_predict("ninth")

    print ("The next card is:", hard_deck11, random.choice(type))
    print ("")
    if hard_deck11 < hard_deck10 and predict9 == "l":
      correct()
    elif hard_deck11 > hard_deck10 and predict9 == "h":
      correct()
    elif hard_deck11 == hard_deck10 and predict9 == "s":
      correct()
    else:
      incorrect()
      
    time.sleep(1)
    print ("")

    predict10 = valid_predict("final")

    print ("The next card is:", hard_deck12, random.choice(type))
    print ("")
    if hard_deck12 < hard_deck11 and predict10 == "l":
      correct()
    elif hard_deck12 > hard_deck11 and predict10 == "h":
      correct()
    elif hard_deck12 == hard_deck11 and predict10 == "s":
      correct()
    else:
      incorrect()
    time.sleep(1)
    print ("")
    print ("AND...")
    time.sleep(1)
    print ("")
    print ("That is the end of the game! You achieved a score of", score, "/10!")
    break