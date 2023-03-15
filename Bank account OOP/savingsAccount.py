from currentAccount import CurrentAccount


class SavingsAccount(CurrentAccount):
    balance = 2000

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def get_service(self):
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
                balance = SavingsAccount.balance - int(withdrawal_amount)
                available_balance = balance
                print(f"withdrawal amount:£{withdrawal_amount} \nYour balance is now:£{balance}")
                print(f"Your available balance is now:£{available_balance}")
                return balance
            elif userchoice2 == "2":
                deposit_amount = input("please enter deposit amount:£ ")
                balance = SavingsAccount.balance + int(deposit_amount)
                available_balance = balance
                print(f"deposit amount:£{deposit_amount} \nYour balance is now:£{balance}")
                print(f"Your available balance is now:£{available_balance}")
                return balance
            else:
                available_balance = SavingsAccount.balance
                print(f"your Balance is:£{SavingsAccount.balance}")
                print(f"Your available balance is now:£{available_balance}")
                return SavingsAccount.balance

        return SavingsAccount.balance

    def get_account_type(self):
        print("Account Type: Savings")

    def get_account_num(self, account_num):
        print("Account No: ", account_num)

    def get_account_balance(self, balance):
        print("Account Balance: ", balance)

    def set_interest_rate(self, interest_rate):
        print("Savings account Interest Rate: ", interest_rate)