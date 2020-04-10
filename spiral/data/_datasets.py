"""
Built-in datasets for demonstration, educational and test purposes.
"""

import os

from spiral.core.exc import SpiralError
from spiral.utils.io import read_data, resource_exists, resource_filename

import pandas as pd

from pandas.api.types import CategoricalDtype as CatType


def load_carshare() -> pd.DataFrame:
    """
    Load and return the carshare dataset.

    Each row represents the availability of car-sharing services near the
    centroid of a zone in Montreal.

    Returns
    -------
    pandas.DataFrame
        A `pandas.DataFrame` with 249 rows and the following columns:
        `['centroid_lat', 'centroid_lon', 'car_hours', 'peak_hour']`.

    """
    return _load_dataset("carshare.csv.gz")


def load_election() -> pd.DataFrame:
    """
    Load and return the election dataset.

    Each row represents voting results for an electoral district in the 2013
    Montreal mayoral election.

    Returns
    -------
    pandas.DataFrame
        A `pandas.DataFrame` with 58 rows and the following columns:
        `['district', 'Coderre', 'Bergeron', 'Joly', 'total', 'winner',
        'result', 'district_id']`.

    """
    return _load_dataset("election.csv.gz")


def load_election_geojson() -> pd.DataFrame:
    """
    Load and return the electron geojson file.

    Each feature represents an electoral district in the 2013 Montreal mayoral
    election.

    Returns
    -------
    pandas.DataFrame
        A GeoJSON-formatted `dict` with 58 polygon or multi-polygon features
        whose `id` is an electoral district numerical ID and whose `district`
        property is the ID and district name.

    """
    return _load_dataset("election.geojson.gz")


def load_flights() -> pd.DataFrame:
    """
    Load and return the flights dataset.

    Returns
    -------
    pandas.DataFrame

    """
    from calendar import month_name

    category_types = {"month": CatType(categories=month_name[1:], ordered=True)}

    return _load_dataset("flights.csv.gz").astype(category_types)


def load_gapminder() -> pd.DataFrame:
    """
    Load and return the gapminder dataset.

    Each row represents a country on a given year.
    https://www.gapminder.org/data/

    Returns
    -------
    pandas.DataFrame
        A `pandas.DataFrame` with 1704 rows and the following columns:
        `['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap',
        'iso_alpha', 'iso_num']`.

    """
    return _load_dataset("gapminder.csv.gz")


def load_iris() -> pd.DataFrame:
    """
    Load and return the iris dataset (classification).

    The iris dataset is a multi-class classification dataset.

    Each row represents a flower.
    https://en.wikipedia.org/wiki/Iris_flower_data_set

    Returns
    -------
    pandas.DataFrame
        A `pandas.DataFrame` with 150 rows and the following columns:
        `['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
        'species', 'species_id']`.

    """
    return _load_dataset("iris.csv.gz")


def load_tips() -> pd.DataFrame:
    """
    Load and return the tips dataset.

    Each row represents a restaurant bill.
    https://vincentarelbundock.github.io/Rdatasets/doc/reshape2/tips.html

    Returns
    -------
    pandas.DataFrame
        A `pandas.DataFrame` with 244 rows and the following columns:
        `['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']`.

    """
    category_types = {
        "day": CatType(categories=["Thur", "Fri", "Sat", "Sun"], ordered=True),
        "sex": CatType(categories=["Male", "Female"], ordered=True),
        "time": CatType(categories=["Lunch", "Dinner"], ordered=True),
        "smoker": CatType(categories=["Yes", "No"], ordered=True),
    }

    return _load_dataset("tips.csv.gz").astype(category_types)


def load_titanic() -> pd.DataFrame:
    """
    Load and return the titanic dataset (classification).

    Returns
    -------
    pandas.DataFrame

    """
    category_types = {
        "class": CatType(categories=["First", "Second", "Third"], ordered=True),
        "deck": CatType(categories=list("ABCDEFG"), ordered=True),
    }

    return _load_dataset("titanic.csv.gz").astype(category_types)


def load_wind() -> pd.DataFrame:
    """
    Load and return the wind dataset.

    Each row represents a level of wind intensity in a cardinal direction, and
    its frequency.

    Returns
    -------
    pandas.DataFrame
        A `pandas.DataFrame` with 128 rows and the following columns:
        `['direction', 'strength', 'frequency']`.

    """
    return _load_dataset("wind.csv.gz")


def _load_dataset(name: str) -> pd.DataFrame:
    filename = os.path.join("data", "datasets", name)

    if not resource_exists(filename):
        raise SpiralError(f"The dataset file '{name}' does not exists.")

    filename = resource_filename(filename)

    return read_data(filename)


loaders = {
    "carshare": load_carshare,
    "election": load_election,
    "election_geojson": load_election_geojson,
    "flights": load_flights,
    "gapminder": load_gapminder,
    "iris": load_iris,
    "tips": load_tips,
    "titanic": load_titanic,
    "wind": load_wind,
}
