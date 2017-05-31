class Movie():
    """ A class representing a movie.

    This class contains information about a movie.
    
    Attributes:
        movie_title: A string representing the title of a movie. 
        poster_URL: A string representing the URL to the poster of the movie. 
        trailer_URL: A string representing the URL to the trailer of the movie. 
    """
    
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """ Inits a movie with title, poster image url, and trailer YouTube url."""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

