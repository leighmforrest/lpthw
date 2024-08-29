import pytest
from ex49.map import Map


def test_map_success(test_map):
      assert test_map is not None

@pytest.mark.parametrize("scene_string, expected", [
      ("opening", 1,),
      ("atrium", 1,),
      ("green", 2,),
      ("finished", 0,)
])
def test_get_next_scenes(scene_string, expected, test_map):
    next_scenes = test_map.get_next_scenes(scene_string)
    assert len(next_scenes) == expected

def test_cannot_initialize_non_dictionaries(capsys):
        with pytest.raises(ValueError):
            map = Map([], [])
            captured = capsys.readouterr()
        
            assert map is None
            assert "Arguments must be dictionaries." in captured.out