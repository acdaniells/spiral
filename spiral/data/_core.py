"""
Spiral data module.
"""

from ._datasets import loaders


def list_datasets():
    """
    Print the list of available dataset names.
    """

    print(sorted(loaders.keys()))


def load_dataset(name):
    """
    Load a dataset.
    """

    try:
        func = loaders[name]
    except KeyError:
        print(f"Dataset '{name}' is not in available list: {list_datasets()}")
    else:
        return func()
