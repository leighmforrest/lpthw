import pytest
import os

from ..ex51.pdf import get_pdf, get_number_clusters
from ..ex51.ttb import get_large_clusters, get_stocks_on_hand, get_production


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


@pytest.fixture
def large_clusters(number_clusters):
    clusters = get_large_clusters(number_clusters)
    return clusters


@pytest.fixture
def stocks_on_hand(number_clusters):
    data = get_stocks_on_hand(number_clusters)
    return data 


@pytest.fixture
def production(large_clusters):
    data = get_production(large_clusters)
    return data 