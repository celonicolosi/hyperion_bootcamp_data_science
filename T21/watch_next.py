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
    print(similar_movies)
    sorted_movies = sorted(similar_movies.items(), key=lambda x: x[1], reverse=True)

    # print the films with similarity scores above 0.8
    print("\nBECAUSE YOU WATCHED PLANET HULK:\n")
    
    for movie, score in sorted_movies:
        if score > 0.8:
            # printing only the movie name without the similarity score because in theory that means nothing to the user
            print(f"- {movie}")

watch_next(planet_hulk, movies)

# There is a commented line in the for loop if you want to see the similarity scores but in resume is this:
# Movie A : 0.7771752937723543
# Movie B : 0.7487075237236891
# Movie C : 0.8866717596279875
# Movie D : 0.3764830873071832
# Movie E : 0.6708372537042129
# Movie F : 0.8753508543471434
# Movie G : 0.8777585723496374
# Movie H : 0.7977046189736419
# Movie I : 0.8196949673276563
# Movie J : 0.6989104466560989