# importing the module
import imdb
# creating an instance of the IMDB()
mymoviedb = imdb.IMDb()
# Using the Search movie method

film = mymoviedb.search_movie("Godfather")
print(film[0].movieID)
items = mymoviedb.get_movie_recommendations(film[0].movieID)
for i in items:
    print(i)