# TASK 20 - Compulsory Task 1 - Introduction to Natural Language Processing

# import the spacy library
import spacy

# load the english model
nlp = spacy.load('en_core_web_sm')

# the 3 garden path sentences that I chose + the 3 mandatory ones from the task
gardenpathSentences = [
    "The sour drink from the ocean.",
    "We painted the wall with cracks.",
    "The man who hunts ducks out on weekends.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenise each sentence in the list and perform named entity recognition
for sentence in gardenpathSentences:
    nlp_gardenpath = nlp(sentence)

    # Tokenise the sentence    
    print([token.orth_ for token in nlp_gardenpath])

    # Perform named entity recognition
    print([(i, i.label_, i.label) for i in nlp_gardenpath.ents])

    # jut to better visualise the output
    print("------------------------------------")


# Examine how spaCy has categorised each sentence. Then, use spacy.explain
# to look up and print the meaning of entities that you don’t understand.
# For example: print(spacy.explain("FAC"))

# First one
print("\nGPE: " + spacy.explain("GPE"))

# Second one
print("PERSON: " + spacy.explain("PERSON"))

# At the bottom of your file, write a comment about two entities that you looked up.
# For each entity answer the following questions:

# ○ What was the entity and its explanation that you looked up?
    # A: The entities that I looked up were GPE and PERSON. GPE stands for
    # "Geo-Political Entity". It is a named entity label used to identify
    # geopolitical entities, such as countries, cities, and states. PERSON is
    # a named entity label used to identify people, including fictional.

# ○ Did the entity make sense in terms of the word associated with it?
    # A: Yes, the entities made sense in terms of the words associated with them.
    # I think that using garden path sentences was not a good idea for this task
    # due to the lack of identifiable entities in the sentences. I tried to find
    # garden path sentences that had entities in them, but I could not find many.
    # Maybe use pre-defined sentences that have diferent entities in them. Like
    # the example below that wrongly label "Dutch Golden Age" as a PERSON and the
    # the painter "Johannes Vermeer" as a GPE.

example = '''
The Girl With A Pearl Earring is an oil painting by Dutch Golden Age painter Johannes Vermeer, dated c. 1665.
Going by various names over the centuries, it became known by its present title towards the end of the 20th century after the earring worn by the girl portrayed there. The work has been in the collection of the Mauritshuis in The Hague since 1902 and has been the subject of various literary and cinematic treatments.
'''

example_nlp = nlp(example)
print("\nExample:")
print([(ent, ent.label_, ent.label) for ent in example_nlp.ents])