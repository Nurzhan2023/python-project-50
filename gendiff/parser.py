import argparse
from gendiff.diff_generator import generate_diff


def args_parser():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="Path to the first file")
    parser.add_argument("second_file", help="Path to the second file")
    parser.add_argument(
        "-f", "--format",
        help="Set output format (supported: stylish, plain, json)",
        default="stylish"
    )
    args = parser.parse_args()

    return generate_diff(args.first_file, args.second_file, 
                         format_name=args.format)
