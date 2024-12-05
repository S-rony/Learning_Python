from art import logo

def add(n1, n2):
    return n1 + n2

# Todo: Write out the other 3 functions - subtract, multiply and divide.

def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

# Todo: Add these 4 functions into a dictionary as the value. keys = "+","-","*","/"
operations = {}
operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide

#Todo: Use the Dictionary operations to perform operations. Multiply 4 * 8 using the dictionary
# print(operations["*"](4,8))
def calculator():
    print(logo)
    operation_repeat = True
    first_number = float(input("What's the first number?: "))
    while operation_repeat:

        print("+")
        print("-")
        print("*")
        print("/")
        pick_operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        output = operations[pick_operation](first_number,next_number)
        print(f"{first_number} {pick_operation} {next_number} = {output}")
        repeat = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ").lower()
        if repeat == "n":
            operation_repeat = False
            print("\n"*10)
            calculator()
        elif repeat == "y":
            first_number = output
            operation_repeat = True
calculator()












