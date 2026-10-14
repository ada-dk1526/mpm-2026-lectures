import math

__all__ = ['sin']


def sin(x, terms=20):
    """Return sin(x) for a real number x, from its Taylor series about 0.

    x is first reduced to the interval [-pi, pi] (sin is periodic), where
    `terms` terms of the series are enough for double precision.
    """
    x = math.remainder(x, 2*math.pi)
    total = 0.0
    term = x  # the first term of the series, x**1 / 1!
    for n in range(terms):
        total += term
        term *= -x*x / ((2*n + 2)*(2*n + 3))  # the next term, from this one
    return total
