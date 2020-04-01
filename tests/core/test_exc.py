from spiral.core.exc import SpiralError

from pytest import raises


class TestExceptions:
    def test_spiralerror(self):
        with raises(SpiralError, match=".*spiral exception.*"):
            raise SpiralError("test spiral exception message")
