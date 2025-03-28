# gendiff/diff_generator.py
from gendiff.read import read_file
from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.json import format_json


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = {}

    for key in keys:
        if key not in data1:
            diff[key] = {"status": "added", "value": data2[key]}
        elif key not in data2:
            diff[key] = {"status": "removed", "value": data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                "status": "nested",
                "children": build_diff(data1[key], data2[key])
            }
        elif data1[key] == data2[key]:
            diff[key] = {"status": "unchanged", "value": data1[key]}
        else:
            diff[key] = {
                "status": "modified",
                "old_value": data1[key],
                "new_value": data2[key]
            }

    return diff


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    diff = build_diff(data1, data2)

    # Выбор форматирования
    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return format_plain(diff)
    elif format_name == "json":
        return format_json(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
