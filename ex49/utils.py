# from sys import exit


def player_input(iterable, casting_function=str):
    """Get a user input filtered based on the elements of a list."""
    while True:
        try:
            choice = casting_function(input("> "))
            if choice in iterable:
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Please make a valid choice.")


def death(message):
    print(message, "GAME OVER.")
    exit(1)
