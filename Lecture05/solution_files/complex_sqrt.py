"""Exercise 8: the complex square roots of a real number."""
import math


def complex_sqrt(x):
    """
    Return the square roots of a real number, as complex numbers.

    Parameters
    ----------
    x : float
        A real number (positive, negative or zero).

    Returns
    -------
    tuple of complex
        The two square roots, ``(r, -r)``. Zero has only one square root,
        so for ``x == 0`` the tuple has a single element.

    Examples
    --------
    >>> complex_sqrt(4)
    ((2+0j), (-2-0j))
    >>> complex_sqrt(-9)
    (3j, (-0-3j))
    >>> complex_sqrt(0)
    (0j,)
    """
    if x == 0:
        return (0j,)
    if x > 0:
        r = complex(math.sqrt(x), 0)
    else:
        r = complex(0, math.sqrt(-x))
    return (r, -r)
