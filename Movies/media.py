import webbrowser


class Movie():
    """ This class provides a way to store movie related information."""
    # VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_rating, movie_storyline,
                 poster_image, trailer_youtube):
        """ This method is the constructor for Movie()."""
        self.title = movie_title
        self.rating = movie_rating
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This method within Movie() opens a window and plays the trailer."""
        webbrowser.open(self.trailer_youtube_url)
