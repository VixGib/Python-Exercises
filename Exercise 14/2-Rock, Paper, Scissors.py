import random


def welcome_user():
    player = input("Welcome to Rock, Paper, Scissors! What is your name?: ")
    print(f"Hi {player.title()}!")


def player_choice():
    choices = ["R", "P", "S"]
    player_selection = input("Please choose R for Rock, P for Paper or S for Scissors: ").upper()
    while player_selection not in choices:
        print("This is not a valid input!")
        player_selection = input("Please choose R for Rock, P for Paper or S for Scissors: ").upper()

    if player_selection == "R":
        print("you chose Rock!")
    elif player_selection == "P":
        print("you chose Paper!")
    elif player_selection == "S":
        print("you chose Scissors!")

    return player_selection


def computer_choice():
    choices = ["R", "P", "S"]
    computer_selection = random.choice(choices)
    choice = computer_selection

    if choice == "R":
        print("computer chose Rock!")
    elif choice == "P":
        print("computer chose Paper!")
    elif choice == "S":
        print("computer chose Scissors!")
    else:
        print("This is not a valid choice")
    return choice


def declare_winner(player, computer):
    if player == computer:
        print(f"Its a tie!")
    elif player == "R" and computer == "P":
        print(f"Computer Wins! Paper wraps Rock!")
    elif player == "R" and computer == "S":
        print(f"You win! Rock blunts scissors!")
    elif player == "P" and computer == "R":
        print(f"You win! Paper wraps Rock!")
    elif player == "P" and computer == "S":
        print(f"Computer wins! Scissors cut Paper!")
    elif player == "S" and computer == "R":
        print(f"Computer wins! Rock blunts Scissors!")
    elif player == "S" and computer == "P":
        print(f"You win! Scissors cut Paper!")
    else:
        print("Better Luck Next Time!")
    return player, computer


play = "y"
while play == "y":

    welcome_user()

    player_1 = player_choice()

    computer_1 = computer_choice()

    declare_winner(player_1, computer_1)

    play_again = input("Would you like to play again? Y/N  ")
    if play_again.lower() != "y":
        play = "n"
        print("Thankyou for playing, come back soon!")







