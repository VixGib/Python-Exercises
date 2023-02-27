carry_on = "y"
print("Hello! Welcome to Vicki's calculator")
while carry_on != "n":
    number1 = int(input("Please select a number "))
    operation = input("please select a function: + - * / ")
    number2 = int(input("please select another number "))

    if operation == "+":
        print(number1 + number2)
        carry_on = input("continue to use calculator y/n ")

    elif operation == "-":
        print(number1 - number2)
        carry_on = input("continue to use calculator y/n ")
    elif operation == "*":
        print(number1 * number2)
        carry_on = input("continue to use calculator y/n ")
    elif operation == "/":
        print(number1 / number2)
        carry_on = input("continue to use calculator y/n ")
print("Thank you for using Vicki's calculator")











