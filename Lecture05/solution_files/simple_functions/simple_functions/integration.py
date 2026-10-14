from scipy.integrate import quad

__all__ = ['integrate']


def integrate(f, a, b):
    """Return the integral of the function f from a to b.

    A thin wrapper around scipy.integrate.quad, which also returns an
    estimate of the error; here we keep only the value.
    """
    value, _ = quad(f, a, b)
    return value
