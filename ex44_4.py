import random

jobs = {
    "jobber": {"hit": 1, "damage": 1, "dialogue": "I am a jabroni"},
    "curtain jerker": {"hit": 2, "damage": 2, "dialogue": "I am a curtain jerker!"},
    "midcarder": {"hit": 3, "damage": 3, "dialogue": "I'm in the midcard."},
    "main eventer": {"hit": 4, "damage": 4, "dialogue": "I am a top guy!"},
}


def Person_new(name, age, eyes, job="jobber"):
    person = {
        "name": name,
        "age": age,
        "eyes": eyes,
        "job": jobs[job].copy(),  # Create a copy of the job dictionary
    }

    def talk(words):
        print(f'I am {person["name"]} and {words}')

    def hit(defender):
        print(f"{person['name']} has attacked {defender['name']}!!!!!")
        defender["job"]["damage"] -= person["job"]["hit"]

        if defender["job"]["damage"] <= 0:
            print(f"{defender['name']} has been killed!")

    person["talk"] = talk
    person["hit"] = hit

    return person


becky = Person_new("Becky", 39, "green")
stinky = Person_new("Stinky Wizzleteats", 65, "brown", "midcarder")
hulk = Person_new("Hulk Hogan", 70, "blue", "main eventer")
jelly = Person_new("Jelly Nutella", 35, "brown", "curtain jerker")

combatants = {"becky": becky, "stinky": stinky, "hulk": hulk, "jelly": jelly}

becky["talk"]("I am talking here.")
stinky["talk"]("Hello boys and girls!")
hulk["talk"]("Lemme tell you something brother!")
jelly["talk"]("I'm a jabroni trash wrestler!")

while len(combatants) > 1:
    random_combatants = random.sample(list(combatants.keys()), 2)
    attacker = combatants[random_combatants[0]]
    defender = combatants[random_combatants[1]]

    attacker["hit"](defender)

    if defender["job"]["damage"] > 0:
        print(defender["job"]["dialogue"])
    else:
        # remove defender from combatant dict
        del combatants[random_combatants[1]]

winner = str(list(combatants.keys())[0])
print("The winner of the battle royal is:", combatants[winner]["name"])
