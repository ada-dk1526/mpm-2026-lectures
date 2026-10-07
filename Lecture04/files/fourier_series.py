"""Fourier series of f(x) = x**2 on [-pi, pi], for Lecture 4's debugging demo.

The partial sums should get closer and closer to x**2 as N grows, but the
plot shows they don't. Find out why with print statements, breakpoint() or
`from IPython import embed; embed()` (the comment in eval_fc marks a good
place to start), or with VS Code's debugger. From the files folder:

    python fourier_series.py
"""

import matplotlib.pyplot as plt
import numpy as np


def eval_fc(x, N):
    """Partial sum of the Fourier series of x**2, up to the term n = N."""
    f = np.pi**2/3
    for i in range(1, N+1):
        f += 4*(-1)**i/N**2*np.cos(i*x)
        # To investigate, add a print statement, breakpoint() or embed() here
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
