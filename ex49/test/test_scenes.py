from unittest.mock import patch


from ..scenes import Scene


def test_base_scene(player):
    scene = Scene()
    with patch("builtins.print") as mock_print:
        scene.enter(player)
        mock_print.assert_any_call("This scene is not configured.")
        mock_print.assert_any_call("Subclass it and implement enter()")
