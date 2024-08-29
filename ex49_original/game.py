from scenes import Atrium, OgreRoom, Finished
from map import Map
from engine import Engine

scenes = {"atrium": Atrium(), "ogre": OgreRoom(), "finished": Finished()}

adjacent_scenes = {
    "opening": ["atrium"],
    "atrium": ["ogre"],
    "ogre": ["finished", "atrium"],
    "finished": [],
}

if __name__ == "__main__":
    map = Map(scenes, adjacent_scenes)
    engine = Engine(map)
    engine.play()
