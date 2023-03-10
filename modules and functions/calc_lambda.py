def get_numbers():
    your_num = input("Give me your list of numbers leaving a space inbetween each one: ")
    your_num_list = your_num.split()
    your_num_str_to_int = list(map(int, your_num_list))
    return your_num_str_to_int


def get_operation():
    operation = input("please select a function: + - * / : ")
    operation_list = ("+", "-", "*", "/")
    while operation not in operation_list:
        print("This is not a valid function!")
        operation = input("please select a function: + - * / : ")
    return operation


def get_second_num():
    your_num2 = int(input("Give me one more number: "))
    while not type(your_num2) == int:
        print("That is not a number!")
        your_num2 = int(input("Give me one more number: "))
    return your_num2


def calculation(num1, operation, num2):
    history = []
    if operation == "+":
        for num in num1:
            equation = "{0} + {1}".format(num, num2)
            total = equation + " = " + str(num + num2)
            history.append(total)

    elif operation == "-":
        for num in num1:
            equation = "{0} - {1}".format(num, num2)
            total = equation + " = " + str(num - num2)
            history.append(total)

    elif operation == "*":
        for num in num1:
            equation = "{0} * {1}".format(num, num2)
            total = equation + " = " + str(num * num2)
            history.append(total)

    elif operation == "/":
        for num in num1:
            equation = "{0} / {1}".format(num, num2)
            total = equation + " = " + str(num / num2)
            history.append(total)

    return history
