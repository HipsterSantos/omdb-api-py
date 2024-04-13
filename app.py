import requests
import collections
api_key = "915ad862"
namedTuttple = collections.namedtuple('movies',"Title,imdbID,Year,Poster,Type")
url = f"http://www.omdbapi.com/?apikey={api_key}&s=Dracula&plot=full"
r = requests.get(url)
result = r.json()["Search"]
v = []
for c in result:
    cc = namedTuttple(**c)
    v.append(cc)
print(v[0])