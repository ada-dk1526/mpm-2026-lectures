from functools import cache

__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    """Return the sum of the items in iterable."""
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    """Return n! (n factorial) for a non-negative integer n."""
    return n * factorial(n-1) if n else 1
