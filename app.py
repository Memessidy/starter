from get_choice import get_user_choice
from movies import Movies
from music import get_music
import pyjokes
from game import game


def main():
    question_string = '1. Find a movie\n2. Find a track\n3. Get a joke\n4. Play a game \n5.Exit'
    while True:
        print("What are you interested in? (type a number): ")
        print(question_string)
        choice = get_user_choice(question_string, parse_string=True)
        match choice:
            case "1":
                mvs = Movies()
                mvs.interface()
            case "2":
                genre = input("Input a genre: ")
                get_music(genre)
            case "3":
                joke = pyjokes.get_joke()
                print(joke)
            case "4":
                game()
            case "5":
                print("Good luck...")
                return


if __name__ == '__main__':
    main()
