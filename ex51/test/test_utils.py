import os
import pytest

from ..utils import (
    parse_to_iso_date,
    to_snake_case,
    to_capitalized,
    generate_data_dict,
    is_pdf,
)


@pytest.mark.parametrize(
    "date_string,date_format,expected",
    [("03MAR2024", "%d%b%Y", "2024-03-03"), ("November 2021", "%B %Y", "2021-11-01")],
)
def test_parse_iso_date(date_string, date_format, expected):
    assert parse_to_iso_date(date_string, date_format) == expected


@pytest.mark.parametrize("date_string,date_format", [("03MAR2024", "%B %d %y")])
def test_parse_iso_date_fail(date_string, date_format):
    with pytest.raises(KeyError) as e:
        parse_to_iso_date(date_string, date_format)
        assert str(e.value) == "Not a valid date format."


@pytest.mark.parametrize(
    "str1,expected",
    [
        ("mark My Words", "mark_my_words"),
        ("ThIs  Iz A Ran$om Note", "this_iz_a_ranom_note"),
    ],
)
def test_to_snake_case(str1, expected):
    assert to_snake_case(str1) == expected


@pytest.mark.parametrize(
    "str1,expected",
    [
        ("mark_my_words", "Mark My Words"),
        ("this_is_a_journey_into_sound", "This Is A Journey Into Sound"),
    ],
)
def test_to_capitalized(str1, expected):
    assert to_capitalized(str1) == expected


def test_generate_data_dict_fail(capsys):
    data_dict = generate_data_dict({"foo": "bar"}, [], (0, 2))
    captured = capsys.readouterr()
    assert captured.out.count("Argument must be a dictionary.") == 2
    assert len(data_dict) == 1


def test_is_pdf(pdf_path):
    assert is_pdf(pdf_path)


@pytest.mark.parametrize(
    "path_string",
    [
        "files/data.txt",
        "files/green.txt",
    ],
)
def test_is_pdf_fail(path_string):
    filepath = os.path.join(os.path.dirname(__file__), path_string)
    assert not is_pdf(filepath)
