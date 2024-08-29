import pytest
from ex49.test.helpers import SCENES, ADJACENT_SCENES
from ex49.character import Player
from ex49.map import Map


@pytest.fixture
def player():
    return Player("Roderick")


@pytest.fixture
def test_map():
    return Map(SCENES, ADJACENT_SCENES)