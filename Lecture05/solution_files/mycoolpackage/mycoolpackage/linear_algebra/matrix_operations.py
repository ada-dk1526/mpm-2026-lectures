"""Matrix addition and subtraction."""

import numpy as np

from ._checks import same_shape

__all__ = ['add_matrices', 'subtract_matrices']


def _matrices(a, b):
    a, b = same_shape(a, b)
    if a.ndim != 2:
        raise ValueError(f"expected matrices (2D arrays), got {a.ndim}D")
    return a, b


def add_matrices(a, b):
    """
    Add two matrices.

    Parameters
    ----------
    a, b : array_like
        Matrices (2D) of the same shape.

    Returns
    -------
    numpy.ndarray
        The matrix ``a + b``.

    Raises
    ------
    ValueError
        If `a` and `b` are not matrices of the same shape.

    Examples
    --------
    >>> add_matrices([[1, 2], [3, 4]], [[10, 20], [30, 40]])
    array([[11., 22.],
           [33., 44.]])
    """
    a, b = _matrices(a, b)
    return np.add(a, b)


def subtract_matrices(a, b):
    """
    Subtract one matrix from another.

    Parameters
    ----------
    a, b : array_like
        Matrices (2D) of the same shape.

    Returns
    -------
    numpy.ndarray
        The matrix ``a - b``.

    Raises
    ------
    ValueError
        If `a` and `b` are not matrices of the same shape.

    Examples
    --------
    >>> subtract_matrices([[1, 2], [3, 4]], [[1, 1], [1, 1]])
    array([[0., 1.],
           [2., 3.]])
    """
    a, b = _matrices(a, b)
    return np.subtract(a, b)
