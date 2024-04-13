import requests
from collections import namedtuple

Movies = namedtuple('Movies',"Title,imdbID,Year,Poster,Type")
api_key = "915ad862"

class MovieList:
    def __init__(self,search: str):
        self.search = search
    def perform_search(self):
        url = f"http://www.omdbapi.com/?apikey={api_key}&s={self.search}&plot=full"
        response = requests.get(url)
        data = response.json()
        return [Movies(**d) for d in data]