"""Element-wise multiplication and division of arrays."""

import numpy as np

from ._checks import same_shape

__all__ = ['multiply_arrays', 'divide_arrays']


def multiply_arrays(a, b):
    """
    Multiply two arrays element by element.

    Parameters
    ----------
    a, b : array_like
        Arrays of the same shape.

    Returns
    -------
    numpy.ndarray
        The element-wise product ``a * b``.

    Raises
    ------
    ValueError
        If the shapes of `a` and `b` differ.

    Examples
    --------
    >>> multiply_arrays([1, 2, 3], [4, 5, 6])
    array([ 4., 10., 18.])
    """
    a, b = same_shape(a, b)
    return np.multiply(a, b)


def divide_arrays(a, b):
    """
    Divide one array by another, element by element.

    Parameters
    ----------
    a, b : array_like
        Arrays of the same shape; no element of `b` may be zero.

    Returns
    -------
    numpy.ndarray
        The element-wise quotient ``a / b``.

    Raises
    ------
    ValueError
        If the shapes of `a` and `b` differ.
    ZeroDivisionError
        If any element of `b` is zero (NumPy itself would only warn, and
        return ``inf`` or ``nan``).

    Examples
    --------
    >>> divide_arrays([1, 4, 9], [1, 2, 3])
    array([1., 2., 3.])
    """
    a, b = same_shape(a, b)
    if np.any(b == 0):
        raise ZeroDivisionError("division by an array with a zero element")
    return np.divide(a, b)
