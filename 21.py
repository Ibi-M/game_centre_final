class color: #Class - lists all colors
    PURPLE = '\033[95m'
    DARKCYAN = '\033[36m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def get_player_turn(player): #Function - Gets each players input and checks if its valid
    while True:
        try:
            count = int(input(f"{player}, how many numbers will you say (1, 2, or 3)? "))
            if 1 <= count <= 3: # Checks if the player input is in valid range
                return count
            else:
                print(color.RED + "Invalid choice! Please choose a number between 1 and 3." + color.END)
                print ("")
        except ValueError:
            print(color.RED + "Invalid input! Please enter a number." + color.END)
            print("")

print (color.BOLD + color.UNDERLINE + "You are going to play 21!" + color.END)
print ("")

players = []
for i in range(2): # Gathers the players' names
    while True:
        name = input(f"Enter name for Player {i + 1}: ")
        print ("")
        if name:
            players.append(name)
            break
        else:
            print(color.RED + "Player name cannot be empty. Please enter a valid name." + color.END)
            print ("")

current_number = 0
player_index = 0
    
while current_number <= 21: # Loop until number reaches 21
    player = players[player_index]
    count = get_player_turn(player)

    current_number = current_number + count
    print ("")
    print(color.BOLD + color.DARKCYAN + player + color.END + color.BOLD + " chose to say " + color.GREEN + str(count) + color.END + color.BOLD + " numbers."+ color.END)
    print (color.BOLD + color.YELLOW + "The current count is " + str(current_number), color.END)
    print ("")
        
    if current_number >= 21:
        print(color.PURPLE + player + " says 21 and loses the game!" + color.END)
        
    player_index = (player_index + 1) % len(players)