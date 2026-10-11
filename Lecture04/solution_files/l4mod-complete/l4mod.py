
def gauss(a, b):
    """
    Given two matrices, `a` and `b`, with `a` square, the determinant
    of `a` (returned as `det`) and a matrix `x` (returned as `b`) such
    that a*x = b are returned. If `b` is the identity, then `x` is the
    inverse of `a`.

    Parameters
    ----------
    a : np.array or list of lists
        'n x n' array
    b : np.array or list of lists
        'n x m' array

    Returns
    -------
    det : float
        The determinant of a
    b : list of lists
        Solution of Ax=b

    Examples
    --------
    >>> det, x = gauss([[2, 0, -1], [0, 5, 6], [0, -1, 1]], [[2], [1], [2]])
    >>> det
    22.0
    >>> x
    [[1.5], [-1.0], [1.0]]

    Notes
    -----
    See https://en.wikipedia.org/wiki/Gaussian_elimination for further details.

    The inputs are first copied into lists of lists. Swapping two rows with
    ``a[i], a[k] = a[k], a[i]`` is correct for lists, but not for NumPy arrays:
    ``a[k]`` is a view, so after ``a[i] = a[k]`` both rows hold the same values.
    That was the bug found by ``test_gauss_accepts_numpy_arrays``.
    """
    a = [[float(v) for v in row] for row in a]
    b = [[float(v) for v in row] for row in b]
    n = len(a)
    p = len(b[0])
    det = 1.
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det

        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return det, b


def matmul(a, b):
    """
    Matrix product of two matrices given as lists of lists.

    Parameters
    ----------
    a : list of lists
        'n x p' matrix
    b : list of lists
        'p x q' matrix

    Returns
    -------
    c : list of lists
        The 'n x q' product a*b

    Raises
    ------
    ValueError
        If the number of columns of `a` differs from the number of rows of `b`.

    Examples
    --------
    >>> matmul([[1, 2], [3, 4]], [[5], [6]])
    [[17], [39]]
    """
    n, p = len(a), len(a[0])
    p1, q = len(b), len(b[0])
    if p != p1:
        raise ValueError("Incompatible dimensions")
    c = zeromat(n, q)
    for i in range(n):
        for j in range(q):
            c[i][j] = sum(a[i][k]*b[k][j] for k in range(p))
    return c


def zeromat(p, q):
    """
    A 'p x q' matrix of zeros, as a list of lists.

    Examples
    --------
    >>> zeromat(2, 3)
    [[0, 0, 0], [0, 0, 0]]
    """
    return [[0]*q for i in range(p)]


if __name__ == "__main__":
    print('Running l4mod example:')
    a = [[2, 0, -1], [0, 5, 6], [0, -1, 1]]
    b = [[2], [1], [2]]
    print('Setting the matrix A as:')
    print(a)
    print('Setting b as:')
    print(b)
    det, x = gauss(a, b)
    print('The determinant of A is:')
    print(det)
    print('The solution of Ax=b is:')
    print(x)
