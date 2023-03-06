from my_functions import *
history = []
print("Hello! Welcome to Vicki's calculator")
Carry_on = "y"


while Carry_on == "y":

    number_list = get_numbers()

    chosen_operation = get_operation()

    second_num = get_second_num()

    full_total = calculation(number_list, chosen_operation, second_num)
    print(full_total)

    Carry_on = input("Would you like to use Vicki's calculator again: y/n? ").lower()

print("Here are all of your calculations!")
print("\n".join(history))
print("Thank you for using Vicki's calculator! ")
