""" This module defines the Movie class."""

import webbrowser


class Movie:
    """ Supplies two functions: __init__() and show_trailer() """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, spotify_playlist):
        """ defines instance methods for a single Movie """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.spotify_playlist_url = spotify_playlist

    def show_trailer(self):
        """ :return: a Movie instance whose trailer should be played """
        webbrowser.open(self.trailer_youtube_url)

