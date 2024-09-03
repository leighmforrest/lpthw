import pytest
import sys
from unittest.mock import patch

from ..utils import player_input, death


CHOICES = ["red", "blue", "green"]


@pytest.mark.parametrize("input_string", CHOICES)
def test_player_input_success(input_string):
    with patch("builtins.input", return_value=input_string):
        assert player_input(CHOICES) == input_string


@pytest.mark.parametrize("input_string", ["cyan", "magenta", "yellow"])
def test_player_input_fail(input_string, capsys):
    with patch("builtins.input", side_effect=[input_string, "red"]):
        player_input(CHOICES)
        captured = capsys.readouterr()

        assert "Please make a valid choice." in captured.out


from unittest.mock import patch
import pytest
import sys


def test_death():
    with patch("builtins.print") as mock_print:
        try:
            death("You have been defeated")
        except SystemExit as e:
            # Verify that the print function was called with the expected message
            mock_print.assert_called_once_with("You have been defeated", "GAME OVER.")

            assert e.code == 1
