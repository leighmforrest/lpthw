import random


jobs = {
    "jobber": {"hit": 1, "damage": 1, "dialogue": "I am a jabroni"},
    "curtain jerker": {"hit": 2, "damage": 2, "dialogue": "I am a curtain jerker!"},
    "midcarder": {"hit": 3, "damage": 3, "dialogue": "I'm in the midcard."},
    "main eventer": {"hit": 4, "damage": 4, "dialogue": "I am a top guy!"},
}


class Person:
    def __init__(self, name, age, eyes, job="jobber"):
        self.name = name
        self.age = age
        self.eyes = eyes
        self.job = jobs[job].copy()

    def talk(self, words):
        print(f"I am {self.name} and {words}")

    def hit(self, defender):
        print(f"{self.name} has attacked {defender.name}!!!!!")
        defender.job["damage"] -= self.job["hit"]

        if defender.job["damage"] <= 0:
            print(f"{defender.name} has been killed!")


becky = Person("Becky", 39, "green")
stinky = Person("Stinky Wizzleteats", 65, "brown", "midcarder")
hulk = Person("Hulk Hogan", 70, "blue", "main eventer")
jelly = Person("Jelly Nutella", 35, "brown", "curtain jerker")

combatants = {"becky": becky, "stinky": stinky, "hulk": hulk, "jelly": jelly}

while len(combatants) > 1:
    random_combatants = random.sample(list(combatants.keys()), 2)
    attacker = combatants[random_combatants[0]]
    defender = combatants[random_combatants[1]]

    attacker.hit(defender)

    if defender.job["damage"] > 0:
        print(defender.job["dialogue"])
    else:
        # remove defender from combatant dict
        del combatants[random_combatants[1]]

winner = str(list(combatants.keys())[0])
print("The winner of the battle royal is:", combatants[winner].name)
