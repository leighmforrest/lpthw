import random
from sys import exit


def death(why):
    """End a losing game."""
    print(f"{why}\nGAME OVER")
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


def roll_dice(num_dice):
    """Simulate the roll of at least one die and up to three dice."""
    if num_dice < 1 or num_dice > 3:
        raise ValueError("Number of dice must be more than one or greater than 3.")

    return sorted([random.randint(1, 6) for _ in range(num_dice)], reverse=True)


def attack(attacker_stamina, defender_stamina):
    """Attack an opponent based on the the classic board game Risk."""
    attacker_dice = max(1, min(3, attacker_stamina - 1))
    defender_dice = max(1, min(2, defender_stamina))
    num_comparisons = min(attacker_dice, defender_dice)

    attacker_rolls = roll_dice(attacker_dice)
    defender_rolls = roll_dice(defender_dice)

    # Note: attacker wins ties
    losses = [
        (
            1 if attacker_rolls[i] >= defender_rolls[i] else 0,
            1 if attacker_rolls[i] < defender_rolls[i] else 0,
        )
        for i in range(num_comparisons)
    ]

    attacker_losses = sum(loss[0] for loss in losses)
    defender_losses = sum(loss[1] for loss in losses)

    return attacker_losses, defender_losses


def calculate_losses(attacker_stamina, defender_stamina):
    """Determine the losses of an attack."""
    attacker_losses, defender_losses = attack(attacker_stamina, defender_stamina)
    attacker_stamina -= attacker_losses
    defender_stamina -= defender_losses
    return attacker_stamina, defender_stamina


def check_winner_ogre_room(ogre_stamina, player_stamina):
    """Check the stamina of the ogre against the player's to determine victory."""
    if ogre_stamina <= 0:
        player_defeats_ogre()
    if player_stamina <= 0:
        death(
            "The ogre has smite your head with the bat! You brains splatter all over the floor."
        )


def player_defeats_ogre():
    """The actions in the ogre room after player defeats ogre."""
    amulet = False
    choices = {
        "proceed": treasure_room,
        "stay": lambda: death("You age at warp speed"),
        "take amulet": None,
    }

    while True:
        print(
            "You have defeated the ogre. There is an amulet where the ogre was. What do you do? "
        )
        choice = player_input(choices.keys())
        if choice == "take amulet":
            if not amulet:
                amulet = True
                print("You now posess the amulet.")
            else:
                print("You already posess the amulet.")
        if choice == "proceed":
            toxic_swamp(amulet)
        else:
            choices[choice]()


def kraken_cave():
    """The Kraken Cave room function."""
    choices = {
        "enter foxhole": atrium,
        "stare": lambda: death("Your gaze angers the kraken and you turn to stone."),
        "retreat": lambda: death(
            "The kraken grabs you with its tentacles and squeezes you."
        ),
    }
    print(
        """
There is a wide lake in the large cavern. The cave expands across the entire horizon.
A perpetual sunset lights the entire sky. A foxhole appears behind you.
The earth shakes and from the lake...
EMERGES THE KRAKEN!!!!!!!
"""
    )

    print("What do you do?")
    choice = player_input(choices)
    choices[choice]()


def frankies_lair():
    """The Frankie's Lair room function."""

    def go_around():
        if frankie_confused:
            spider_room()
        else:
            death("Monster grabs you by the collar and flings you out the window.")

    def confuse_frankie():
        nonlocal frankie_confused

        if frankie_confused:
            print("Monster gets unconfused.")
        else:
            print("Monster gets confused.")
        frankie_confused = not frankie_confused

    choices = {
        "go around": go_around,
        "give sitout piledriver": lambda: death(piledriver_death),
        "confuse monster": confuse_frankie,
    }

    frankie_confused = False
    piledriver_death = """Frankie squeeze your head with his bare hands, like a vise."""

    # Action starts here
    print(
        """
There is a thick oak table in the dark room, with conical flasks, test tubes, and
a leather-bound gilt grimoire on a wooden stand. From the corner of the room,
a tall monster with green skin, shovel forehead, and bolts protruding from his
corotid arteries elicits a large groan and lurches towards you.
"""
    )
    while True:
        print("What is your choice?")
        choice = player_input(choices.keys())
        choices[choice]()


