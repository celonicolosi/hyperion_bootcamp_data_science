# Reviewer:
# Even though I'm doing task 4 (T04), the file is named task3.py because
# the Compulsory Task statement asked me to name it that way.

# Design a program that determines the award a person competing in a triathlon will receive.

# Welcoming the user and asking them to input their times in each event
print("\nCongratulations on finishing this triathlon event!")
print("Please inform your times (in minutes) for all the three events.\n")

# Your program should read in the times (in minutes) for all three events of a
# # triathlon, namely swimming, cycling, and running, and then calculate and
# # display the total time taken to complete the triathlon.
swimming = int(input("Swimming: "))
cycling = int(input("Cycling: "))
running = int(input("Running: "))

total_time = swimming + cycling + running
print(f"Your TOTAL TIME is: {total_time} minutes!\n")

# The qualifying time for awards is 100 minutes.
# Display the award that the participant will receive based on the following criteria:
# |   TOTAL TIME                                  |   AWARD                   |
# |   Within qualifying time.                     |   Provincial Colours      |
# |   Within 5 minutes of qualifying time.        |   Provincial Half Colours |
# |   Within 10 minutes of qualifying time.       |   Provincial Scroll       |
# |   More than 10 minutes of qualifying time.    |   No award                |

print("Based on your total time your Award is:")
if total_time <= 100:
    print("AWARD: Provincial Colours")
elif total_time <= 105:
    print("AWARD: Provincial Half Colours")
elif total_time <= 110:
    print("AWARD: Provincial Scroll")
else:
    print("No award")
