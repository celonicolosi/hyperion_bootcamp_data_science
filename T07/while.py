# This is a program that asks the user to input numbers
# The program stops as soon user type -1
# Then the average of all the numbers the user inputted is printed on the screen

# declaring the variables that will store the sum of the numbers and how many numbers the user inputted
total = 0
count = 0

print("\nThis program will calculate the average of all positive numbers you type!")
print("To stop the program and get the average type -1\n")

# Make use of the while loop repetition structure to implement the program.
# P.S: I hope this simple while is enough
while True:
    # Ask the user to enter a number inside the while loop
    user_number = int(input("Please, enter a number (type -1 to stop): "))
    # When the user enters -1, the program should stop requesting the user to enter a number
    if user_number == -1:
        break
    total += user_number
    count += 1

if count == 0:
    # Extra message in case the first number typed is -1
    print("\nNo numbers were entered.")
else:
    # The program must then calculate the average of the numbers entered, excluding the -1.
    average = total / count
    print("\nThe average of the entered numbers is:", "%0.2f" % average)
    # I learned how to format a decimal number to show just 2 numbers here:
    # https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places

    # QUESTION TO THE REVIEWER
    # In a previous task (T05 - finance_calculator.py) I used: round(float, 2) to get just two decimals
    # in the float but this one that I used above looks like it does the same. Which one is correct?
    # OR Which one is better? OR Is there a better way to do this?
