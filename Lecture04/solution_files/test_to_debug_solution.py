"""Regression test for the second bug in to_debug.py: every optimizer must be benchmarked.

`capsys` is a built-in pytest fixture that captures what the code prints.
"""
from to_debug_solution import OPTIMIZERS, compare_optimizers


def test_every_optimizer_makes_function_calls(capsys):
    compare_optimizers(OPTIMIZERS)
    lines = capsys.readouterr().out.splitlines()[1:]          # skip the heading
    counts = [int(line.split(":")[1].split()[0]) for line in lines]
    assert len(counts) == len(OPTIMIZERS)
    assert all(count > 0 for count in counts)
