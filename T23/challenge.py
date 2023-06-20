# As asked by the task description, this file contains the Little Sister's Vocabulary exercises.
# Link to the exercises: https://exercism.org/tracks/python/exercises/little-sisters-vocab
# I know that is not mandatory but I will add the .py to the Dropbox folder.

# 1. Add a prefix to a word
# One of the most common prefixes in English is un, meaning "not". In this activity, your sister needs to make
# negative, or "not" words by adding un to them.

# Implement the add_prefix_un() function that takes word as a parameter and returns a new un prefixed word:

def add_prefix_un(word):
    print("un" + word)

# example of the function call working
print("\nExercise 1: Add a prefix to a word")
add_prefix_un("happy")
add_prefix_un("kind")
add_prefix_un("paid")

# 2. Add prefixes to word groups
# There are four more common prefixes that your sister's class is studying: en (meaning to 'put into' or 'cover with'),
# pre (meaning 'before' or 'forward'), auto (meaning 'self' or 'same'), and inter (meaning 'between' or 'among').
# In this exercise, the class is creating groups of vocabulary words using these prefixes, so they can be studied
# together. Each prefix comes in a list with common words it's used with. The students need to apply the prefix and
# produce a string that shows the prefix applied to all of the words.

# Implement the make_word_groups(<vocab_words>) function that takes a vocab_words as a parameter in the following form:
# [<prefix>, <word_1>, <word_2> .... <word_n>], and returns a string with the prefix applied to each word that looks like:
# '<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'.

def make_word_groups(prefix, *words):
    for word in words:
        print(prefix + word)

# example of the function call working
print("\nExercise 2: Make word groups")
make_word_groups("pre", "dispose", "position")
make_word_groups("en", "close", "joy", "light")
make_word_groups("auto", "correct", "mate", "graph", "biography")


# 3. Remove a suffix from a word
# ness is a common suffix that means 'state of being'. In this activity, your sister needs to find the original root word
# by removing the ness suffix. But of course there are pesky spelling rules: If the root word originally ended in a consonant
# followed by a 'y', then the 'y' was changed to 'i'. Removing 'ness' needs to restore the 'y' in those root words. e.g.
# happiness --> happi --> happy.

# Implement the remove_suffix_ness(<word>) function that takes in a word str, and returns the root word without the ness suffix.

def remove_suffix_ness(word):
    # check if the word ends with "iness" removing the suffix and adding "y"
    if word.endswith("iness"):
        print(word[:-5] + "y")
    # for all the other cases, just remove the suffix "ness"
    else:
        print(word[:-4])

# example of the function call working
print("\nExercise 3: Remove a suffix from a word")
remove_suffix_ness("happiness")
remove_suffix_ness("sadness")
remove_suffix_ness("goodness")
remove_suffix_ness("dizziness")
remove_suffix_ness("heaviness")
remove_suffix_ness("darkness")
remove_suffix_ness("business")

# 4. Extract and transform a word
# Suffixes are often used to change the part of speech a word has. A common practice in English is "verbing" or
# "verbifying" -- where an adjective becomes a verb by adding an en suffix.
# In this task, your sister is going to practice "verbing" words by extracting an adjective from a sentence and turning
# it into a verb. Fortunately, all the words that need to be transformed here are "regular" - they don't need spelling
# changes to add the suffix.
# Implement the adjective_to_verb(<sentence>, <index>) function that takes two parameters. A sentence using the vocabulary
# word, and the index of the word, once that sentence is split apart. The function should return the extracted adjective
# as a verb.

def adjective_to_verb(sentence, index):
    # split the sentence into a list of words
    words = sentence.split()
    # remove punctuation
    adjective = words[index].strip(",.")
    verb = adjective + "en"
    print(verb)

# example of the function call working
print("\nExercise 4: Extract and transform a word\n")
adjective_to_verb("I need to make that bright.", -1)
adjective_to_verb("It got dark as the sun set.", 2)
adjective_to_verb("The doctor diagnosed him with a severe case of the flu, leaving him feeling weak and sick.", -1)
adjective_to_verb("She sank into the soft cushions of the cozy armchair, enjoying its comfort and warmth.", 4)