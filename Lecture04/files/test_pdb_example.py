# test_pdb_example.py
import math

import pytest


def area_of_circle(r):
    """Compute the area of a circle."""
    if r < 0:
        raise ValueError("radius must be non-negative")
    return math.pi * r**2


def test_area_of_circle():
    """Deliberately failing test, to demonstrate pytest --pdb."""
    result = area_of_circle(2)
    expected = 12.56  # wrong on purpose: the area is 4*pi = 12.566...
    assert result == pytest.approx(expected)
