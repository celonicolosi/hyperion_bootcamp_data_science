# TASK 21 - Compulsory Task 1 - Semantic Similarity (NLP)

# import the spacy library
import spacy

# load the english model
nlp = spacy.load("en_core_web_md")
# nlp = spacy.load("en_core_web_sm") # uncomment this line and comment the line above to run the example with the simpler language model

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Write a note about what you found interesting about the similarities between cat, monkey and banana 
# and think of an example of your own.

    # Answer:
    # One interesting observation is that "cat" and "monkey" have a relatively higher similarity score
    # (0.5929) compared to "cat" and "banana" (0.2235). This indicates that "cat" and "monkey" share more
    # semantic similarities in the given model compared to "cat" and "banana." This finding aligns with our
    # intuitive understanding as both "cat" and "monkey" are animals, whereas "banana" is a fruit. Following
    # this logic is safe to assume that "monkey" and "banana" have a higher similarity score (0.4041) compared
    # to "cat" and "banana" (0.2235) due to the fact that is commonly known that "monkey" likes "banana".

    # One example of my own is the following:

word4 = nlp("tree")
word5 = nlp("house")

# print the similarity between cat and the new words
print("cat x tree: " + str(word1.similarity(word4))) # 0.2694
print("cat x house: " + str(word1.similarity(word5))) # 0.2295

# print the similarity between monkey and the new words
print("monkey x tree: " + str(word2.similarity(word4))) # 0.3544
print("monkey x house: " + str(word2.similarity(word5))) #0.1426

# print the similarity between banana and the new words
print("banana x tree: " + str(word3.similarity(word4))) # 0.4260 (the highest similarity score, maybe because one is a fruit and the other is a plant)
print("banana x house: " + str(word3.similarity(word5))) # 0.1320

# print the similarity between the new words
print("tree x house: " + str(word4.similarity(word5))) # 0.3665

# ============================================================================================================

# Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice
# is different from the model 'en_core_web_md'.

    # Answer:
    # Running with "en_core_web_md" model:
    # 0.5929929675536907
    # 0.4041501317354622
    # 0.22358827466989753

    # Running with "en_core_web_sm" model:
    # 0.6770565401305904
    # 0.7276309426913784
    # 0.6806928240713817

    # My note: The similarity scores are higher when using the "en_core_web_sm" model compared to the
    # "en_core_web_md" model. This is probably due to the fact that the "en_core_web_sm" model is smaller and
    # therefore less accurate than the "en_core_web_md" model. The comparison between banana and cat really
    # surprised me (0.6806)!
    # The output came with a warning: "UserWarning: [W007] The model you're using has no word vectors
    # loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER,
    # which may not give useful similarity judgements. This may happen if you're using one of the small models,
    # e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always
    # add your own word vectors, or use one of the larger models instead if available."

    # Adition information that I found on the internet about the difference between the two models:
    # It's important to note that the 'en_core_web_sm' model provides a more lightweight and computationally efficient
    # option for tasks that don't require the additional capabilities and larger size of the 'en_core_web_md' model.
    # However, the trade-off is that the 'en_core_web_sm' model may have a reduced capacity to capture fine-grained
    # semantic relationships and may perform slightly differently in various natural language processing tasks. 
