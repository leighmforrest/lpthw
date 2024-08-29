import pytest

from ex49.character import Character, Player
from .helpers import SCENES, ADJACENT_SCENES
from ex49.map import Map
from ex49.engine import Engine


@pytest.fixture
def character():
    return Character("Ganon", 10, 10)


@pytest.fixture
def opponent():
    return Character("Barry Horowitz", 1, 1)


@pytest.fixture
def player():
    return Player("John Doe")


@pytest.fixture
def map():
    return Map(SCENES, ADJACENT_SCENES)


@pytest.fixture
def engine(map):
    return Engine(map)
