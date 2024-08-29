import random


WEAPONS = {"dagger": 9, "sword": 20}


class Character(object):
    def __init__(self, name, hp, max_attack):
        self.name = name
        self.hp = hp
        self.max_attack = max_attack

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

        if self._hp < 0:
            self._hp = 0

    def is_alive(self):
        return self.hp > 0

    def attack(self, opponent):
        """Character initiates attack."""
        damage = random.randint(0, self.max_attack)

        if damage == 0:
            print(f"The attack on {opponent.name} has been repelled.")
        else:
            opponent.hp -= damage

        print(f"{self.name} attacks {opponent.name} for {damage}")

    def __str__(self):
        return f"{self.name}: {self.hp}"


class Player(Character):
    def __init__(self, name):
        self.weapon = "dagger"
        self.inventory = []
        hp = 50
        max_attack = WEAPONS[self.weapon]

        super().__init__(name, hp, max_attack)

    def new_weapon(self, weapon_string):
        try:
            if weapon_string in WEAPONS.keys():
                self.weapon = weapon_string
                self.max_attack = WEAPONS[weapon_string]
            else:
                raise KeyError("Weapon not found")
        except KeyError as e:
            print(e)
