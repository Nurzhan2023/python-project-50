from gendiff.read import read_file


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
                "children": build_diff(
                    data1[key],
                    data2[key])}
        elif data1[key] == data2[key]:
            diff[key] = {"status": "unchanged", "value": data1[key]}
        else:
            diff[key] = {
                "status": "modified",
                "old_value": data1[key],
                "new_value": data2[key]}

    return diff


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    diff = build_diff(data1, data2)

    if format_name == "stylish":
        from gendiff.formaters.stylish import format_stylish
        return format_stylish(diff)

    raise ValueError(f"Unsupported format: {format_name}")
