Carry_on = "y"
history = []
print("Hello! Welcome to Vicki's calculator")
while Carry_on != "n":
    your_num = input("Give me your list of numbers leaving a space inbetween each one: ")
# print(your_num)
# makes the string into a list
    your_num_list = your_num.split()
# print(your_num_list)
# Turns the string list into an integer list
    your_num_str_to_int = list(map(int, your_num_list))
# print(str_to_int)
# print(type(str_to_int))

# at this point the numbers given are a list of integers
    operation = input("please select a function: + - * / : ")
    your_num2 = int(input("Give me one more number: "))

    if operation == "+":
        for e in your_num_str_to_int:
            equation = ("{0} + {1}".format(e, your_num2))
            total = equation + " = " + str(e + your_num2)
            history.append(total)
            print(total)

    elif operation == "-":
        for e in your_num_str_to_int:
            equation = ("{0} - {1}".format(e, your_num2))
            total = equation + " = " + str(e - your_num2)
            history.append(total)
            print(total)

    elif operation == "*":
        for e in your_num_str_to_int:
            equation = ("{0} * {1}".format(e, your_num2))
            total = equation + " = " + str(e * your_num2)
            history.append(total)
            print(total)

    elif operation == "/":
        for e in your_num_str_to_int:
            equation = ("{0} / {1}".format(e, your_num2))
            total = equation + " = " + str(e / your_num2)
            history.append(total)
            print(total)
    else:
        print()

    Carry_on = input("Would you like to use Vicki's calculator again: y/n? ")
print("Here are all of your calculations!")
print("\n".join(history))
print("Thank you for using Vicki's calculator! ")














