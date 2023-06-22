# TASK 21 - Compulsory Task 2 - Semantic Similarity (NLP)

# import the spacy library
import spacy

# load the english model
nlp = spacy.load("en_core_web_md")

# Read in the movies.txt file. Each separate line is a description of a different movie.
with open("movies.txt", "r") as f:
    movies = f.readlines()

planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

def watch_next(movie, movie_list):
    # create a dictionary to store the similarity scores
    similar_movies = {}

    # create a doc object for the movie
    movie_doc = nlp(movie)

    # loop through the movie list
    for token in movie_list:
        token = nlp(token)
        similar_movies[token] = token.similarity(movie_doc)
        # print(f"{token} : {token.similarity(movie_doc)}") # Uncomment this line if you want to see the similarity scores
    
    # sort the dictionary by the values
    sorted_movies = sorted(similar_movies.items(), key=lambda x: x[1], reverse=True)

    # print the film with the highest similarity score
    print("\nBECAUSE YOU WATCHED PLANET HULK:\n")
    print(sorted_movies[0][0])

watch_next(planet_hulk, movies)