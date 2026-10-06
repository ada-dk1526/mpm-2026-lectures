"""Fit a straight line to some measurements and report how well it fits.

This script runs without any error, but the root-mean-square (RMS) error it
prints is far too large for points that lie so close to a straight line.
Can you find the problem, reduce it to a minimal failing example (MFE),
and fix it?
"""
import numpy as np

# A small table of measurements: x in the first column, y in the second
data = np.array([[0.0, 1.1],
                 [1.0, 2.9],
                 [2.0, 5.2],
                 [3.0, 6.8],
                 [4.0, 9.1]])


def load_columns(table):
    """Split the table into the x values and the measured y values."""
    x = table[:, 0]
    y = table[:, 1:]
    return x, y


def fit_line(x, y):
    """Least-squares straight line through the points: returns (m, c) for y = m*x + c."""
    m, c = np.polyfit(x, np.ravel(y), 1)
    return m, c


def rms_error(y, y_fit):
    """Root-mean-square difference between the measured and fitted values."""
    return np.sqrt(np.mean((y - y_fit)**2))


x, y = load_columns(data)
m, c = fit_line(x, y)
y_fit = m*x + c
print(f"Fitted line: y = {m:.3f} x + {c:.3f}")
print(f"RMS error:   {rms_error(y, y_fit):.3f}")
