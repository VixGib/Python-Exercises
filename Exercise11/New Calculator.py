Carry_on = "y"
history = []
print("Hello! Welcome to Vicki's calculator")
while Carry_on != "n":
    def number_list():
        your_num = input("Give me your list of numbers leaving a space inbetween each one: ")
        your_num_list = your_num.split()
        your_num_str_to_int = list(map(int, your_num_list))
        return your_num_str_to_int

    your_numbers = number_list()

    operation = input("please select a function: + - * / : ")
    your_num2 = input(int("Give me one more number: "))

    def operation(op):
        if op in operation == "+":
            for e in number_list():
                equation = ("{0} + {1}".format(e, your_num2))
                total = equation + "=" + (e + your_num2)
                print(total)
                history.append(total)
        elif operation == "-":
            for e in your_numbers:
                equation = ("{0} - {1}".format(e, your_num2))
                total = (f"{equation} {+} "=" {-} (e + your_num2)
                print(total)
                history.append(total)

        elif operation == "*":
            for e in your_numbers:
                equation = ("{0} * {1}".format(e, your_num2))
                history.append(equation)
                print(equation)

        elif operation == "/":
            for e in your_numbers:
                equation = ("{0} / {1}".format (e, your_num2))
                history.append(equation)
                print(equation)
        else:
            print()
        return total


    full_total = calculation()


    Carry_on = input("Would you like to use Vicki's calculator again: y/n? ")
    print("Here are all of your calculations!")
    print("\n".join(history))
print("Thank you for using Vicki's calculator! ")














