number_one = int(input("Insert the first number: "))
number_two = int(input("Insert the second number: "))


def operation_select():
    print("-------------------------------------------------")
    print("Select the desired operation: 1 - addition;      ")
    print("                              2 - subtraction;   ")
    print("                              3 - multiplication;")
    print("-------------------------------------------------")
    selected = int(input("Insert the option: "))
    return selected


operation = operation_select()

while operation < 1 or operation > 3:
    print("Please select one option [1, 2 or 3]")
    operation = operation_select()

result = 0
if operation == 1:
    result = number_one + number_two

elif operation == 2:
    result = number_one - number_two

elif operation == 3:
    result = number_one * number_two

print("The result of the operation is: ", result)
