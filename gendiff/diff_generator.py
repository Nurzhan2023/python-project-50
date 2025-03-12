from gendiff.read import read_file


def format_diff(key, value, status):
    symbols = {'added': '+', 'removed': '-', 'unchanged': ' '}
    return f" {symbols[status]} {key}: {value}"


def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        if key not in data1:
            diff.append(format_diff(key, data2[key], 'added'))
        elif key not in data2:
            diff.append(format_diff(key, data1[key], 'removed'))
        elif data1[key] == data2[key]:
            diff.append(format_diff(key, data1[key], 'unchanged'))
        else:
            diff.append(format_diff(key, data1[key], 'removed'))
            diff.append(format_diff(key, data2[key], 'added'))

    return "{\n" + "\n".join(diff) + "\n}"
