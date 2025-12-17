import argparse
from forecast_lib.utils import add
from forecast_lib.train import train

def main() -> None:
    parser = argparse.ArgumentParser(
        description="forecast-lib command line interface"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # add command
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float)
    add_parser.add_argument("b", type=float)

    train_parser = subparsers.add_parser("train", help="Run training job")
    train_parser.add_argument("--run-id", required=True)
    train_parser.add_argument("--output-dir", default="artifacts")
    train_parser.add_argument("--force", action="store_true")

    args = parser.parse_args()

    if args.command == "add":
        print(add(args.a, args.b))

    elif args.command == "train":
        train(run_id=args.run_id, output_dir=args.output_dir, force=args.force)
