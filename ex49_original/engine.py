from character import Player

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
        self.player = None

    def play(self):
        current_scene_name = "atrium"
        current_scene = self.scene_map.get_scene(current_scene_name)
        last_scene = self.scene_map.get_scene("finished")

        print("WELCOME TO MONSTER MAZE")

        # This scene is 'opening' in Map. Initialize the player here.
        player_name = input("Enter your name:")
        self.player = Player(player_name)

        while current_scene != last_scene:
            next_scene_name = current_scene.enter(self.player)

            if next_scene_name in self.scene_map.get_next_scenes(current_scene_name):
                current_scene = self.scene_map.get_scene(next_scene_name)
                current_scene_name = next_scene_name
            else:
                raise ValueError("Next scene is not adjacent to current scene.")

        current_scene.enter(self.player)
