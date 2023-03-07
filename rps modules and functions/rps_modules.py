import random
from rps_functions import *


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
        