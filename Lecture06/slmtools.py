"""A very small number of helpers for Lecture 06.

Deliberately tiny. The whole point of today's lecture is that there is no black
box, so nothing that matters lives in here - only corpus loading and one
plotting convenience. Every model, every distribution and every gradient is
written out in the notebook where you can see it.
"""

import inspect
import pathlib
import urllib.request

import numpy as np

DATA_DIR = pathlib.Path(__file__).resolve().parent / "data"

SHAKESPEARE_URL = (
    "https://raw.githubusercontent.com/karpathy/char-rnn/master/"
    "data/tinyshakespeare/input.txt"
)

# Used only if data/shakespeare.txt is missing *and* there is no network.
# It is far too small to train anything convincing, and only enough for the
# first few cells of the notebook: most of the lecture needs the real corpus.
_FALLBACK = """
First Citizen:
Before we proceed any further, hear me speak.

All:
Speak, speak.

First Citizen:
You are all resolved rather to die than to famish?

All:
Resolved. resolved.

MENENIUS:
There was a time when all the body's members
Rebell'd against the belly, thus accused it:
That only like a gulf it did remain
I' the midst o' the body, idle and unactive,
Still cupboarding the viand, never bearing
Like labour with the rest, where the other instruments
Did see and hear, devise, instruct, walk, feel,
And, mutually participate, did minister
Unto the appetite and affection common
Of the whole body.

MARCIUS:
He that will give good words to thee will flatter
Beneath abhorring. What would you have, you curs,
That like nor peace nor war? the one affrights you,
The other makes you proud.
""" * 12


def load_text(name="shakespeare"):
    """Return a corpus as a single string.

    Parameters
    ----------
    name : {'shakespeare', 'python'}
        'shakespeare' loads data/shakespeare.txt, downloading it if necessary
        and falling back to a small embedded excerpt if that fails.
        'python' builds a corpus of Python source code at run time out of the
        standard library, so it needs no download at all.

    Returns
    -------
    str
    """
    if name == "python":
        return _python_corpus()
    if name != "shakespeare":
        raise ValueError(f"unknown corpus {name!r}; expected 'shakespeare' or 'python'")

    target = DATA_DIR / "shakespeare.txt"
    if target.exists():
        return target.read_text(encoding="utf-8")

    try:
        DATA_DIR.mkdir(exist_ok=True)
        # Download to a temporary name and rename only once it is complete, so
        # that an interrupted download never leaves a truncated corpus behind.
        partial = target.with_name(target.name + ".part")
        urllib.request.urlretrieve(SHAKESPEARE_URL, partial)
        partial.replace(target)
        return target.read_text(encoding="utf-8")
    except Exception as exc:                                   # noqa: BLE001
        print(f"Could not download the corpus ({exc}).")
        print("Falling back to a small embedded excerpt. It is only enough for the")
        print("first few cells: most of the lecture needs the real corpus, so run")
        print("download_data.py when you next have a network connection.")
        return _FALLBACK


def _python_corpus():
    """Build a corpus of Python source out of the standard library.

    No download required, and it is code the students can actually read.
    """
    import bisect
    import dataclasses
    import fractions
    import random
    import statistics

    modules = [statistics, fractions, dataclasses, random, bisect]
    return "\n\n".join(inspect.getsource(m) for m in modules)


def plot_matrix(M, labels=None, title=None, ax=None, cmap="Blues"):
    """Show a (small) matrix as a heatmap, with character labels on the axes.

    Used for the bigram count matrix and for attention weights.
    """
    import matplotlib.pyplot as plt

    if ax is None:
        _, ax = plt.subplots(figsize=(8, 7))

    im = ax.imshow(np.asarray(M), cmap=cmap)
    ax.figure.colorbar(im, ax=ax, fraction=0.046)

    if labels is not None:
        # repr turns '\n' into a visible \n; a space would be invisible, so it becomes ␣
        pretty = [("␣" if c == " " else repr(c)[1:-1]) if isinstance(c, str) else str(c) for c in labels]
        ax.set_xticks(range(len(pretty)), pretty, fontsize=7, rotation=90)
        ax.set_yticks(range(len(pretty)), pretty, fontsize=7)
    if title:
        ax.set_title(title)
    return ax
