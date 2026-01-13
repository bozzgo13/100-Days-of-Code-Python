def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

decision = "y"
while decision != "x":
    number1 = float(input("What's the first number?: "))
    decision = "y"
    while decision == "y":
        print("+\n-\n*\n/")
        selected_operation = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))

        number1 = operations[selected_operation](number1,number2)

        print(f"Type 'y' to continue calculating with {number1}.")
        print("Type 'n' to start a new calculation.")
        decision = input("Type 'x' to exit the program.\n")
