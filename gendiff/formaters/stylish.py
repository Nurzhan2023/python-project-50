def format_value(value, depth):
    indent = " " * (depth * 4)

    if isinstance(value, dict):
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {format_value(v, depth + 1)}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)

    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"

    return str(value)


def format_stylish(diff, depth=0):
    indent = " " * (depth * 4)
    lines = ["{"]

    for key, info in sorted(diff.items()):
        status = info.get("status")

        if status == "nested":
            children = format_stylish(info.get("children", {}), depth + 1)
            lines.append(f"{indent}    {key}: {children}")
        elif status == "added":
            value = format_value(info.get("value"), depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif status == "removed":
            value = format_value(info.get("value"), depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif status == "modified":
            old_value = format_value(info.get("old_value"), depth + 1)
            new_value = format_value(info.get("new_value"), depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        else:  # unchanged
            value = format_value(info.get("value"), depth + 1)
            lines.append(f"{indent}    {key}: {value}")

    lines.append(f"{indent}}}")
    return "\n".join(lines)
