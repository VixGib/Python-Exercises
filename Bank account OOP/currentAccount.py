
class CurrentAccount:
    balance = 500

    def __init__(self, an_firstname, an_lastname):
        self._firstname = an_firstname
        self._lastname = an_lastname

    def __str__(self):
        return "Account Name: " + self._firstname + " " + self._lastname

    def get_pin(self):
        print("Welcome to Vicki's ATM")

        pin_num = 2468
        trials = 3
        while trials != 0:
            supplied_pin = int(input("please enter your pin number: "))
            if supplied_pin != pin_num:
                trials -= 1
                print("incorrect pin number! you have", trials, "trials left")
            else:
                print("pin number correct")
                trials = 0

    def get_service(self):
        overdraft = 1500
        choice = ["y", "n"]
        userchoice = input("Would you like a service y/n ? ").lower()

        while userchoice not in choice:
            print("This is not a valid choice!")
            userchoice = input("Would you like a service y/n ? ").lower()

        if userchoice == "n":
            print("Here are your account details \nThankyou for using Vicki's ATM!")

        elif userchoice == "y":
            choice2 = ["1", "2", "3"]
            userchoice2 = input("please select service:\n1 = withdrawal\n2 = deposit\n3 = balance :").lower()

            while userchoice2 not in choice2:
                print("This is not a valid choice!")
                userchoice2 = input("please select service:\n1 = withdrawal\n2 = deposit\n3 = balance :").lower()

            if userchoice2 == "1":
                withdrawal_amount = int(input("please enter withdrawal amount: "))
                balance = CurrentAccount.balance - int(withdrawal_amount)
                available_balance = CurrentAccount.balance + overdraft
                print(f"withdrawal amount:£{withdrawal_amount} \nYour balance is now:£{balance}")
                print(f"Your available balance is now:£{available_balance}")
                return balance
            elif userchoice2 == "2":
                deposit_amount = input("please enter deposit amount:£ ")
                balance = CurrentAccount.balance + int(deposit_amount)
                available_balance = balance + overdraft
                print(f"deposit amount:£{deposit_amount} \nYour balance is now:£{balance}")
                print(f"Your available balance is now:£{available_balance}")
                return balance
            else:
                available_balance = CurrentAccount.balance + overdraft
                print(f"your Balance is:£{CurrentAccount.balance}")
                print(f"Your available balance is now:£{available_balance}")
                return CurrentAccount.balance



    def get_email(self, email):
        print("Customer email: ", email)

    def get_phone_num(self, phone_num):
        print("Customer phone No: ", phone_num)

    def get_account_type(self):
        print("Account Type: Current")

    def get_account_num(self, account_num):
        print("Account No: ", account_num)

    def get_account_balance(self, balance):
        print("Account Balance: ", balance)

    def set_interest_rate(self, interest_rate):
        print("Current account Interest Rate: ", interest_rate)
