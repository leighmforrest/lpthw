import pytest

from ..ex51.ttb import get_large_clusters, get_actual_sales
from .helpers import dictionary_key_has_integer


def test_get_large_clusters(number_clusters):
    large_clusters = get_large_clusters(number_clusters)
    assert isinstance(large_clusters, dict)
    assert len(large_clusters) == 4


def test_get_large_clusters_right_numbers(large_clusters):
    for key in large_clusters.keys():
        assert len(large_clusters[key]) > 5


def test_get_stocks_on_hand(stocks_on_hand):
    assert len(stocks_on_hand) == 2
    dictionary_key_has_integer(stocks_on_hand)


def test_get_production(production):
    assert len(production) == 4
    dictionary_key_has_integer(production)


def test_get_actual_sales(stocks_on_hand, production):
    actual_sales = get_actual_sales(production, stocks_on_hand)
    assert len(actual_sales) == 2
    dictionary_key_has_integer(actual_sales)
