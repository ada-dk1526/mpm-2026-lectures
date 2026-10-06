"""A function whose docstring contains a test.

Run the test with `python docstring_test.py`, `python -m doctest -v docstring_test.py`
or `pytest --doctest-modules docstring_test.py`.
"""


def mean(x):
    """Mean of a list of numbers.

    >>> mean([1, 5, 9])
    5.0
    """
    return sum(x)/len(x)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
