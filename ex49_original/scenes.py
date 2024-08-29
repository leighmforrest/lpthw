from .character import Character
from .utils import death, player_input


class Scene(object):

    def enter(self, player):
        print("This scene is not configured.")
        print("Subclass it and implement enter()")
        exit(0)


class Atrium(Scene):
    def enter(self, player):
        print("Atrium!")
        return "ogre"


class OgreRoom(Scene):
    ogre = Character("Ogre", 25, 5)

    def enter(self, player):
        print("OGRE ROOM!")

        while self.ogre.is_alive() and player.is_alive():
            self.ogre.attack(player)

            if not player.is_alive():
                death("The ogre has smite your head.")

            print("What do you want to do?")
            action = input(">")

            if action == "retreat":
                print("You go back...")
                return "atrium"
            if action == "attack":
                player.attack(self.ogre)
            else:
                print("Please make a valid choice.")

            self.ogre.attack(player)
            print(player)
            print(self.ogre)

        if player.is_alive():
            print("The ogre is dead. You now possess the power sword.")
            player.new_weapon("sword")
            return "finished"
        else:
            death("The ogre has smite your head.")


class Finished(Scene):
    def enter(self, player):
        print("FINISHED!")

        if player.weapon == "sword":
            print("You own the power sword.")
        exit(1)
