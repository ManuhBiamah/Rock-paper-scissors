import random

total_games = int(input("Enter the number of times you want to play the game: "))
possible_actions = ("rock", "paper", "scissors")
computer_wins = 0
user_wins = 0

for _ in range(total_games):
    user_action = input("Enter a choice: rock, paper, or scissors\n")
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_wins += 1
        else:
            print("Paper covers rock! You lose.")
            computer_wins += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_wins += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_wins += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_wins += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_wins += 1

print("\nGame results:")
print(f"Computer wins: {computer_wins}")
print(f"User wins: {user_wins}")

if computer_wins > user_wins:
    print("Computer is the winner!")
elif user_wins > computer_wins:
    print("You are the winner!")
else:
    print("It's a tie!")
