import random
from collections import Counter
from sys import exit
import os


def clear_screen():
    """Clear the terminal screen."""
    # For Windows
    if os.name == "nt":
        os.system("cls")
    # For Unix/Linux/Mac
    else:
        os.system("clear")


def menu_input(iterable, casting_func=str):
    while True:
        try:
            choice = casting_func(input("> "))
            if choice in iterable:
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Please make a valid choice.")


def display_menu(iterable):
    if isinstance(iterable, dict):
        for key, value in iterable.items():
            print(f"{key}: {value}")
    elif isinstance(iterable, list):
        for item in iterable:
            print(f"{item}")
    else:
        raise ValueError("Menu must be either a list or dictionary.")


def roll_dice(num_dice=2):
    if num_dice < 1 or num_dice > 3:
        raise ValueError("Number of dice must be between 1 and 3")
    return sorted([random.randint(1, 6) for _ in range(num_dice)], reverse=True)


def check_doubles(dice):
    counts = Counter(dice)
    return any(count > 1 for count in counts.values())


def attack(attacker_stamina, defender_stamina):
    # Ensure at least 1 die is rolled
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

    defender_losses = sum(loss[0] for loss in losses)
    attacker_losses = sum(loss[1] for loss in losses)

    return attacker_losses, defender_losses


def calculate_losses(attacker, defender):
    attacker_losses, defender_losses = attack(attacker["stamina"], defender["stamina"])
    print(f"{attacker['name']} losses: {attacker_losses}")
    print(f"{defender['name']} losses: {defender_losses}")
    attacker["stamina"] -= attacker_losses
    defender["stamina"] -= defender_losses
    return attacker, defender


def display_stamina(combatant):
    print(f"{combatant['name']}: {combatant['stamina']}")


def player_attack(player, ogre):
    print("Player attacks!!!!!!")
    return calculate_losses(player, ogre)


def ogre_attack(ogre, player):
    return calculate_losses(ogre, player)


def check_winner(ogre, player):
    if ogre["stamina"] <= 0:
        print("The ogre is defeated!")
        treasure_room()

    if player["stamina"] <= 0:
        death(
            "The ogre has sucked the gizzards right out of your body with its chelicerae!"
        )


def death(why):
    print(why, "\nGAME OVER")
    exit(0)


def treasure_room():
    print("Congratulations! You have won the grand and glorious jackpot!\a")
    exit(0)


def kraken_cavern():
    def kraken_death():
        death(
            """
You look directly at the kraken. You immediately turn to stone!
"""
        )

    menu = {"enter foxhole": atrium, "stare": kraken_death}
    menu_items = list(menu.keys())

    print(
        """
You enter a very expansive cavern.
There is a lake in front of you. The earth shakes...
from the lake...
EMERGES THE KRAKEN!
There is a foxhole to your right.
What do you do? 
        """
    )

    choice = menu_input(menu_items, str)
    menu[choice]()


def frankies_lair():
    frankie_confused = False
    piledriver_death = """
You kick the monster in the breadbasket. Monster groans VERY LOUDLY!!!!!!
He grabs you by the head and squeezes your melon with his brute strength, like a vise.
"""

    def go_around():
        if frankie_confused:
            ogre_room()
        else:
            death("Monster grabs you by the collar and flings you out of the window.")

    def confuse_frankie():
        nonlocal frankie_confused
        if frankie_confused:
            print("Monster gets unconfused.")
        else:
            print(
                """
You look directly into the face of the monster, making a funny face. 
Monster looks puzzled and freezes in place.
You may go around him to open the door behind him.
"""
            )
        frankie_confused = not frankie_confused

    menu = {
        "go around": go_around,
        "give sitout piledriver": lambda: death(piledriver_death),
        "confuse monster": confuse_frankie,
    }
    menu_items = list(menu.keys())

    print(
        """
There is a thick wooden workbench in the room with test tubes, conical flasks,
and a gilt grimoire opened up on a stand. A tall monster with green skin,
shovel forehead, and bolts coming out of his carotid arteries. He elicits a
loud reverberous groan. What do you do?
          """
    )

    while True:
        display_menu(menu_items)
        choice = menu_input(menu_items, str)
        menu[choice]()


def ogre_room():
    ogre = {
        "name": "Ogre",
        "stamina": 20,
        "strength": 1,
    }

    player = {
        "name": "Player",
        "stamina": 15,
        "strength": 1,
    }

    menu = ["retreat", "pass", "attack"]

    clear_screen()
    print("There are cobwebs everywhere.")

    while True:
        print("Ogre Attacks!!!!")
        ogre, player = ogre_attack(ogre, player)
        display_stamina(ogre)
        display_stamina(player)
        check_winner(ogre, player)
        print("What do you do?")
        display_menu(menu)
        choice = menu_input(menu)

        if choice == "pass":
            pass
        if choice == "attack":
            player, ogre = player_attack(player, ogre)
            display_stamina(ogre)
            display_stamina(player)
            check_winner(ogre, player)
        if choice == "retreat":
            death("You run full force into the cave's stone door.")


def atrium():
    def abyss():
        death("You fall into a bottomless abyss.")

    menu = {"left": kraken_cavern, "right": frankies_lair, "center": abyss}
    menu_items = list(menu.keys())
    print("There are 3 doors in front of you. Which one do you choose?")
    display_menu(menu_items)
    choice = menu_input(menu_items, str)
    return menu[choice]()


if __name__ == "__main__":
    atrium()
    # Uncomment below to test Frankie's Lair directly
    # frankies_lair()
    # Uncomment below to test Ogre Room directly
    # ogre_room()
