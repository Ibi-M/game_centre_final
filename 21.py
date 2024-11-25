from colorama import *
init(autoreset=True)

class color:
    UNDERLINE = '\033[4m'

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

print (f"{Fore.BLUE} Testing {Fore.RESET}")

def get_player_turn(player): #Function - Gets each players input and checks if its valid
    while True:
        try:
            count = int(input(f"\n{player}, how many numbers will you say (1, 2, or 3)? "))
            if 1 <= count <= 3: # Checks if the player input is in valid range
                return count
            else:
                print(f"{Fore.RED} Invalid choice! Please choose a number between 1 and 3. {Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Invalid input! Please enter a number.{Fore.RESET}")
            print("")

print (f"{color.UNDERLINE + Style.BRIGHT} You are going to play 21!")

players = []
for i in range(2): # Gathers the players' names
    while True:
        name = input(f"\nEnter name for Player {i + 1}:")
        if name:
            players.append(name)
            break
        else:
            print(f"{Fore.RED} Player name cannot be empty. Please enter a valid name.\n")

current_number = 0
player_index = 0
    
while current_number <= 21: # Loop until number reaches 21
    player = players[player_index]
    count = get_player_turn(player)

    current_number = current_number + count
    print(f"{Style.BRIGHT + Fore.BLUE + player + Fore.RESET + Style.BRIGHT} chose to say {Fore.GREEN + str(count) + Style.BRIGHT} numbers.")
    print(f"{Style.BRIGHT + Fore.YELLOW}The current count is {str(current_number)}")

    if current_number >= 21:
        print(f"\n{Fore.GREEN + player} says 21 and loses the game!")
        
    player_index = (player_index + 1) % len(players)