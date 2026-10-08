"""Solution to the MFE exercise (files/mfe.py).

The bug: `load_columns` keeps y as a column (`table[:, 1:]`, shape (5, 1)), while
`y_fit = m*x + c` has shape (5,). In `rms_error`, `y - y_fit` therefore broadcasts
to a (5, 5) array of every y minus every fitted value, so the mean is over 25 wrong
differences: no error is raised, but the RMS (3.983) is wrong. The correct value is 0.146.

A minimal failing example: three lines, no fitting, no data file.
"""
import numpy as np

y = np.array([[1.0], [2.0], [3.0]])   # a column, shape (3, 1)
y_fit = np.array([1.0, 2.0, 3.0])     # shape (3,)
print((y - y_fit).shape)              # (3, 3), not (3,)

# Fixes (any one of them):
#   - in load_columns, take a 1D column:      y = table[:, 1]
#   - or flatten before subtracting:          np.ravel(y) - y_fit
#   - and make rms_error refuse mismatched shapes, so the bug can't come back silently:
#
#         def rms_error(y, y_fit):
#             if np.shape(y) != np.shape(y_fit):
#                 raise ValueError(f"shapes differ: {np.shape(y)} and {np.shape(y_fit)}")
#             return np.sqrt(np.mean((y - y_fit)**2))
#
# Regression tests (in a test file):
#
#     def test_rms_error_of_an_exact_fit_is_zero():
#         y = np.array([1.0, 2.0, 3.0])
#         assert rms_error(y, y) == 0.0
#
#     def test_rms_error_rejects_mismatched_shapes():
#         with pytest.raises(ValueError):
#             rms_error(np.ones((3, 1)), np.ones(3))
