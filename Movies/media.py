import webbrowser


class Movie():
    """ This class provides a way to store movie related information.
    Parameters
    -------------
    movie_title : str
        This is the title of the movie.
    movie_rating : str
        This is the movie industry rating, ie G, PG, PG-13, R.
    movie_storyLine : str
        A short description of the movie.
    poster_image : str
        This is the url to an image of the movie poster or other artwork.
    trailer_youtube_url : str
        url to the youtube movie trailer
    """
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
        """ This method within Movie() opens a window and plays the trailer
        that was supplied  in the trailer_youtube argument.
        """
        webbrowser.open(self.trailer_youtube_url)
