# mycoolpackage

Simple numerical operations on NumPy arrays: matrix addition and subtraction, element-wise
multiplication and division, and basic statistics (mean, median and standard deviation).
A worked solution to Exercise 2 of MPM Lecture 5 (Python packaging).

## Installation

From this folder (the one containing `pyproject.toml`):

```bash
pip install -e ".[dev]"
```

This installs `mycoolpackage` and NumPy; `[dev]` adds `pytest` and `flake8`.

## Usage

```python
import numpy as np
import mycoolpackage as mcp

a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])

mcp.add_matrices(a, b)        # array([[ 6.,  8.], [10., 12.]])
mcp.divide_arrays(b, a)       # element-wise b / a
mcp.mean([1, 2, 3, 4])        # 2.5
mcp.standard_deviation([2, 4, 4, 4, 5, 5, 7, 9])   # 2.0
```

## Tests

```bash
pytest --doctest-modules
flake8 .
```

## License

MIT (see `LICENSE`).
