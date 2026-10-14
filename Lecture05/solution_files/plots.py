"""Exercise 6: plot sin, cos and tan over [0, 2 pi], on screen and to files.

    python plots.py
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 1001)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label=r'$\sin(x)$')
ax.plot(x, np.cos(x), label=r'$\cos(x)$')
ax.plot(x, np.tan(x), label=r'$\tan(x)$')
ax.set_ylim(-3, 3)  # tan(x) goes to +/- infinity at pi/2 and 3 pi/2
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend()
fig.savefig('trig.png')
fig.savefig('trig.pdf')
plt.show()  # shows the plot in a window, if your system can open one
