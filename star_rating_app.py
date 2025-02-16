"""
Homework 5: Star Rating App
===========================
Course:   CS 5001
Student:  Kelsey Edinborough
Semester: Fall 2024

An application that queries the client for movie titles
and a rating for each movie.
"""
from typing import List, Tuple
import string


__WELCOME_MESSAGE = """Welcome to the movie tracker!\nEnter a movie and rating to add it to the list."""
__GOODBYE_MESSAGE = """Thanks for using the movie tracker!\nSadly, movies will not be saved, as we still need to learn how to write to files."""

__PROMPT = """What would you like to do? """
__HELP_MESSAGE = """
You have the following command options for the movie tracker. 
    add movie,rating: add a movie and rating to the list
                        examples: 
                            ? add Princess Bride,10   
                            ? add Jurassic Shark,1
    list [filter]: list all movies and ratings, contains optional filters
                        examples:
                            ? list
                            ? list > 3
                            ? list < 2
                            ? list = 5
                            ? list Bride
    help: print this help message
    exit: exit the movie tracker
""".strip()


# COMMAND OPTION RETURNS
__ADD_COMMAND = "add"
__LIST_COMMAND = "list"
__EXIT_COMMAND = "exit"

# you can use this list for something like the following
# if command in _FILTER_OPERATION_OPTIONS:
#    do something
# else:
#    assume it is a movie title
__FILTER_OPERATION_OPTIONS = ['<', '>', '=', '<=', '>=', '!=']

# some program constants
__MIN_STARS = 1
__MAX_STARS = 5
__SPACER = 2


def clean_title(movie: str) -> str:
    """
    Cleans a string stripping trailing and leading whitespaces,
    and converts it to title case (capwords). 

    Examples:
        >>> clean_title("     v")
        'V'
        >>> clean_title("Princess bride  ")
        'Princess Bride'
        >>> clean_title("it's a wonderful life")
        'It's A Wonderful Life'
        >>> clean_title("harry  pOtter")
        'Harry Potter'
        >>> clean_title("   twIlIghT    ")
        'Twilight'

    See:
        https://docs.python.org/3/library/string.html#helper-functions

    Arguments:
        movie (str): movie title to clean
    Returns:
        str : the movie in title case, and leading and trailing spaces removed
    """
    lower_title = movie.lower()
    name = lower_title.split()
    i = 0
    final_cap_name = ''
    while i < len(name):
        if i == 0:
            cap_name = str.capitalize(name[i])
            final_cap_name += cap_name
            i += 1
        else:
            cap_name = str.capitalize(name[i])
            final_cap_name += ' ' + cap_name
            i += 1

    return final_cap_name


def convert_str_movie_tuple(val: str) -> Tuple[str, int]:
    """
    Converts a string in the format of "movie,rating" to a tuple
    It will clean up the title by calling clean_title, and will
    convert the rating to an int. This function assumes the string
    is correct, and in the format of "movie,rating" where movie is
    a string and rating is an int. 

    For Example:
        >>> convert_str_movie_tuple("v,5")
        ('V', 5)
        >>> convert_str_movie_tuple("Princess bride  ,10")
        ('Princess Bride', 10)
        >>> convert_str_movie_tuple("   JurAssic shARk  ,    1  ")
        ('Jurassic Shark', 1)
        >>> convert_str_movie_tuple(" twIliGht,   2")
        ('Twilight', 2)
        >>> convert_str_movie_tuple(" parks   and ReC,   6   ")
        ('Parks And Rec', 6)

    Args:
        val (str): String in the format of "movie,rating"

    Returns:
        Tuple[str, int]: Movie and int rating 
    """
    mov = val.split(",")
    movie_name = str(mov[0])
    clean_movie_name = clean_title(movie_name)
    rating = int(mov[1])
    return clean_movie_name, rating


def convert_rating(val: int, min_stars: int = __MIN_STARS, max_stars: int = __MAX_STARS) -> str:
    """Converts rating to stars (*) equal
    to the rating. Any value over max_stars will only
    return max_stars stars, and any value under min_stars
    will return min_stars star.
    For Example: 
        >>> convert_rating(0)
        '*'
        >>> convert_rating(6)
        '*****'
        >>> convert_rating(5)
        '*****'
        >>> convert_rating(1)
        '*'
        >>> convert_rating(10, 1, 10)
        '**********'
        >>> convert_rating(1, 2, 10)
        '**'    


    Args:
        val (int): the rating value
        min_stars (int, optional): the minimum number of stars to return. Defaults to _MIN_STARS.
        max_stars (int, optional): the maximum number of stars to return. Defaults to _MAX_STARS.

    Returns:
        str: stars between min_stars and max_stars
    """
    star = "*"
    if min_stars <= val <= max_stars:
        rating = str(val * star)

    if val < min_stars:
        rating = str(min_stars * star)

    if val > max_stars:
        rating = str(max_stars * star)

    return rating


