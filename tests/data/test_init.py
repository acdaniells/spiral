from spiral.core.exc import SpiralError
from spiral.data import list_datasets, load_dataset
from spiral.data._datasets import _load_dataset

import pandas as pd

from pytest import raises


def test_list_datasets():
    list_datasets()


def test_load_carshare_dataset():
    data = load_dataset("carshare")
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (249, 4)


def test_load_election_dataset():
    data = load_dataset("election")
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (58, 8)


def test_load_election_geojson_dataset():
    data = load_dataset("election_geojson")
    assert isinstance(data, dict)
    assert sorted(data.keys()) == ["features", "type"]


def test_load_flights_dataset():
    data = load_dataset("flights")
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (144, 3)


def test_load_gapminder_dataset():
    data = load_dataset("gapminder")
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (1704, 8)


def test_load_iris_dataset():
    data = load_dataset("iris")
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (150, 6)


def test_load_tips_dataset():
    data = load_dataset("tips")
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (244, 7)


def test_load_titanic_dataset():
    data = load_dataset("titanic")
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (891, 15)


def test_load_wind_dataset():
    data = load_dataset("wind")
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (128, 3)


def test_invalid_loader():
    assert load_dataset("__missing__") is None


def test_missing_dataset():
    with raises(SpiralError, match=".*does not exists.*"):
        _load_dataset("__missing__")
