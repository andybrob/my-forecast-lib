import argparse
from forecast_lib.utils import add

def main() -> None:
    parser = argparse.ArgumentParser(
        description="forecast-lib command line interface"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # add command
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float)
    add_parser.add_argument("b", type=float)

    args = parser.parse_args()

    if args.command == "add":
        result = add(args.a, args.b)
        print(result)

