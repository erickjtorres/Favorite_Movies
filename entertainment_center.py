import media
#import the fresh_tomatoes python module in the files
import fresh_tomatoes
import movie_finder

#create the movie finder class instance
movie = movie_finder.MovieFinder('http://www.omdbapi.com/?i=tt3896198&apikey=e3e960d7')

movies_to_find = ['toy story', 'avatar', 'school of rock', 'ratatouille', 'midnight in paris']
movies = []


for i in movies_to_find:
    dictionary = movie.content_search(i)
    movies.append(media.Movie(dictionary['title'], dictionary['plot'], dictionary['poster'], "https://www.youtube.com/watch?v=KYz2wyBy3kc"))
print(movies[1].storyline)

#
# toy_story = media.Movie("Toy Story",
#                         "A story of a boy and his toys that come to life",
#                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
#                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# avatar = media.Movie("Avatar",
#                      "A marine on an alien planet",
#                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
#                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#
# school_of_rock = media.Movie("School of Rock",
#                              "Using rock music to learn",
#                              "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
#                              "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
#
# ratatouille = media.Movie("Ratatoulle",
#                           "A rat is a chef in Paris",
#                           "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
#                           "https://www.youtube.com/watch?v=c3sBBRxDAqk")
#
# midnight_in_paris = media.Movie("Midnight in Paris",
#                                 "Going back in time to meet authors",
#                                 "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
#                                 "https://www.youtube.com/watch?v=FAfR8omt-CY")
#
# hunger_games = media.Movie("Hunger Games",
#                            "A reaally real reality show",
#                            "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
#                            "https://www.youtube.com/watch?v=mfmrPu43DF8")
#
# #create an array of the object instances created above
# movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
#call the open_movies_page function within fresh_tomatoes with the array created above
# fresh_tomatoes.open_movies_page(movies)