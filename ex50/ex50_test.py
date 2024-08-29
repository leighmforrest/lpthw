import pytest
from ex50.person import Person

def test_combat():
    boxer = Person("Boxer", 100, 10)
    zombie = Person("Zed", 1000, 1000)

    # these asserts are bad, fix them
    assert boxer.hp == 100, f"Boxer has wrong hp of {boxer.hp}."
    assert zombie.hp == 1000, f"Zombie has wrong hp of {zombie.hp}."

    boxer.hit(zombie)
    assert zombie.alive(), "Zombie should be alive"

    zombie.hit(boxer)
    assert not boxer.alive(), "Boxer should be dead"

def test_negative_hp():
    boxer = Person("Boxer", 10, 10)
    zombie = Person("Zed", 11, 11)

    boxer.hit(zombie)
    assert boxer.hp == 0
    assert not boxer.alive()


def test_negative_hp_and_damage_fail():
    with pytest.raises(ValueError):
        boxer = Person("Boxer", -100, -100)