from unittest.mock import patch
from ..character import WEAPONS


def test_character_exists(character):
    assert len(character.name) > 0
    assert character.hp > 0
    assert character.max_attack > 0
    assert character is not None


def test_characer_is_alive(character):
    assert character.is_alive()


def test_character_is_not_alive(character):
    new_hp = character.hp + 1
    character.hp -= new_hp
    assert not character.is_alive()


def test_character_no_negative_hp(character):
    new_hp = character.hp + 2
    character.hp -= new_hp
    assert character.hp == 0


def test_character_attack_repelled(character, opponent, capsys):
    with patch("random.randint", return_value=0):
        character.attack(opponent)
        captured = capsys.readouterr()

    assert opponent.hp == 1
    assert opponent.is_alive() is True
    assert f"The attack on {opponent.name} has been repelled." in captured.out


def test_character_attack_direct_hit(character, opponent, capsys):
    with patch("random.randint", return_value=2):
        character.attack(opponent)
        captured = capsys.readouterr()

    assert opponent.hp == 0
    assert opponent.is_alive() is False
    assert f"{character.name} attacks {opponent.name} for" in captured.out


def test___str__(character):
    assert str(character) == f"{character.name}: {character.hp}"


def test_player(player):
    assert player is not None
    assert player.name == "John Doe"
    assert player.hp == 50
    assert player.weapon == "dagger"
    assert player.max_attack == WEAPONS[player.weapon]


def test_player_new_weapon_success(player):
    player.new_weapon("sword")
    assert player.weapon == "sword"
    assert player.max_attack == WEAPONS["sword"]


def test_player_new_weapon_fail(player, capsys):
    player.new_weapon("shovel")
    captured = capsys.readouterr()

    assert "Weapon not found" in captured.out
    assert player.weapon != "shovel"
