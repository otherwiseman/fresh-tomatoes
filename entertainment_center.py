import fresh_tomatoes
import media
__author__ = 'lauramooney'


garden_state = media.Movie("Garden State",
                           "After many years away, a television bit actor returns to his hometown for his mother's funeral. There he is confronted by various aspects of the life he left behind, as he heals old wounds and forges new friendships.",
                           "https://upload.wikimedia.org/wikipedia/en/3/3c/Garden_State_Poster.jpg",
                           "https://youtu.be/6ZbqE23IRH0",
                           "https://play.spotify.com/album/24mCiOTIF5Ob1uwluRFERv")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                               "After a painful breakup, Clementine undergoes a procedure to erase memories of her former boyfriend Joel from her mind. When Joel discovers that Clementine is going to extremes to forget their relationship, he undergoes the same procedure.",
                               "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                               "https://youtu.be/quuMv7cGUn0",
                               "https://play.spotify.com/album/5yOO5ZvqDZx5Sr8jOGtWRR")

dan_in_real_life = media.Movie("Dan in Real Life",
                               "Dan Burns, a widower and advice columnist, meets a beautiful stranger in a bookstore and is instantly smitten. Unfortunately the woman, named Marie, is already involved with Dan's charismatic brother.",
                               "https://upload.wikimedia.org/wikipedia/en/d/d3/Dan_in_real_life.jpg",
                               "https://youtu.be/8SqaWEBSd4g",
                               "https://play.spotify.com/album/2hc3wJYs3eHHjvSAhI3VjV")

movies = [garden_state, eternal_sunshine, dan_in_real_life]
fresh_tomatoes.open_movies_page(movies)
