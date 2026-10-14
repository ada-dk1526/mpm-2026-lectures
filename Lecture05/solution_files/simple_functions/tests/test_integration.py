import numpy as np
import pytest

from simple_functions import integrate


class TestIntegrate:
    """Tests for integrate in integration.py."""

    @pytest.mark.parametrize('f, a, b, expected', [
        (np.sin, 0.0, np.pi, 2.0),
        (lambda x: x**2, 0.0, 3.0, 9.0),
        (np.exp, 0.0, 1.0, np.e - 1.0),
    ])
    def test_integrate(self, f, a, b, expected):
        """integrate gets known integrals right."""
        assert integrate(f, a, b) == pytest.approx(expected)
