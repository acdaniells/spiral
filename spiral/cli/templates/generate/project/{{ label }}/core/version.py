"""
{{ label }} core version module.
"""

from spiral import get_version as spiral_get_version

VERSION = (0, 0, 1, "alpha", 0)


def get_version(version=VERSION):
    return spiral_get_version(version)
