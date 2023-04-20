# Create a simple calculator application that asks a user to enter two numbers and the operation (e.g. +, -, x, etc.)
# that they’d like to perform on the numbers. Display the answer to the equation. Every equation entered by the user
# should be written to a text file.
# Use defensive programming to write this program in a manner that is robust and handles unexpected events and user inputs.

import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.pow
}
print("Welcome to the CALCULATOR!")

while True:
    try:
        num1 = float(input("\nEnter the FIRST number: "))
        num2 = float(input("\nEnter the SECOND number: "))
        operation = input("\nEnter the OPERATION (+, -, *, /, %, ^): ")
        assert operation in operations
        break
    except ValueError:
        print("Invalid number. Please enter a valid number.\n")
    except AssertionError:
        print("Invalid operation. Please enter a valid operation.\n")
    
# perform the calculation
result = operations[operation](num1, num2)

# display the result
print("\nResult: ", result)

# write the equation to a text file
with open("results.txt", "w") as f:
    f.write(f"{num1} {operation} {num2} = {result}\n")