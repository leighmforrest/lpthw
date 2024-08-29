def death(message):
    print(f"{message} GAME OVER.")
    exit(1)


def player_input(iterable, casting_func=str):
    """Get a user input filtered based on the elements of a list."""
    while True:
        try:
            choice = casting_func(input("> "))
            if choice in iterable:
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Please make a valid choice.")
