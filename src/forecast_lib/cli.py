from pathlib import Path
from forecast_lib.run_manifest import write_run_manifest
from forecast_lib.evaluate import evaluate
from forecast_lib.promote import promote
import sys
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

    eval_parser = subparsers.add_parser("evaluate", help="Evaluate a trained model")
    eval_parser.add_argument("--run-id", required=True)
    eval_parser.add_argument("--output-dir", default="artifacts")
    eval_parser.add_argument("--force", action="store_true")

    promote_parser = subparsers.add_parser("promote", help="Promote a run to production")
    promote_parser.add_argument("--run-id", required=True)
    promote_parser.add_argument("--output-dir", default="artifacts")
    promote_parser.add_argument("--force", action="store_true")

    pipe_parser = subparsers.add_parser("pipeline", help="Run train → evaluate → promote")
    pipe_parser.add_argument("--run-id", required=True)
    pipe_parser.add_argument("--output-dir", default="artifacts")
    pipe_parser.add_argument("--force", action="store_true")


    args = parser.parse_args()

    try:
        if args.command == "add":
            print(add(args.a, args.b))

        elif args.command == "train":
            train(run_id=args.run_id, output_dir=args.output_dir, force=args.force)

        elif args.command == "evaluate":
            evaluate(run_id=args.run_id, output_dir=args.output_dir, force=args.force)

        elif args.command == "promote":
            promote(run_id=args.run_id, output_dir=args.output_dir, force=args.force)

        elif args.command == "pipeline":
            run_dir = Path(args.output_dir) / args.run_id
            steps = ["train", "evaluate", "promote"]

            try:
                train(run_id=args.run_id, output_dir=args.output_dir, force=args.force)
                evaluate(run_id=args.run_id, output_dir=args.output_dir, force=args.force)
                promote(run_id=args.run_id, output_dir=args.output_dir, force=args.force)
                write_run_manifest(run_dir, status="success", steps=steps)
            except Exception:
                write_run_manifest(run_dir, status="failure", steps=steps)
                raise

    except Exception as e:
        # Critical: non-zero exit code signals failure to scheduler
        print(f"ERROR: {e}", file=sys.stderr)
        raise SystemExit(1)
