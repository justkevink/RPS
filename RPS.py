import random

options = ("rock", "paper", "scissors")

game_play = True

while game_play:

    player = None
    Computer = random.choice(options)

    while player not in options:
        player = input("Select rock, paper, or scissors:")

    print(f"Player: {player}")
    print(f"Computer: {Computer}")

    if player == Computer:
        print("Draw!")
    elif player == "rock" and Computer == "paper":
        print("Computer wins! Try again")
    elif player == "paper" and Computer == "rock":
        print("Player wins!")
    elif player == "scissors" and Computer == "rock":
        print("Computer wins! Try again")
    elif player == "rock" and Computer == "scissors":
        print("Player wins!")
    elif player == "paper" and Computer == "scissors":
        print("Computer wins! Try again")
    elif player == "scissors" and Computer == "paper":
        print("Player wins!")

    if not input("Play again? (y/n): ").lower() == "y":
            game_play = False

print("Thank you for playing! :)")

