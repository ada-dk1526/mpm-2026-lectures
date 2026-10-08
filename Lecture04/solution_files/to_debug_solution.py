"""
A script to compare different root-finding algorithms: the fixed version.

There were two bugs.

1. `apply_optimizer` ended in a stray comma, so it returned a one-element tuple
   rather than a number, and `sum` failed with
   TypeError: unsupported operand type(s) for +: 'int' and 'tuple'.
   The traceback points straight at the `sum` in `bench_optimizer`; in the debugger
   (`python -m pdb to_debug.py`, then `c`, then `p apply_optimizer(optimizer, func, a, b)`)
   the returned value is visibly a tuple.

2. Once that is fixed, the script runs, but every optimizer after the first reports
   0 function calls. `itertools.product` returns an iterator, which can be used only
   once: the first call of `bench_optimizer` consumes it. The fix is to make a list
   (`list(product(...))`). `test_to_debug_solution.py` is a regression test for it.

Once fixed, the output of the script should look something like this (the exact
numbers vary from run to run, because the brackets are chosen at random):

    Benching 1D root-finder optimizers from scipy.optimize:
                brenth:   604678 total function calls
                brentq:   594454 total function calls
                ridder:   778394 total function calls
                bisect:  2148380 total function calls
"""
from itertools import product

import numpy as np
from scipy import optimize

FUNCTIONS = (np.tan,  # Dilating map
             np.tanh, # Contracting map
             lambda x: x**3 + 1e-4*x, # Almost null gradient at the root
             lambda x: x+np.sin(2*x), # Non monotonous function
             lambda x: 1.1*x+np.sin(4*x), # Function with several local maxima
            )

OPTIMIZERS = (optimize.brenth, optimize.brentq, optimize.ridder,
              optimize.bisect)


def apply_optimizer(optimizer, func, a, b):
    """ Return the number of function calls given a root-finding optimizer,
        a function and upper and lower bounds.
    """
    return optimizer(func, a, b, full_output=True)[1].function_calls


def bench_optimizer(optimizer, param_grid):
    """ Find roots for all the functions, and upper and lower bounds
        given and return the total number of function calls.
    """
    return sum(apply_optimizer(optimizer, func, a, b)
               for func, a, b in param_grid)


def compare_optimizers(optimizers):
    """ Compare all the optimizers given on a grid of a few different
        functions all admitting a single root in zero and a upper and
        lower bounds.
    """
    random_a = -1.3 + np.random.random(size=100)
    random_b =   .3 + np.random.random(size=100)
    param_grid = list(product(FUNCTIONS, random_a, random_b))
    print("Benching 1D root-finder optimizers from scipy.optimize:")
    for optimizer in OPTIMIZERS:
        print('% 20s: % 8i total function calls' % (
                    optimizer.__name__,
                    bench_optimizer(optimizer, param_grid)
                ))


if __name__ == '__main__':
    compare_optimizers(OPTIMIZERS)
