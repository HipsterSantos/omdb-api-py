from movie_search import MovieList

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
        except:
            print("invalid input, goddamn it!")
if __name__ == "__main__":
    main()

