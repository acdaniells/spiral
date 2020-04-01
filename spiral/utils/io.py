"""
Spiral IO utility.
"""

from spiral.core.exc import SpiralError

import pandas as pd
import pkg_resources


def get_package_name() -> str:
    """
    Get the package name.

    Returns
    -------
    str
        The package name.

    """
    return __name__.split(".")[0]


def resource_exists(filename: str) -> bool:
    """
    Check if a package resource exists.

    Parameters
    ----------
    filename : str
        The filename.

    Returns
    -------
    bool
        True if the file exists otherwise False.

    """
    return pkg_resources.resource_exists(get_package_name(), filename)


def resource_filename(filename: str) -> str:
    """
    Check if a package resource exists.

    Parameters
    ----------
    filename : str
        The filename.

    Returns
    -------
    str
        True if the file exists otherwise False.

    """
    return pkg_resources.resource_filename(get_package_name(), filename)


def open_file(filename: str, compression: str = "infer"):
    if filename.endswith(".gz"):
        import gzip

        with gzip.GzipFile(filename, "r") as fp:
            return fp.read()
    else:
        with open(filename) as fp:
            return fp.read()


def read_data(filename: str, compression="infer"):
    from pathlib import Path

    extensions = Path(filename).suffixes

    if ".csv" in extensions:
        return read_csv(filename, compression=compression)
    elif ".json" in extensions or ".geojson" in extensions:
        return read_json(filename, compression=compression)
    else:
        raise SpiralError(f"Unrecognised extension(s): {extensions}")


def read_csv(filename: str, **kwargs) -> pd.DataFrame:
    """
    Read a CSV file into a data frame.

    Parameters
    ----------
    filename : str
        The filename.

    **kwargs
        The keyword arguments for the pandas.read_csv call.

    Returns
    -------
    DataFrame
        A pandas DataFrame containing the CSV data.

    """
    import pandas as pd

    return pd.read_csv(filename, **kwargs)


def read_json(filename: str, compression="infer") -> dict:
    import json

    return json.loads(open_file(filename, compression))
