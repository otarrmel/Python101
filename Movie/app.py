import json
import os

from user import User


def menu():
    user_name = input("Please enter a name: ")
    if os.path.exists(user_name.capitalize() + ".json"):
        print("Welcome, {}!".format(user_name))
        with open(user_name+".json", 'r') as f:
            json_data = json.load(f)
            user = User.from_json(json_data)
            option(user)

    else:
        print(user_name.capitalize() + "'s account is not found!")
        print("Creating user data!")
        user = User(user_name)
        option(user)


def option(user):
    opt = 0
    while opt != 4:
        print("\n\nWhat would you like to do?")
        print("\t[1]Add a movie?")
        print("\t[2]See list of movies?")
        print("\t[3]See list of watched movies")
        print("\t[4]Save and Quit")
        opt = int(input("\nPlease enter the option [1-4]: "))

        if opt == 1:

            movie_name = input("\nEnter movie name: ")
            movie_genre = input("Enter movie genre: ")

            user.add_movie(movie_name, movie_genre)
            print("Movie {} was added!".format(movie_name))

        elif opt == 2:
            opt2 = 0
            allowed_opt = [1, 2, 3]
            print("\nMovies:")
            for movie in user.movies:
                print("{} - {}".format(movie.name, movie.genre))

            while opt2 not in allowed_opt:
                print("\nWhat do you want to do?")
                print("\t[1] Set a movie as watched?")
                print("\t[2] Delete a movie by name?")
                print("\t[3] Back to main menu")
                try:
                    opt2 = int(input("\nPlease select an option [1-3]: "))
                except ValueError:
                    opt2 = 4

                if opt2 == 1:
                    watched_name = input("\nEnter the movie you want to watched: ")
                    selected_movie = list(filter(lambda mov: mov.name == watched_name, user.movies))

                    if selected_movie[0].watched:
                        print("\nYou have watched it already!")

                    else:
                        selected_movie[0].watched = True
                        print("\nYou have watched {}!".format(selected_movie[0].name))

                    break

                elif opt2 == 2:
                    delete_movie = input("\nEnter the movie you want to delete: ")
                    user.delete_movie(delete_movie)
                    print("\nYou have deleted {}!".format(delete_movie))
                    break

                elif opt2 == 3:
                    break

                else:
                    print("\nInvalid input!")

        elif opt == 3:
            print("\nWatched Movies:")
            if user.watched_movies():
                for movie in user.watched_movies():
                    print("{} - {}".format(movie.name, movie.genre))
            else:
                print("\nYou don't have any watched movies!")

        elif opt == 4:
            user.save_to_file(user.name)
            break

        else:
            print("Invalid input!")


if __name__ == '__main__':
    menu()

