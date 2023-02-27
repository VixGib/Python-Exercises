import random
choices = ["ROCK", "PAPER", "SCISSORS"]
while True:
    print("Welcome to ROCK, PAPER, SCISSORS!")

    player_choice = input("Make your choice [ROCK, PAPER, SCISSORS]: ").upper()

    computer_choice = random.choice(choices)

    print(f"you chose: {player_choice},\ncomputer chose: {computer_choice}")

    if player_choice == "ROCK":
        if computer_choice == "SCISSORS":
            print(f"Rock blunts Scissors! you win!")
        elif computer_choice == "ROCK":
            print(f"you both chose Rock it's a tie!")
        else:
            print(f"Paper wraps Rock! you loose!")

    elif player_choice == "PAPER":
        if computer_choice == "ROCK":
            print(f"Paper wraps Rock! you win!")
        elif computer_choice == "PAPER":
            print(f"you both chose Paper! it's a tie!")
        else:
            print(f"Scissors cut Paper! you loose!")

    elif player_choice == "SCISSORS":
        if computer_choice == "PAPER":
            print(f"Scissors cut Paper! you win!")
        elif computer_choice == "SCISSORS":
            print(f"you both chose Scissors it's a tie!")
        else:
            print(f"Rock blunts Scissors! you loose!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thankyou for playing, come back soon!")
        break