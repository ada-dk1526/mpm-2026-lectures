"""Fourier series of f(x) = x**2 on [-pi, pi]: the fixed version of
Lecture04/files/fourier_series.py.

The bug was in eval_fc: each term was divided by N**2 (the number of terms)
instead of i**2 (the square of its own index n), so the coefficients were
all tiny and the partial sums never approached x**2. Now they do: with
N = 100 the sum is within 0.04 of x**2 everywhere on [-pi, pi].
"""

import matplotlib.pyplot as plt
import numpy as np


def eval_fc(x, N):
    """Partial sum of the Fourier series of x**2, up to the term n = N."""
    f = np.pi**2/3
    for i in range(1, N+1):
        f += 4*(-1)**i/i**2*np.cos(i*x)
    return f


x = np.linspace(-np.pi, np.pi, 1000)

plt.figure(figsize=(12, 8))
plt.plot(x, x**2, "k--", label="$y(x)=x^2$")
for N in (1, 2, 5, 10, 100):
    plt.plot(x, eval_fc(x, N), label=f"$N={N}$")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim((-1.0, 11.5))
plt.legend()
plt.show()
