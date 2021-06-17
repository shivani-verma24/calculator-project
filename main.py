from art import logo

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator():
    print(logo)
    a = float(input("What's the first number?: "))

    while (True):

        c = input("+ \n- \n* \n/ \nPick an operation: ")
        b = float(input("What's the next number?: "))

        if (c == '+'):
            ans = add(a, b)
        elif (c == '-'):
            ans = subtract(a, b)
        elif (c == '*'):
            ans = multiply(a, b)
        else:
            ans = divide(a, b)
        print(f"{a} {c} {b} = {ans}")

        choice = input(f"type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: \n")

        if (choice == 'y'):
            a = ans
            continue
        elif (choice == 'n'):
            calculator()
        else:
            break

calculator()

# Project by Shivani Verma