def check_filter(movie: Tuple[str, int], filter: str) -> bool:
    """Checks if the movie title contains the filter.

    The filter can either be a string  (case insensitive) that will map to the title,
    or a filter operation and a number. The filter operation can be
    one of the following: <, >, =, <=, >=, !=. Which is meant to check
    the rating of the movie based on the number that follows. 

    if the empty string ("") is passed in, then the function will return True.

    Examples:
        >>> check_filter(("Princess Bride", 10), "Bride")
        True
        >>> check_filter(("Princess Bride", 10), "bride")
        True
        >>> check_filter(("Princess Bride", 10), "> 3")
        True
        >>> check_filter(("Princess Bride", 10), "< 3")
        False
        >>> check_filter(("Princess Bride", 10), "= 10")
        True
        >>> check_filter(("Princess Bride", 10), "= 11")
        False
        >>> check_filter(("Princess Bride", 10), "!= 10")
        False
        >>> check_filter(("Princess Bride", 10), "")
        True
        >>> check_filter(("Princess Bride", 10), "> 4")
        True
        >>> check_filter(("Princess Bride", 10), "> 10")
        False
        >>> check_filter(("Princess Bride", 10), ">= 10")
        True


    Args:
        movie (Tuple[str, int]): The movie tuple
        filter (str): The filter to check

    Returns:
        bool: True the movie meets the filter requirements.
    """

    title_string = str(movie[0])

    if filter == "":
        return True

    all_caps_movie_title = title_string.upper()

    if filter[0].isalpha():
        all_caps_filter = filter.upper()

        if all_caps_filter in all_caps_movie_title:
            return True
        else:
            return False

    elif filter.startswith(">") and filter[1] == " ":

        operation_int_split = filter.split()
        operation = operation_int_split[0]
        int_rating_comparison = int(operation_int_split[1])

        if movie[1] > int_rating_comparison:
            return True
        else:
            return False

    elif filter.startswith("<") and filter[1] == " ":

        operation_int_split = filter.split()
        operation = operation_int_split[0]
        int_rating_comparison = int(operation_int_split[1])

        if movie[1] < int_rating_comparison:
            return True
        else:
            return False

    elif filter.startswith("=") and filter[1] == " ":

        operation_int_split = filter.split()
        operation = operation_int_split[0]
        int_rating_comparison = int(operation_int_split[1])

        if movie[1] == int_rating_comparison:
            return True
        else:
            return False

    elif filter.strip()[:2] == ">=":
        int_rating_comparison = int(filter[3:])
        if movie[1] >= int_rating_comparison:
            return True
        else:
            return False

    elif filter[:2] == "<=":

        int_rating_comparison = int(filter[3:])

        if movie[1] <= int_rating_comparison:
            return True
        else:
            return False

    elif filter[:2] == "!=":

        int_rating_comparison = int(filter[3:])

        if movie[1] != int_rating_comparison:
            return True
        else:
            return False


check_filter(("Princess Bride", 10), ">= 10")


def print_movies(movies: List[Tuple[str, int]], filter: str = '', spacer: int = __SPACER, max_stars: int = __MAX_STARS) -> None:
    """Prints out a list of movies.

    Prints out the movies to the console along with star ratings. 

    Will filter the movies before printing based on the filter 
    passed into the function. See: check_filter() for more details.

    Uses the string format
        f"{convert_rating(rating):<{max_stars + spacer}}{movie}"

    For grading purposes, print the movies in the order that they
    appear in the list, as you loop through the list (do not sort the list, do not concatenate the strings, etc)

    Args:
        movies (List[Tuple[str, int]]): The list of movies
        filter (str, optional): The filter to apply. Defaults to ''.
        spacer (int, optional): The number of spaces between the stars and the movie title. Defaults to __SPACER.
        max_stars (int, optional): The maximum number of stars to print, used for spacing purposes. Defaults to __MAX_STARS.
    """

    i = 0

    while i < len(movies):
        if check_filter(movies[i], filter):
            done = f"{convert_rating(movies[i][1]):<{max_stars + spacer}}{movies[i][0]}"
            print(done)
            i += 1


# No need to modify the following code
def menu() -> Tuple[str, str]:
    """
    Prompts the client for their command.

    See HELP_MESSAGE for more options. Will also
    parse the command and return the command and
    any options that were passed in.

    Returns:
        Tuple[str, str]: the command OPTION, and the value after the command, or 
        the empty string if there was no value.
    """
    check = input(__PROMPT).strip()
    # this unpacks the string split by spaces into a variable, and a list of values
    command, *rest = check.split()
    command = command.casefold()
    while command not in [__ADD_COMMAND, __LIST_COMMAND, __EXIT_COMMAND]:
        print(__HELP_MESSAGE)
        check = input(__PROMPT).strip()
        command, *rest = check.split()
        command = command.casefold()
    return command, " ".join(rest)


def run() -> None:
    """
    Runs the star rating application.
    """
    print(__WELCOME_MESSAGE)
    command, options = '', ''
    movies = []
    while command != __EXIT_COMMAND:
        command, options = menu()
        if command == __ADD_COMMAND:
            movie = convert_str_movie_tuple(options)
            movies.append(movie)
        elif command == __LIST_COMMAND:
            print_movies(movies, options)

    print(__GOODBYE_MESSAGE)


if __name__ == "__main__":
    run()
