import os
from datetime import date
import pytest

from ..utils import DATE_FORMATS, to_snake_case
from ..pdf import get_pdf, get_matching_lines, get_line_items, get_number_clusters
from pdftotext import PDF


def test_get_pdf_success(pdf):
    assert isinstance(pdf, PDF)


@pytest.mark.parametrize("bad_file_path", ["files/data.txt", "green.dat"])
def test_get_pdf_fail(bad_file_path):
    file_path = os.path.join(os.path.dirname(__file__), bad_file_path)

    with pytest.raises(ValueError) as e:
        get_pdf(file_path)

        assert str(e.value) == "The path must be a PDF file."


@pytest.mark.parametrize(
    "startswith, results",
    [
        ("Reporting Period", ["Reporting Period: November 2021"]),
        ("Report Date", ["Report Date: 09MAR2022"]),
    ],
)
def test_get_matching_lines(pdf, startswith, results):
    lines = get_matching_lines(pdf, startswith)
    assert lines == results


@pytest.mark.parametrize(
    "line_item, date_format",
    [
        ("Reporting Period", DATE_FORMATS["reporting_period"]),
        ("Report Date", DATE_FORMATS["report_date"]),
    ],
)
def test_get_line_items_success(pdf, line_item, date_format):
    line_item_dict = get_line_items(pdf, line_item, date_format)
    iso_date_string = line_item_dict[to_snake_case(line_item)]
    iso_date = date.fromisoformat(iso_date_string)
    assert isinstance(iso_date, date)


@pytest.mark.parametrize("line_item", ["Purchase Date", "Green"])
def test_get_line_items_fail_no_line_item(line_item, pdf):
    with pytest.raises(ValueError) as e:
        get_line_items(pdf, line_item, DATE_FORMATS["reporting_period"])
        assert str(e.value) == f"No matching item found for {line_item}"


@pytest.mark.parametrize(
    "line_item, date_format",
    [
        ("2018-2021", DATE_FORMATS["report_date"]),
        ("2017 and prior =", DATE_FORMATS["reporting_period"]),
    ],
)
def test_get_line_items_fail_invalid_format(line_item, date_format, pdf):
    with pytest.raises(ValueError) as e:
        get_line_items(pdf, line_item, date_format)
    assert str(e.value) == f"Incorrect format for {line_item}."


def test_get_number_clusters(number_clusters):
    assert len(number_clusters) == 10
