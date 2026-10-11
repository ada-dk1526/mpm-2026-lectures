"""Fetch the text corpus needed for Lecture 06.

Run this once, from within the `Lecture06` folder, before the lecture:

    python download_data.py

It downloads the `tinyshakespeare` corpus (~1.1 MB, public domain) into
`data/shakespeare.txt`. If you have no network access, the notebook falls
back to a small excerpt embedded in `slmtools.py`, but that is only enough
for its first few cells: most of the lecture needs the real corpus.
"""

import pathlib
import urllib.request

URL = (
    "https://raw.githubusercontent.com/karpathy/char-rnn/master/"
    "data/tinyshakespeare/input.txt"
)

DATA_DIR = pathlib.Path(__file__).resolve().parent / "data"


def main():
    DATA_DIR.mkdir(exist_ok=True)
    target = DATA_DIR / "shakespeare.txt"

    if target.exists():
        print(f"{target} already exists ({target.stat().st_size / 1e6:.2f} MB) - nothing to do.")
        return

    print(f"Downloading {URL}")
    # Download to a temporary name and rename only once it is complete, so that
    # an interrupted download never leaves a truncated corpus behind.
    partial = target.with_name(target.name + ".part")
    urllib.request.urlretrieve(URL, partial)
    partial.replace(target)
    print(f"Wrote {target} ({target.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()
