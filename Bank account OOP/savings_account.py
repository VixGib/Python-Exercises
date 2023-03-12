from current_account import CurrentAccount


class SavingsAccount(CurrentAccount):

    def get_pin(self):
        print("Welcome to Vicki's savings account ATM")
        trials = 3
        pin_num = 1234
        withdrawal = 0
        deposit = 0
        balance = 2000
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
                        print(f"withdrawal amount:£{withdrawal_amount}\nYour balance is now:£{balance}")
                        trials = 0
                    elif userchoice2 == "2":
                        deposit_amount = input("please enter deposit amount: ")
                        balance = balance + int(deposit_amount)
                        print(f"deposit amount:£{deposit_amount} \nYour balance is now:£{balance}")
                        trials = 0
                    else:
                        print(f"your Balance is:£{balance} ")
                        trials = 0
                        break


    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def get_account_type(self):
        print("Account Type: Savings")

    def get_account_num(self, account_num):
        print("Account No: ", account_num)

    def get_account_balance(self, balance):
        print("Account Balance: ", balance)

    def set_interest_rate(self, interest_rate):
        print("Savings account Interest Rate: ", interest_rate)