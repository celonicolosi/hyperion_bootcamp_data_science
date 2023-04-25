# Create a program called alternative.py that reads in a string and makes each alternate
# character an UPPERCASE character and each other alternate character a lowercase character
# (e.g, the string “Hello World” would become “HeLlO WoRlD”).

uppercased_string = ""

original_string = input("\nEnter a string: ")

for i in range(len(original_string)):
    if i % 2 == 0:
        uppercased_string += original_string[i].upper()
    else:
        uppercased_string += original_string[i].lower()

print(uppercased_string)

# Now, try starting with the same string but making each alternative word lower and
# upper case (e.g. the string: “I am learning to code” would become “i AM learning TO code”). 
# Using the split and join functions will help you here.

splited_string = original_string.split(" ")

for i in range(len(splited_string)):
    if i % 2 == 0:
        splited_string[i] = splited_string[i].lower()
    else:
        splited_string[i] = splited_string[i].upper()

joined_string = " ".join(splited_string)

print(joined_string)