def spider_room():
    """The action of the spider room."""

    def check_winner_spider_room(spiders, player_stamina):
        if len(spiders) <= 0:
            print("You walk under the waterfall, stamina is topped up.")
            ogre_room()
        if player_stamina <= 0:
            death("Spider sucks out your gizzards.")

    def delete_spider():
        if spiders and spiders[0] <= 0:
            del spiders[0]
            print("Spider has been defeated.")

    choices = {
        "attack": calculate_losses,
        "retreat": lambda: death("You run into a stone wall."),
        "freeze": lambda: print("You freeze."),
    }
    spiders = [1, 1, 2, 2, 3, 4]
    player_stamina = 15

    # Action starts here.
    print(
        """
Rock formations reach high up. Cobwebs span each corner of the chamber.
Several poisonous spiders crawl from all corners!
"""
    )

    while len(spiders) > 0:
        random.shuffle(spiders)
        # spiders[0] attacks player
        print(f"There are {len(spiders)} spiders.")
        spiders[0], player_stamina = calculate_losses(spiders[0], player_stamina)
        print("Spider attacks!!!!!")
        print("Spider:", spiders[0])
        print("Player:", player_stamina)
        delete_spider()
        check_winner_spider_room(spiders, player_stamina)
        print(f"There are {len(spiders)} spiders.")
        print("What move do you take?")
        choice = player_input(choices.keys())

        if choice == "attack":
            player_stamina, spiders[0] = choices[choice](player_stamina, spiders[0])
            print("Spider:", spiders[0])
            print("Player:", player_stamina)
            delete_spider()
            check_winner_spider_room(spiders, player_stamina)
        else:
            choices[choice]()


def atrium():
    """The atrium room function."""
    choices = {
        "left": kraken_cave,
        "center": lambda: death("You fall into a bottomless abyss."),
        "right": frankies_lair,
    }

    print(
        """
Bright white walls with a big skylight overhead showers the room with white solar light.
There are three identical doors ahead of you. 
"""
    )

    print("Which door do you want to open?")
    choice = player_input(choices.keys())
    choices[choice]()


def treasure_room():
    """The treasure room function."""
    print("You have won the grand and glorious jackpot!!!!!!")
    exit(1)


def ogre_room():
    """The ogre room function."""
    ogre_stamina = 15
    player_stamina = 10

    choices = {
        "attack": calculate_losses,
        "retreat": lambda: death("You run into the stone door at full speed."),
        "freeze": lambda: print("You freeze."),
    }

    # Action starts here
    print(
        """
Black walls and ceiling surround the environment. From the back comes a green
froglike anthropod. It groans loudly and comes at you with a baseball bat.
"""
    )

    while True:
        ogre_stamina, player_stamina = calculate_losses(ogre_stamina, player_stamina)
        print("Ogre attacks!")
        print("Ogre:", ogre_stamina)
        print("Player:", player_stamina)
        check_winner_ogre_room(ogre_stamina, player_stamina)

        print("What do you do?")
        choice = player_input(choices.keys())
        if choice == "attack":
            player_stamina, ogre_stamina = choices[choice](player_stamina, ogre_stamina)
            print("Player attacks!")
            print("Ogre:", ogre_stamina)
            print("Player:", player_stamina)
            check_winner_ogre_room(ogre_stamina, player_stamina)
        else:
            choices[choice]()


def toxic_swamp(amulet):
    """Crossing the toxic swamp function."""

    # Action starts here
    print(
        "There is a swamp the glows purple and pink. A doorway appears on the other side."
    )

    if amulet:
        print("You are immune to the toxicity of the swamp. You advance to the door...")

    else:
        turns = 0
        stamina = 5

        while turns < 10:
            swamp_die = roll_dice(1)
            player_die = roll_dice(1)
            turns += 1

            if swamp_die > player_die:
                stamina -= 1
                print("The swamp has sapped your strength.")
            if stamina <= 0:
                death("The swamp eats the meat off of your bones.")
            else:
                print("\nYou move ahead.\n")

        print("You advance to the door....")
        treasure_room()


if __name__ == "__main__":
    atrium()
