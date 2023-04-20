# Since in theory, there were no classes about 'WHILE' or 'FUNCTIONS' till this point,
# I believe I need to solve this using IF statement.

# For this task, assume that you have been approached by a small financial company and asked
# to create a program that allows the user to access two different financial calculators:
# an investment calculator and a home loan repayment calculator.

# At the top of the file include the line: import math
import math

# The user should be allowed to choose which calculation they want to do.
print("\n_______________________________________________________________________________________________________")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("_______________________________________________________________________________________________________\n")

# How the user capitalises their selection should not affect how the program proceeds. i.e.
# ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’, ‘INVESTMENT’, etc., should all be
# recognised as valid entries.
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if user_choice == "investment":
    # if the user selects investment, asks for the amount of money, the interest rate, how long the user
    # plan to invest and if it's using 'single' or 'compound' interest.
    amount = float(input("\nWhat is the amount of money that you are depositing: "))
    interest_rate = float(input("What is the interest rate (don't need to add %): "))
    time = int(input("How long do you intend to keep investing (in years): "))

    print("\n_______________________________________________________________________________________________________")
    print("simple   - simple interest is calculated on the original (principal) amount")
    print("compound - compound interest is calculated on the original amount and on the interest already accumulated "
          "on it")
    print("_______________________________________________________________________________________________________\n")

    interest = input("Enter either 'simple' or 'compound' from the menu above to proceed: ").lower()

    # Calculating and printing the total amount if user selects simple interest
    if interest == "simple":
        # The total amount when simple interest is applied is calculated as follows: A = P*(1 + r*t)
        total_amount = amount * (1 + (interest_rate / 100) * time)
        total_amount = round(total_amount, 2)

        print("\n================================ TOTAL AMOUNT USING SIMPLE INTEREST ================================")
        print(f"If you invest £{amount}, after {time} years, at {interest_rate}% using simple interest, you will "
              f"get a TOTAL of: £{total_amount}")
        print("====================================================================================================")

    # Calculating and printing the total amount if user selects compound interest
    elif interest == "compound":
        # The total amount when compound interest is applied is calculated as follows: A = P * math.pow((1+r),t)
        total_amount = amount * math.pow((1 + (interest_rate / 100)), time)
        total_amount = round(total_amount, 2)

        print("\n=============================== TOTAL AMOUNT USING COMPOUND INTEREST ===============================")
        print(f"If you invest £{amount}, after {time} years, at {interest_rate}% using compound interest, you will "
              f"get a TOTAL of: £{total_amount}")
        print("====================================================================================================")

    # If the user doesn’t type in a valid input, show an appropriate error message.
    else:
        print("\nERROR: Invalid Option! The only valid options are 'simple' or 'compound'!")

elif user_choice == "bond":
    # If the user selects ‘bond’, ask the user to input:
    house_value = float(input("\nWhat is the present value of the house: "))
    interest_rate = float(input("What is the interest rate: "))
    months = int(input("In how many months do you plan to take to repay the bond: "))

    # The amount that a person will have to be repaid on a home loan each month is calculated as follows:
    # repayment = (i * P)/(1 - (1 + i)**(-n))
    repayment = (((interest_rate / 100) / 12) * house_value) / (1 - (1 + ((interest_rate / 100) / 12)) ** (- months))
    repayment = round(repayment, 2)

    # Calculate how much money the user will have to repay each month and output the answer.
    print("\n=================================== BOND PAYOFF MONTHLY PAYMENT ===================================")
    print(f"Your monthly payment value for the bond purchase of property is: £{repayment}")
    print("=====================================================================================================")

else:
    # If the user doesn’t type in a valid input, show an appropriate error message.
    print("\nERROR: Invalid Option! The only valid options are 'investment' or 'bond'!")
