from unittest.mock import patch
import pytest

from ..map import Map
from ..engine import Engine
from .helpers import SCENES, BAD_ADJACENT_SCENES


def test_engine_init(engine):
    assert len(engine.scene_map.scenes) == 3
    assert engine.player is None


def test_init_player(engine, capsys):
    with patch("builtins.input", return_value="Roderick"):
        try:
            engine.play()
        except SystemExit as e:
            assert e.code == 0  # Ensure the game exits with code 0
        captured = capsys.readouterr()

        assert "WELCOME TO MONSTER MAZE" in captured.out
        assert engine.player is not None
        assert engine.player.name == "Roderick"


def test_run_game(engine):
    with patch("builtins.input", return_value="Roderick"):
        with patch("builtins.print") as mock_print:
            try:
                engine.play()
            except SystemExit as e:
                mock_print.assert_called_with("YOU WIN")
                assert e.code == 0


def test_engine_adjacent_fail():
    map = Map(SCENES, BAD_ADJACENT_SCENES)
    engine = Engine(map)

    with patch("builtins.input", return_value="Roderick"):
        with pytest.raises(ValueError) as e:
            engine.play()
            assert str(e.value) == "Next scene is not adjacent to current scene."
