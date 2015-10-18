import webbrowser
__author__ = 'lauramooney'


class Movie:
    #  define instance methods
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, spotify_playlist):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.spotify_playlist_url = spotify_playlist

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

