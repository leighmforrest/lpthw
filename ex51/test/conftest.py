import pytest
import os

from ..pdf import get_pdf, get_number_clusters


@pytest.fixture
def pdf_path():
    return os.path.join(os.path.dirname(__file__), "files/ttb_11_2021.pdf")


@pytest.fixture
def pdf(pdf_path):
    pdf = get_pdf(pdf_path)
    return pdf


@pytest.fixture
def number_clusters(pdf):
    clusters = get_number_clusters(pdf)
    return clusters
