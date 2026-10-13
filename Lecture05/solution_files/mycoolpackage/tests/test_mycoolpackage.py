import numpy as np
import pytest

import mycoolpackage as mcp

A = np.array([[1.0, 2.0], [3.0, 4.0]])
B = np.array([[5.0, 6.0], [7.0, 8.0]])


class TestLinearAlgebra:
    """Tests for the linear_algebra subpackage."""

    def test_add_matrices(self):
        np.testing.assert_allclose(mcp.add_matrices(A, B),
                                   [[6.0, 8.0], [10.0, 12.0]])

    def test_subtract_matrices(self):
        np.testing.assert_allclose(mcp.subtract_matrices(B, A),
                                   [[4.0, 4.0], [4.0, 4.0]])

    def test_add_matrices_accepts_lists(self):
        np.testing.assert_allclose(mcp.add_matrices([[1, 2]], [[3, 4]]),
                                   [[4.0, 6.0]])

    @pytest.mark.parametrize('function', [mcp.add_matrices,
                                          mcp.subtract_matrices])
    def test_matrix_shapes_must_match(self, function):
        with pytest.raises(ValueError):
            function(A, np.ones((3, 2)))

    def test_matrices_must_be_2d(self):
        with pytest.raises(ValueError):
            mcp.add_matrices([1, 2], [3, 4])

    def test_multiply_arrays(self):
        np.testing.assert_allclose(mcp.multiply_arrays(A, B),
                                   [[5.0, 12.0], [21.0, 32.0]])

    def test_divide_arrays(self):
        np.testing.assert_allclose(mcp.divide_arrays([1.0, 1.0], [3.0, 7.0]),
                                   [1/3, 1/7])

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            mcp.divide_arrays([1.0, 2.0], [1.0, 0.0])

    @pytest.mark.parametrize('function', [mcp.multiply_arrays,
                                          mcp.divide_arrays])
    def test_array_shapes_must_match(self, function):
        with pytest.raises(ValueError):
            function([1.0, 2.0], [1.0, 2.0, 3.0])


class TestStatistics:
    """Tests for the statistics subpackage."""

    @pytest.mark.parametrize('x, expected', [
        ([1, 2, 3, 4], 2.5),
        ([[1, 2], [3, 4]], 2.5),
        ([0.1, 0.2], 0.15),
    ])
    def test_mean(self, x, expected):
        assert mcp.mean(x) == pytest.approx(expected)

    @pytest.mark.parametrize('x, expected', [
        ([3, 1, 2], 2.0),
        ([4, 1, 3, 2], 2.5),
    ])
    def test_median(self, x, expected):
        assert mcp.median(x) == pytest.approx(expected)

    def test_standard_deviation(self):
        x = [2, 4, 4, 4, 5, 5, 7, 9]
        assert mcp.standard_deviation(x) == pytest.approx(2.0)
        assert mcp.standard_deviation(x, ddof=1) == pytest.approx(
            np.sqrt(32 / 7))

    @pytest.mark.parametrize('function', [mcp.mean, mcp.median,
                                          mcp.standard_deviation])
    def test_empty_input(self, function):
        with pytest.raises(ValueError):
            function([])
