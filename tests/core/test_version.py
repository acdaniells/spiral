from spiral.core import version


def test_version():
    # ensure that we bump things properly on version changes
    assert version.VERSION[0] == 0
    assert version.VERSION[1] == 0
    assert version.VERSION[2] == 1
    assert version.VERSION[3] == "alpha"
    assert version.VERSION[4] == 0


def test_get_version():
    ver = version.get_version()
    assert ver.startswith("0.0")

    ver = version.get_version((2, 1, 1, "alpha", 1))
    assert ver == "2.1.1a1"

    ver = version.get_version((2, 1, 2, "beta", 2))
    assert ver == "2.1.2b2"

    ver = version.get_version((2, 1, 2, "rc", 3))
    assert ver == "2.1.2c3"

    ver = version.get_version((2, 1, 3, "final", 0))
    assert ver == "2.1.3"
