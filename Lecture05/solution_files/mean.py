"""Exercise 5: the mean of a sequence of numbers.

    python mean.py 1 5 7 13 8
    python mean.py -x 2A 10     # hexadecimal; -b for binary, -o for octal
"""
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Print the mean of a sequence of numbers.")
    parser.add_argument('numbers', nargs='*',
                        help='The numbers (decimal unless -b, -o or -x).')
    base = parser.add_mutually_exclusive_group()
    base.add_argument('-b', dest='base', action='store_const', const=2,
                      help='The numbers are binary (base 2).')
    base.add_argument('-o', dest='base', action='store_const', const=8,
                      help='The numbers are octal (base 8).')
    base.add_argument('-x', dest='base', action='store_const', const=16,
                      help='The numbers are hexadecimal (base 16).')
    args = parser.parse_args()

    if not args.numbers:
        sys.exit("Error: give at least one number.")
    try:
        if args.base:
            values = [int(n, args.base) for n in args.numbers]
        else:
            values = [float(n) for n in args.numbers]
    except ValueError as err:
        sys.exit(f"Error: {err}")
    print(sum(values) / len(values))


if __name__ == "__main__":
    main()
