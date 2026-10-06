import pytest

import foo


def test_two_roots():
    assert foo.solve_quadratic(1, 0, -1) == (-1.0, 1.0)


def test_one_root():
    assert foo.solve_quadratic(1, 0, 0) == 0.0


def test_no_real_roots():
    assert foo.solve_quadratic(1, 0, 1) is None


def test_irrational_roots():
    # The roots of x^2 - 2 are not exact in floating point: compare with a tolerance, not ==
    assert foo.solve_quadratic(1, 0, -2) == pytest.approx((-2**0.5, 2**0.5))
