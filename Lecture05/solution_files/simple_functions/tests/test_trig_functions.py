import numpy as np
import pytest

from simple_functions import sin


class TestSin:
    """Tests for sin in trig_functions.py."""

    @pytest.mark.parametrize('x', [0.0, 0.5, np.pi/6, np.pi/2, 2.0, np.pi,
                                   4.0, 3*np.pi/2, 6.0, 2*np.pi])
    def test_sin_in_one_period(self, x):
        """sin agrees with numpy for x in [0, 2 pi]."""
        assert sin(x) == pytest.approx(np.sin(x), abs=1e-14)

    @pytest.mark.parametrize('x', [-1.0, -10.0, 10.0, 100.0, 1000.5])
    def test_sin_outside_one_period(self, x):
        """sin agrees with numpy for negative x and x > 2 pi."""
        assert sin(x) == pytest.approx(np.sin(x), abs=1e-12)

    def test_sin_known_values(self):
        """sin(pi/6) = 1/2 and sin(pi/2) = 1."""
        assert sin(np.pi/6) == pytest.approx(0.5)
        assert sin(np.pi/2) == pytest.approx(1.0)
