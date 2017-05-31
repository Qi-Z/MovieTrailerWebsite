from media import Movie
import json
class EntertainmentCenter():
    """ A class that manages entertainment content.

    Attributes:
        movies: A list of Movie objects.
    """
    def __init__(self, movie_file):
        """ Init the class.

        Args:
            movie_file: A string representing the JSON file containing a list movies.
        """
        self.movies = []
        self.read_movies_from_file(movie_file)

    def read_movies_from_file(self, movie_file):
        """ Read a list of movies from a file and return them as a list.

        Args:
            movie_file: A JSON file containing a list movies.

        Returns:
            This function returns nothing.
        """
        with open(movie_file, 'r') as f:
            movies = json.load(f)
            for movie in movies:
                self.movies.append(Movie(movie["title"], movie["poster_image_url"], movie["trailer_youtube_url"]))

    def get_movies(self):
        """
        Return a list of movies.

        Returns:
            A list of movies.
        """
        return self.movies

