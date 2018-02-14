import media
#import the fresh_tomatoes python module in the files
import fresh_tomatoes
#import movie finder
import movie_finder

#create the movie finder class instance with API URL
movie = movie_finder.MovieFinder('http://www.omdbapi.com/?i=tt3896198&apikey=e3e960d7')

#create the movies we want to add
movies_to_find = ['Limitless', 'The Social Network', 'Steve Jobs', 'The Big Short', 'The Wolf of Wall Street', 'Bleed for This']
#create an array to store movie objects
movies = []

#create movie objects
for i in movies_to_find:
    dictionary = movie.content_search(i)
    movies.append(media.Movie(dictionary['title'], dictionary['plot'], dictionary['poster'], dictionary['rating'], "https://www.youtube.com/watch?v=KYz2wyBy3kc"))

fresh_tomatoes.open_movies_page(movies)