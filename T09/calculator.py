import operator

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "**": operator.pow,
}

print("\nWelcome to the CALCULATOR program. Choose:")

# The task doesn't ask defensive coding for the choice, but I added it anyway.
while True:
    try:
        print("\n1 - To use the Calculator")
        print("2 - To read all of the equations from a new .txt file\n")
        choice = int(input("What do you want to do?: "))
        assert choice in [1, 2]
        break
    except AssertionError:
        print("Invalid choice! Please enter a valid choice (1 or 2 only).\n")
    except ValueError:
        print("Invalid choice! Text not permited! Please enter a valid choice (1 or 2 only).\n")

if choice == 1:
    print("\nYou have chosen to use the Calculator!")
    while True:
        try:
            num1 = float(input("\nEnter the FIRST number: "))
            num2 = float(input("\nEnter the SECOND number: "))
            operation = input("\nEnter the OPERATION (+, -, *, /, %, **): ")
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

    # write the equation to a text file. I added the T09/ to save the file in the T09 folder.
    # Without the T09 it would save the file in the rood directory of the project.
    with open("T09/results.txt", "a") as f:
        f.write(f"{num1} {operation} {num2} = {result}\n")

else:
    print("\nYou have chosen to read all of the equations from a new .txt file!")
    while True:
        try:
            # Same as above, I added the T09/ to looks for the file in the T09 folder instead of the root directory.
            file_name = input("\nEnter the name of the .txt file: ")

            # the file with a list of equations to read is equations.txt
            with open("T09/"+file_name, "r") as file:
                for line in file:
                    # I learned about and how to use eval() here:
                    # https://www.youtube.com/watch?v=XAYrmGc4ZYM&t=105s&ab_channel=StudySession
                    print(line.strip("\n") + " = " + str(eval(line)))
            break
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")