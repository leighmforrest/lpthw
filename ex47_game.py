import ex47
from ex47.classes import Map, Engine

# for k, v in ex47.DIALOGUE.items():
#     print(v)

a_map = Map("opening_scene")
a_game = Engine(a_map)
a_game.play()
