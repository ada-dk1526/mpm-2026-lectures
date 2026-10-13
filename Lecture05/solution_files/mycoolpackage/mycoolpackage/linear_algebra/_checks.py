"""Input checks shared by the linear_algebra modules."""

import numpy as np


def same_shape(a, b):
    """Return `a` and `b` as arrays, after checking that their shapes match.

    Raises
    ------
    ValueError
        If the shapes of `a` and `b` differ.
    """
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    if a.shape != b.shape:
        raise ValueError(f"shapes differ: {a.shape} and {b.shape}")
    return a, b
