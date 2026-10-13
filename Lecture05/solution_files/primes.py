"""Exercise 4: the first 20 prime numbers, or the primes below n.

    python primes.py        # the first 20 primes
    python primes.py 50     # the primes smaller than 50
"""
import math
import sys


def is_prime(n, smaller_primes):
    """Return True if n is prime, given all the primes smaller than n."""
    for p in smaller_primes:
        if p > math.isqrt(n):  # no factor up to sqrt(n): n is prime
            return True
        if n % p == 0:  # p divides n exactly
            return False
    return n > 1


def first_primes(count):
    """Return a list of the first `count` prime numbers."""
    primes = []
    n = 2
    while len(primes) < count:
        if is_prime(n, primes):
            primes.append(n)
        n += 1
    return primes


def primes_below(limit):
    """Return a list of the prime numbers smaller than `limit`."""
    primes = []
    for n in range(2, limit):
        if is_prime(n, primes):
            primes.append(n)
    return primes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(primes_below(int(sys.argv[1])))
    else:
        print(first_primes(20))
