"""Simple numerical operations on NumPy arrays."""

from .linear_algebra import (add_matrices, divide_arrays, multiply_arrays,
                             subtract_matrices)
from .statistics import mean, median, standard_deviation

__all__ = ['add_matrices', 'subtract_matrices', 'multiply_arrays',
           'divide_arrays', 'mean', 'median', 'standard_deviation']
