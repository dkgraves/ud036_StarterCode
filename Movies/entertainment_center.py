# fresh _tomatoes.py and media.py must exist in the same directory as entertainment_center.py
import fresh_tomatoes 
import media

# media.Movie() must be populated in this order: title, rating, short description, link to a movie poster or other artwork and the link to trailer on youTube.
# medeia.py dictates the order and what content should be provided.
toy_story = media.Movie("Toy Story", "G", "A story of a boy and his toys come to life.", "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg"
                        , "https://www.youtube.com/watch?v=KYz2wyBy3kc" )


avatar = media.Movie("Avatar", "PG-13", "A marine on an alien planet.", "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg" 
                     ,"https://www.youtube.com/watch?v=5PSNL1qE6VY" )


true_lies = media.Movie("True Lies", "R", "A fearless, globe-trotting, terrorist-battling secret agent has his life turned upside down "
                       +"when he discovers his wife might be having an affair with a used car salesman while terrorists smuggle nuclear war heads into the United States." 
                       , "https://m.media-amazon.com/images/M/MV5BYzg5YmUyNGMtMThiNS00MjA2LTgwZDctNDlhM2RkZDNmZmRkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,671,1000_AL_.jpg"
                       , "https://www.youtube.com/watch?v=i1CPsVNUAG8")
                    

full_metal_jacket = media.Movie("Full Metal Jacket", "R", "A pragmatic U.S. Marine observes the dehumanizing effects the Vietnam War has on his fellow recruits from their brutal boot camp training to the bloody street fighting in Hue.",
                                 "https://m.media-amazon.com/images/M/MV5BNzkxODk0NjEtYjc4Mi00ZDI0LTgyYjEtYzc1NDkxY2YzYTgyXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,666,1000_AL_.jpg"
                                 , "https://youtu.be/x9f6JaaX7Wg")

true_grit = media.Movie("True Grit", "PG-13", "A stubborn teenager enlists the help of a tough U.S. Marshal to track down her father's murderer."
                        , "https://m.media-amazon.com/images/M/MV5BMjIxNjAzODQ0N15BMl5BanBnXkFtZTcwODY2MjMyNA@@._V1_SY1000_CR0,0,640,1000_AL_.jpg"
                        , "https://youtu.be/CUiCu-zuAgM")

big_jake = media.Movie("Big Jake", "PG-13", "In 1909, when John Fain's gang kidnaps Jacob McCandles' grandson and holds him for ransom, Big Jake sets out to rescue the boy."
                       , "https://m.media-amazon.com/images/M/MV5BNGRlNjIwNzEtZjNlMi00YWJjLWI5ODctMjRmZDNlMzdhMTc0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjI4MjA5MzA@._V1_SY1000_CR0,0,659,1000_AL_.jpg"
                       , "https://www.youtube.com/watch?v=bq0gp54818A")

# all movies that will be displayed need to be listed here using the correct name from the previous section
movies = [toy_story, avatar, true_lies, full_metal_jacket, true_grit, big_jake]
fresh_tomatoes.open_movies_page(movies)



