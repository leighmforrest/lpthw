import random

WEAPONS = {"dagger": 9, "sword": 20}


class Character:

    def __init__(self, name, hp, max_attack):
        self.name = name
        self.hp = hp
        self.max_attack = max_attack

    def attack(self, other):
        """Character initiates attack."""
        damage = random.randint(0, self.max_attack)
        if damage == 0:
            print(f"The attack on {other.name} has been repelled.")
        else:
            other.hp -= damage

            if other.hp < 0:
                other.hp = 0

            print(f"{self.name} attacks {other.name} for {damage} damage.")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp}"


class Player(Character):
    def __init__(self, name):
        """Character class for the game.

        name: The name of the character.
        """

        self.weapon = "dagger"
        self.inventory = []
        hp = 50
        max_attack = WEAPONS[self.weapon]

        super(Player, self).__init__(name, hp, max_attack)

    def new_weapon(self, weapon_string):
        try:
            if weapon_string in WEAPONS.keys():
                self.weapon = weapon_string
                self.max_attack = WEAPONS[weapon_string]
            else:
                raise KeyError("Weapon not found")
        except KeyError as e:
            print(e)
