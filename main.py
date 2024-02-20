# Generate documentation for the code using the comments and docstrings
import random,re


#Explain in github copilot
def is_valid_username(username):
    # The regex pattern for a valid username
    pattern = "^[a-zA-Z][a-zA-Z0-9]{4,14}$"
    
    # Check if the username matches the pattern
    if re.match(pattern, username):
        return True
    else:
        return False
# generate doc for this function
def rock_paper_scissors():
    player_name = input("Enter your name: ")
    while not player_name.strip():
        print("Invalid name. Please try again.")
        player_name = input("Enter your name: ")

    print("Hello, " + player_name + "! Let's play Rock, Paper, Scissors.")

    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (rock, paper, scissors): ")
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ")

    print("Computer chose: ", computer_choice)

    # let's add some cool message if the user wins or loses !
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

print(rock_paper_scissors())