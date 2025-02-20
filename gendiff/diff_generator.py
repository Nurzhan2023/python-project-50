from gendiff.read import read_file


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
