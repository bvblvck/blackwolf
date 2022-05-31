import random

while True:
    user_name = input('what is your name? ')
    print(f'welcome {user_name}, to rock, paper and scissors')
    user_action = input("rock, paper or scissors? ")
    actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(actions)
    print(f"You chose {user_action}, computer chose {computer_action}.")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print(f'thanks for playing {user_name}, do have a nice day')
        break
