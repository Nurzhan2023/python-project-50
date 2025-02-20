# gendiff/parser.py

import argparse
from gendiff.diff_generator import generate_diff


def args_parser():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="path to the first file")
    parser.add_argument("second_file", help="path to the second file")
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        default="stylish"
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
