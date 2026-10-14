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

@pytest.mark.parametrize('number, expected', [
    (5, 120),
    (3, 6),
    (1, 1),
    (0, 1),
])
def test_factorial(self, number, expected):
    """factorial is right for small numbers, including 0! = 1."""
    assert factorial(number) == expected