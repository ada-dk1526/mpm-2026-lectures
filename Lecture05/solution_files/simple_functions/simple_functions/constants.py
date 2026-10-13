from functools import cache

from numpy import sqrt

from simple_functions.functions1 import factorial

__all__ = ['pi']


def pi(terms=1):
    """Approximate pi by summing Ramanujan's series from k = 0 to terms."""
    return 1./(2.*sqrt(2.)/9801.*rsum(terms))


@cache
def rsum(n):
    """Return the sum of the terms k = 0, 1, ..., n of Ramanujan's series."""
    t = factorial(4*n)*(1103+26390*n)/(factorial(n)**4*396**(4*n))
    return t + rsum(n-1) if n else t
