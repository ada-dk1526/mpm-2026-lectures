"""Exercise 1: basic arithmetic from the command line, with argparse.

    python arithmetic.py -o add -n1 10 -n2 5
"""
import argparse
import sys


def main():
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Perform basic arithmetic operations.")

    # Add arguments. `choices` makes argparse reject any other operation:
    # it prints an error message and exits with status 2.
    parser.add_argument('-o', '--operation', required=True,
                        choices=['add', 'subtract', 'multiply', 'divide'],
                        help='The operation to perform.')
    parser.add_argument('-n1', '--num1', type=float, required=True,
                        help='The first number.')
    parser.add_argument('-n2', '--num2', type=float, required=True,
                        help='The second number.')

    # Parse the arguments
    args = parser.parse_args()

    # Perform the operation
    if args.operation == 'add':
        result = args.num1 + args.num2
        symbol = '+'
    elif args.operation == 'subtract':
        result = args.num1 - args.num2
        symbol = '-'
    elif args.operation == 'multiply':
        result = args.num1 * args.num2
        symbol = '*'
    else:  # divide
        if args.num2 == 0:
            # Print the message to stderr and exit with status 1.
            sys.exit("Error: Division by zero is not allowed.")
        result = args.num1 / args.num2
        symbol = '/'
    print(f"The result of {args.num1} {symbol} {args.num2} is: {result}")


if __name__ == "__main__":
    main()
