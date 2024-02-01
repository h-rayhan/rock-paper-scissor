"""
    Author: Rayhan Hossain
    Date created: 01/02/2024
    Last modified: 01/02/2024
    Python Version: 3.12
"""

from hand_arts import rock, paper, scissors
import random


def play_game():
    try:
        user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    except ValueError:
        print("Please enter a valid integer.")
        return play_game()

    computer = random.randint(0, 2)

    game_images = [rock, paper, scissors]
    if user >= 3 or user < 0:
        print("You lose! Next time enter a correct number")

    else:
        print(f"You chose:{game_images[user]} \n\nComputer chose: {game_images[computer]}")

        if (user == 0 and computer == 2) or (user > computer):
            print("You win")

        elif (user == 2 and computer == 0) or (user < computer):
            print("You lose")

        elif user == computer:
            print("Draw")


continue_game = True

while continue_game:
    play_game()
    play_again = input("Play again? (y/n): ")

    if play_again.lower() != "y":
        continue_game = False
