# Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog!.” as a single string.
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

# Reprint this sentence as “The quick brown fox jumps over the lazydog.” using the replace() function
# to replace every “!” exclamation mark with a blank space.
print(sentence.replace("!"," ").replace("dog ", "dog"))
# I noticed that the last "!" will add a space between "dog" and "." so I add a new replace to remove this
# additional " " so the final sentence is "The quick brown fox jumps over the lazy dog." instead of
# "The quick brown fox jumps over the lazy dog ."

# Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.” using the upper() function
print(sentence.replace("!"," ").replace("dog ", "dog").upper())

# Print the sentence in reverse.
print(sentence[::-1])


