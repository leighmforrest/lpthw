from ex49.scenes import Scene


class Atrium(Scene):

    def enter(self, player):
        return "green"


class Green(Scene):

    def enter(self, player):
        return "finished"


class Finished(Scene):

    def enter(self, player):
        print("YOU WIN")
        exit(0)


SCENES = {"atrium": Atrium(), "green": Green(), "finished": Finished()}


ADJACENT_SCENES = {
    "opening": ["atrium"],
    "atrium": ["green"],
    "green": ["finished", "atrium"],
    "finished": [],
}
