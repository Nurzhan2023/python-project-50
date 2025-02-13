import argparse
import json
from gendiff.scripts.read import read_file

def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        if key not in data1:  # Если ключ есть только во втором файле
            diff.append(f" + {key}: {data2[key]}")
        elif key not in data2:  # Если ключ есть только в первом файле
            diff.append(f" - {key}: {data1[key]}")
        elif data1[key] == data2[key]:  # Если значения равны
            diff.append(f"   {key}: {data1[key]}")
        else:  # Если значения отличаются
            diff.append(f" - {key}: {data1[key]}")
            diff.append(f" + {key}: {data2[key]}")

    return "{\n" + "\n".join(diff) + "\n}"

def main():
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

if __name__ == '__main__':
    main()
