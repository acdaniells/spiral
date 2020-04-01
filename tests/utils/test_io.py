from spiral.core.exc import SpiralError
from spiral.utils.io import read_data

from cement.utils import fs
from pytest import raises


def test_read_data():
    filename = fs.join("..", "..", "README.md")

    with raises(SpiralError, match=".*Unrecognised extension.*"):
        read_data(filename)
