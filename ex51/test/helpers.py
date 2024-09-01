def dictionary_key_has_integer(dictionary):
    for item in dictionary.values():
        assert int(item) is not None
