import imdb
from possible_genres import genres
from prettytable import PrettyTable
from get_choice import get_user_choice, get_user_input, is_integer


def print_exception_if_exists(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as exc:
            print(exc)
    return inner


class Movies:
    def __init__(self):
        self.__ia = imdb.IMDb()
        self.movies = None
        self.desired_movie = None
        self.__genres = genres

    def print_movies_desc(self):
        table = PrettyTable()
        table.field_names = ['id', 'title', 'year', 'kind']
        movies = [[index, movie['title'], movie.get('year', 'unknown'), movie['kind']] for index, movie
                  in enumerate(self.movies, start=1)]
        table.add_rows(movies)
        print(table)

    def get_full_information(self):
        movie_id = self.desired_movie.getID()
        self.desired_movie = self.__ia.get_movie(movie_id)

    def print_full_movie_desc(self):
        table = PrettyTable()
        table.field_names = ['title', 'year', 'kind', 'rating', 'directors', 'actors']

        year = self.desired_movie.get('year', '')
        kind = self.desired_movie.get('kind', '')
        title = self.desired_movie['title']
        rating = self.desired_movie.get('rating', '')
        directors = self.desired_movie.get('directors', '')
        casting = self.desired_movie.get('cast', '')
        actors = ', '.join(map(str, casting))
        directors_str = ', '.join(map(str, directors))
        table.add_row([title, year, kind, rating, directors_str, actors])
        print(table)

    def is_interested_in_movie(self):
        print("Is there a movie you are interested in?")
        print('Y - yes; N - no')
        ui = get_user_input()
        match ui:
            case 'y':
                movies_count = len(self.movies)
                movie_id = input('Type movie id: ')
                if not (is_integer(movie_id) and int(movie_id) - 1 <= movies_count):
                    print('Incorrect input')
                else:
                    movie_id = int(movie_id) - 1
                    self.desired_movie = self.movies[movie_id]
                    return True
            case 'n':
                return False

    def find_movie_by_title(self):
        movie_name = input("Enter movie name: ")
        self.movies = self.__ia.search_movie(movie_name)

    def find_movie_by_genres(self):
        genres = list(map(lambda x: x.lower(), self.__genres))
        print('Genres:')
        print(', '.join(genres))
        ui_genres = input("Input genres: ")
        if ',' in ui_genres:
            ui_genres = ui_genres.split(sep=',')
        else:
            ui_genres = ui_genres.split()
        ui_genres = list(map(lambda x: x.lower(), ui_genres))
        all_ui_genres_is_valid = all([genre in genres for genre in ui_genres])
        if all_ui_genres_is_valid:
            movies_by_genres = self.__ia.get_top50_movies_by_genres(ui_genres)
        else:
            raise ValueError("Invalid genre")
        self.movies = movies_by_genres

    def movie_search(self):
        self.print_movies_desc()
        interested = self.is_interested_in_movie()
        if interested:
            print("Loading movie information...")
            self.get_full_information()
            self.print_full_movie_desc()

    @print_exception_if_exists
    def interface(self):
        question_string = '1. Find a movie by title\n2. Find movies by genres\n3. Back'
        while True:
            print("What do you want?")
            print(question_string)
            choice = get_user_choice(question_string, parse_string=True)
            match choice:
                case '1':
                    self.find_movie_by_title()
                    self.movie_search()
                case '2':
                    self.find_movie_by_genres()
                    self.movie_search()
                case '3':
                    print('Closing movies app...')
                    return


if __name__ == '__main__':
    mvs = Movies()
    mvs.interface()
