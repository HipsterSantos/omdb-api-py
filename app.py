from movie_search import MovieList
from requests.exceptions import ConnectionError
def main():
    event_loop()
def event_loop():
    searchTitle = "ONCE_THROUGH_LOOP"
    while searchTitle != 'x':
        try:
            searchTitle =   input('enter the text to be searched')
            if searchTitle != 'x':
                movies = MovieList(searchTitle)
                result = movies.perform_search()
                for c in result:
                    print("{} -- {}".format(c.Year,c.Title))
        except ConnectionError as cr:
            print(f"Please check your internet connection - {cr}")
        except ValueError as vr: print("Please enter a value - {}".format(vr))
        except Exception as ee:
            print("invalid input, goddamn it!", type(ee))
if __name__ == "__main__":
    main()

