__all__ = ['my_sum']


def my_sum(iterable):
    """Return the sum of the items in iterable."""
    tot = 0
    for i in iterable:
        tot += i
    return tot
