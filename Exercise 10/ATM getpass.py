import getpass
print("Welcome to Vicki's ATM")
# set variables, pin number and number of trials
# number of trials or attempts
trials = 3
# set the pin number
pin_num = 2468
# keep this running by creating a while loop, set while statement while the number of trials are not = to (!=) 0, keep the loop running
while trials != 0:
# ask for the pin number. change string into an interger
    supplied_pin = int(getpass.getpass("please enter your pin number: "))
# set the if statement, if pin does not = pin number (!=) tell them and how many trials left
    if supplied_pin != pin_num:
        # first reduce the trials by 1
        trials -= 1
        # print out incorrect pin plus the number of trials they have left
        print("incorrect pin number! you have", trials, "trials left")
        # if the pin number is does = pin number print pin correct
    else:
        print("pin number correct")
        # give user a choice of what to do next, would they like another service
        UserChoice = input("Would you like another service y/n ? ")
        # if they say no leave message and break loop
        if UserChoice == "n":
            print("Thankyou for using Vicki's ATM")
            trials = 0
        # if they say yes ask what other service then break loop (would go on further if we developed code)
        if UserChoice == "y":
            print("please select another service")
            trials = 0


