"""Mean, median and standard deviation."""

import numpy as np

__all__ = ['mean', 'median', 'standard_deviation']


def _values(x):
    x = np.asarray(x, dtype=float)
    if x.size == 0:
        raise ValueError("the statistics of an empty array are not defined")
    return x


def mean(x):
    """
    Mean of the values in an array.

    Parameters
    ----------
    x : array_like
        The values (an array of any shape, or a list).

    Returns
    -------
    float
        The mean of all the values in `x`.

    Raises
    ------
    ValueError
        If `x` is empty.

    Examples
    --------
    >>> mean([1, 2, 3, 4])
    2.5
    """
    return float(np.mean(_values(x)))


def median(x):
    """
    Median of the values in an array.

    Parameters
    ----------
    x : array_like
        The values (an array of any shape, or a list).

    Returns
    -------
    float
        The median of all the values in `x`: the middle value once sorted,
        or the mean of the two middle values if there is an even number.

    Raises
    ------
    ValueError
        If `x` is empty.

    Examples
    --------
    >>> median([3, 1, 2])
    2.0
    >>> median([4, 1, 3, 2])
    2.5
    """
    return float(np.median(_values(x)))


def standard_deviation(x, ddof=0):
    """
    Standard deviation of the values in an array.

    Parameters
    ----------
    x : array_like
        The values (an array of any shape, or a list).
    ddof : int, optional
        "Delta degrees of freedom": the sum of squared deviations is divided
        by ``N - ddof``. The default, 0, gives the population standard
        deviation; ``ddof=1`` gives the sample standard deviation.

    Returns
    -------
    float
        The standard deviation of all the values in `x`.

    Raises
    ------
    ValueError
        If `x` is empty.

    Examples
    --------
    >>> standard_deviation([2, 4, 4, 4, 5, 5, 7, 9])
    2.0
    """
    return float(np.std(_values(x), ddof=ddof))
