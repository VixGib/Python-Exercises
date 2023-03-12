import getpass


class CurrentAccount:

    def get_pin(self):
        print("Welcome to Vicki's current account ATM")

        pin_num = 2468
        withdrawal = 0
        deposit = 0
        balance = 500
        overdraft = 1500
        trials = 3
        while trials != 0:
            supplied_pin = int(input("please enter your pin number: "))
            if supplied_pin != pin_num:
                trials -= 1
                print("incorrect pin number! you have", trials, "trials left")
            else:
                print("pin number correct")
                userchoice = input("Would you like another service y/n ? ")
                if userchoice == "n":
                    print("Here are your account details \nThankyou for using Vicki's ATM!")
                    trials = 0
                if userchoice == "y":
                    userchoice2 = input("please select service:\n1 = withdrawal\n2 = deposit\n3 = balance :").lower()
                    if userchoice2 == "1":
                        withdrawal_amount = int(input("please enter withdrawal amount: "))
                        balance = balance - int(withdrawal_amount)
                        available_balance = balance + overdraft
                        print(f"withdrawal amount:£{withdrawal_amount} \nYour balance is now:£{balance}")
                        print(f"Your available balance is now:£{available_balance}")
                        return balance
                    elif userchoice2 == "2":
                        deposit_amount = input("please enter deposit amount:£ ")
                        balance = balance + int(deposit_amount)
                        available_balance = balance + overdraft
                        print(f"deposit amount:£{deposit_amount} \nYour balance is now:£{balance}")
                        print(f"Your available balance is now:£{available_balance}")
                        return balance
                    else:
                        available_balance = balance + overdraft
                        print(f"your Balance is:£{balance}")
                        print(f"Your available balance is now:£{available_balance}")
                        return balance

        trials = 0



    def __init__(self, an_firstname, an_lastname):
        self._firstname = an_firstname
        self._lastname = an_lastname

    def __str__(self):
        return "Account Name: " + self._firstname + " " + self._lastname

    def get_email(self, email):
        print("Customer email: ", email)

    def get_phone_num(self, phone_num):
        print("Customer phone No: ", phone_num)

    def get_account_type(self):
        print("Account Type: Current")

    def get_account_num(self, account_num):
        print("Account No: ", account_num)

    def get_account_balance(self, balance):
        print("Account Balance: ",balance )


    def set_interest_rate(self, interest_rate):
        print("Current account Interest Rate: ", interest_rate)





