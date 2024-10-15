import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   WHITE = '\033[97m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


ticket = [["*", "*", "*"],["*", "*", "*"] ,["*", "*", "*"]]


print ("_________________")
print ("|",  ticket[0][0], " | ", ticket[0][1], " | ",ticket[0][2]," |")
print ("|____|_____|_____|")
print ("|", ticket[1][0], " | ", ticket[1][1], " | ", ticket[1][2]," |")
print ("|____|_____|_____|")
print ("|", ticket[2][0], " | ", ticket[2][1], " | ", ticket[2][2]," |")
print ("|____|_____|_____|")



ticket[0][0] = random.randint(0,20)
ticket[0][1] = random.randint(0,20)
ticket[0][2] = random.randint(0,20)
ticket[1][0] = random.randint(0,20)
ticket[1][1] = random.randint(0,20)
ticket[1][2] = random.randint(0,20)
ticket[2][0] = random.randint(0,20)
ticket[2][1] = random.randint(0,20)
ticket[2][2] = random.randint(0,20)

tickets_total = [ticket[0][0], ticket[0][1], ticket[0][2], ticket[1][0], ticket[1][1], ticket[1][2], ticket[2][0], ticket[2][1], ticket[2][2]]

seen = set()
for i, e in enumerate(tickets_total):
    if e in seen:
        tickets_total[i] = random.randint(0,20)
    else:
        seen.add(e)
pos1 = "."
pos2 = "."
pos3 = "."
pos4 = "."
pos5 = "."
pos6 = "."
pos7 = "."
pos8 = "."
pos9 = "."

finish = False


while finish != True: 
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        WHITE = '\033[97m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    print (tickets_total)
    guess = int(input("Input a number: "))
    if guess in tickets_total:
        print ("Yes, that's in the sequence!")
        print (guess)
        if guess == ticket[0][0]:
            pos1 = guess
        elif guess == ticket[0][1]:
            pos2 = guess
        elif guess == ticket[0][2]:
            pos3 = guess
        elif guess == ticket[1][0]:
            pos4 = guess
        elif guess == ticket[1][1]:
            pos5 = guess
        elif guess == ticket[1][2]:
            pos6 = guess
        elif guess == ticket[2][0]:
            pos7 = guess
        elif guess == ticket[2][1]:
            pos8 = guess
        elif guess == ticket[2][2]:
            pos9 = guess
    else:
        print ("No, that's not in the sequence!")

        print (tickets_total)
        
        result = [[pos1, pos2, pos3],
                  [pos4, pos5, pos6],
                  [pos7, pos8, pos9]]
    print ("")
    print (pos1,pos2,pos3)
    print (pos4,pos5,pos6)
    print (pos7,pos8,pos9)

    if type(pos1) is int and type(pos2) is int and type(pos3) is int:
        print ("You have won!")
        print (color.YELLOW, pos1,pos2,pos3, color.END)
        print (pos4,pos5,pos6)
        print (pos7,pos8,pos9)
        finish = True
       
        print ("_________________")
        print ("|",color.YELLOW, pos1, color.END,  "|",color.YELLOW, pos2,color.END, "|",color.YELLOW, pos3, color.END, "|")
        print ("|_____|_____|_____|")
        print ("|", pos4, "  |", pos5, " |", pos6,"  |")
        print ("|____|_____|_____|")
        print ("|", pos7, " | ", pos8, " | ", pos9," |")
        print ("|____|_____|_____|")

        
    elif type(pos4) is int and type(pos5) is int and type(pos6) is int:
        print ("You have won!") 
        print (color.WHITE, pos1,pos2,pos3, color.END)
        print (color.YELLOW, pos4,pos5,pos6, color.END)
        print (color.WHITE, pos7,pos8,pos9, color.END)
        finish = True
        
    elif type(pos7) is int and type(pos8) is int and type(pos9) is int:
        print ("You have won!")   
        print (pos1,pos2,pos3)
        print (pos4,pos5,pos6)
        print (color.YELLOW, pos7,pos8,pos9, color.END)
        finish = True
        
    elif type(pos1) is int and type(pos4) is int and type(pos7) is int:
        print ("You have won!") 
        print (color.YELLOW, pos1,color.END, pos2,pos3)
        print (color.YELLOW, pos4,color.END, pos5,pos6)
        print (color.YELLOW, pos7,color.END, pos8,pos9)
        finish = True
        
    elif type(pos2) is int and type(pos5) is int and type(pos8) is int:
        print ("You have won!") 
        print (pos1,color.YELLOW, pos2,color.END, pos3)
        print (pos4,color.YELLOW, pos5,color.END, pos6)
        print (pos7,color.YELLOW, pos8,color.END, pos9)
        finish = True
        
    elif type(pos3) is int and type(pos6) is int and type(pos9) is int:
        print ("You have won!")  
        print (pos1,pos2,color.YELLOW, pos3,color.END)
        print (pos4,pos5,color.YELLOW, pos6,color.END)
        print (pos7,pos8,color.YELLOW, pos9,color.END)
        finish = True
        
    elif type(pos1) is int and type(pos5) is int and type(pos9) is int:
        print ("You have won!")     
        print (color.YELLOW, pos1, color.END,pos2,pos3)
        print (pos4,color.YELLOW, pos5, color.END, pos6)
        print (pos7,pos8,color.YELLOW, pos9, color.END)
        finish = True
        
    elif type(pos3) is int and type(pos5) is int and type(pos7) is int:
        print ("You have won!") 
        print (pos1,pos2,color.YELLOW, pos3,color.END)
        print (pos4,color.YELLOW, pos5,color.END, pos6)
        print (color.YELLOW, pos7,color.END, pos8,pos9)
        finish = True
       