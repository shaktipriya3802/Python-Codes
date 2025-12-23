# Prints the logo from the file "art.py"
from art import logo
print(logo)

# Defining the Mathematical Operations
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

# Assigning the Mathematical Symbols its Respective Functions
Operations={"+":add,
            "-":subtract,
            "*":multiply,
            "/":divide
            }

yes_or_no=False
num1 = float(input("What's the first number?: ")) # User Input 1
while yes_or_no == False:
    for symbol in Operations:  # Prints the symbols so, the user can select from the set of options
        print(symbol)
    pick_op = input("Pick an Operation: ") # User's selected symbol
    num2 = float(input("What's the next number?: ")) # User Input 2
    output = Operations[pick_op](num1, num2) # Stores the result
    print(num1, pick_op, num2, "=", output) # Prints the output once the user enters the respective value & symbol

    # Asks the user if he/she wants to continue next operation with the current output or not
    continue_or_not = input("Type 'y' to continue calculating with the current output or type 'n' to start a new calculation:").lower()
    if continue_or_not == "y":
        num1=output
    elif continue_or_not=="n":
        print("\n"*100) # prints in a new page
        print(logo)
        num1=float(input("What's the first number?: "))
    else:
        yes_or_no = True
