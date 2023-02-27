import random


def welcome_user(player_1):
    print(f"Hi! {player_1}")


def player_choice(choice):
    if choice == "R":
        print("you chose Rock!")
    elif choice == "P":
        print("you chose Paper!")
    elif choice == "S":
        print("you chose Scissors!")
    else:
        print("This is not a valid choice!")
    return choice


def player_choice_num(choice):
    if choice == "R":
        choice = 0
    elif choice == "P":
        choice = 1
    elif choice == "S":
        choice = 2
    return choice


def computer_choice(choice):
    if choice == 0:
        print("computer chose Rock!")
    elif choice == 1:
        print("computer chose Paper!")
    elif choice == 2:
        print("computer chose Scissors!")
    else:
        print("This is not a valid choice!")
    return choice


def declare_winner(player, computer):
    if player == computer:
        if player == 0 and computer == 0:
            print(f"Its a tie! you both chose Rock! ")
        elif player == 1 and computer == 1:
            print(f"Its a tie! you both chose Paper! ")
        elif player == 2 and computer == 2:
            print(f"Its a tie! you both chose Scissors! ")
    elif player == 0 and computer == 1:
        print(f"Computer Wins! Paper wraps Rock!")
    elif player == 0 and computer == 2:
        print(f"You win! Rock blunts scissors!")
    elif player == 1 and computer == 0:
        print(f"You win! Paper wraps Rock!")
    elif player == 1 and computer == 2:
        print(f"Computer wins! Scissors cut Paper!")
    elif player == 2 and computer == 0:
        print(f"Computer wins! Rock blunts Scissors!")
    elif player == 2 and computer == 1:
        print(f"You win! Scissors cut Paper!")


name = input("Welcome to Rock, Paper, Scissors! What is your name?: ")
welcome_user(name.title())

play = "y"
while play:

    user_selection = input("Please choose R for Rock, P for Paper or S for Scissors: ")

    player = player_choice_num(player_choice(user_selection.upper()))

    computer_selection = random.randint(0, 2)

    computer = computer_choice(computer_selection)

    declare_winner(player, computer)

    play_again = input("Would you like to play again? Y/N  ")
    if play_again.lower() != "y":
        print("Thankyou for playing, come back soon!")
        break
