# simple_functions

A few simple functions, for practising continuous integration (MPM Lecture 5).

## Installation

From this folder, in the `mpm2026` environment (or any environment with Python 3.10 or later):

```bash
pip install -e ".[dev]"
```

`[dev]` also installs the tools used to check the package, `pytest` and `flake8`.

## Usage

```python
from simple_functions import my_sum

my_sum([1, 2, 3])  # 6
```

## Running the tests

```bash
pytest
flake8 .
```

## License

MIT (see `LICENSE`).
