import requests
from collections import namedtuple

Movies = namedtuple('Movies',"Title,imdbID,Year,Poster,Type")
api_key = "915ad862"

class MovieList:
    def __init__(self,search: str):
        if not search or not search.strip():
            raise ValueError('Please provide a proper search value')
        self.search = search
    def perform_search(self):
        url = f"http://www.omdbapi.com/?apikey={api_key}&s={self.search}&plot=full"
        response = requests.get(url)
        data = response.json()
        movies = [Movies(**d) for d in data["Search"]]
        movies.sort(key=lambda movie: movie.Year, reverse=True)
        return movies