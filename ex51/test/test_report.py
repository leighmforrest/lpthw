from collections import OrderedDict
from ..ex51.report import generate_report


def test_generate_report(pdf_path):
    report = generate_report(pdf_path)
    assert len(report) == 10
    assert isinstance(report, OrderedDict)