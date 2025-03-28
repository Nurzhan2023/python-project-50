from gendiff.read import read_file
from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.json import format_json


def get_diff_entry(key, data1, data2):
    if key not in data1:
        return {"status": "added", "value": data2[key]}
    if key not in data2:
        return {"status": "removed", "value": data1[key]}
    if isinstance(data1[key], dict) and isinstance(data2[key], dict):
        return {
            "status": "nested",
            "children": build_diff(data1[key], data2[key])
        }
    if data1[key] == data2[key]:
        return {"status": "unchanged", "value": data1[key]}
    return {
        "status": "modified",
        "old_value": data1[key],
        "new_value": data2[key]
    }


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    return {key: get_diff_entry(key, data1, data2) for key in keys}


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    diff = build_diff(data1, data2)

    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return format_plain(diff)
    elif format_name == "json":
        return format_json(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
