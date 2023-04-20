# This program will be used to validate that a user inputs at least two names when asked to enter their full name.

# Ask the user to input their full name.
full_name = input("Please insert your full name: ")

# Perform some validation to check that the user has entered a full name. Give an appropriate error message if they
# haven’t.

# User didn't type anything.
if full_name == "":
    print("You haven’t entered anything. Please enter your full name.")
# User typed less than 4 characters.
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
# User typed more than 25 characters.
elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
# EXTRA: Verify if user typed at least a name and a surname/lastname (normal for latinos to have more than one
# surname/lastname e.g. Marcelo Nicolosi Santos)
elif len(full_name.split(" ")) < 2:
    print("Please enter your full name.")
else:
    print("Thank you for entering your name.")
