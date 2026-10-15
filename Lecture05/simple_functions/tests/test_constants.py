import numpy as np
import pytest

from simple_functions import pi


class TestPi:
    """Tests for the constants in constants.py."""

    def test_pi(self):
        """Three terms of Ramanujan's series give pi to double precision."""
        assert pi(2) == pytest.approx(np.pi, abs=1e-12)
        