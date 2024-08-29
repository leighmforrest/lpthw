from . import randint, DIALOGUE


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud... if she was smarter.",
        "Such a luser.",
        "I have a small puppy that is better than this.",
        "You'r worse than your Dad's jokes.",
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class OpeningScene(Scene):
    codes = []

    def enter(self):
        print("""
Welcome to Gothons from Percal #25. 

Enter a code or press enter.
              """)
        
        user_input = input("> ")
        
        if user_input in self.codes:
            pass
        else:
            return "central_corridor"

class CentralCorridor(Scene):

    def enter(self):
        print(DIALOGUE["CentralCorridor_enter"])

        action = input("> ").lower()
        if "shoot" in action:
            print(DIALOGUE["CentralCorridor_shoot"])
            return "death"
        if "dodge" in action:
            print(DIALOGUE["CentralCorridor_dodge"])
            return "death"
        if "tell a joke" in action:
            print(DIALOGUE["CentralCorridor_joke"])
            return "laser_weapon_armory"
        else:
            print("DOES NOT COMPUTE!")
            return "central_corridor"


class LaserWeaponArmory(Scene):

    def enter(self):
        print(DIALOGUE["LaserWeaponArmory_enter"])

        code = "".join([str(randint(0, 9)) for _ in range(3)])
        print(code)
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")
        if guess == code:
            print(DIALOGUE["LaserWeaponArmory_guess"])
            return "the_bridge"
        else:
            print(DIALOGUE["LaserWeaponArmory_fail"])
            return "death"


class TheBridge(Scene):

    def enter(self):
        print(DIALOGUE["TheBridge_enter"])

        action = input("> ")

        if "throw the bomb" in action:
            print(DIALOGUE["TheBridge_throw_bomb"])
            return 'death'
        if "slowly place the bomb" in action:
            print(DIALOGUE["TheBridge_place_bomb"])

            return "escape_pod"
        else:
            print("DOES NOT COMPUTE")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(DIALOGUE["EscapePod_enter"])
        good_pod = randint(1, 5)
        guess = input("[pod #]>")

        if int(guess) != good_pod:
            print(DIALOGUE["EscapePod_death"]
                .format(guess=guess))
            return 'death'
        else:
            print(DIALOGUE['EscapePod_escape']
                  .format(guess=guess))
        
        return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        exit(1)


class Map(object):

    scenes = {
        "opening_scene": OpeningScene(),
        "central_corridor": CentralCorridor(),
        "death": Death(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "the_bridge": TheBridge(),
        "escape_pod": EscapePod(),
        "finished": Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
