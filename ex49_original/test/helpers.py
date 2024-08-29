from ex49.scenes import Scene

class Green(Scene):
        def enter(self, player):
            return "finished"


class Finished(Scene):
    def enter(self, player):
        exit(0)


class Atrium(Scene):
        def enter(self, player):
            return "green"

SCENES =  {"atrium": Atrium(), "green": Green(), "finished": Finished()}

ADJACENT_SCENES = {
        "opening": ["atrium"],
        "atrium": ["green"],
        "green": ["finished", "atrium"],
        "finished": [],
    }