import random

# list of choices
choices = ["Horse", "Shoe", "Saddle"]

# Randomly selecting the computer choice
computer_choice = random.choice(choices)

computer_choice

# Function to get the players choice

def get_player_choice():
    print("Enter your choice: Horse, Shoe, Saddle")
    player_choice = input().capitalize()
    return player_choice

player_choice = get_player_choice()

def determine_winner(player_choice, compute_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Horse" and computer_choice == "Shoe") or \
        (player_choice == "Shoe" and computer_choice == "Saddle") or \
        (player_choice == "Saddle" and computer_choice == "Horse"):
        return "You win!" 
    else:
        return "You lose!"

# Determine the winner
result = determine_winner(player_choice, computer_choice)

# Display the result and what the computer chose
print(f"Computer chose: {computer_choice}")
print(result)