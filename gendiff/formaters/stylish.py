# gendiff/formaters/stylish.py
def format_value(value, depth):
    indent = " " * (depth * 4)

    if isinstance(value, dict):
        formatted = ["{"]
        for k, v in value.items():
            formatted.append(f"{indent}    {k}: {format_value(v, depth + 1)}")
        formatted.append(f"{indent}}}")
        return "\n".join(formatted)

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

    for key, info in diff.items():
        status = info["status"]

        if status == "nested":
            children = format_stylish(info["children"], depth + 1)
            lines.append(f"{indent}    {key}: {children}")
        elif status == "added":
            lines.append(
                f"{indent}  + {key}: {format_value(info['value'], depth + 1)}"
            )
        elif status == "removed":
            lines.append(
                f"{indent}  - {key}: {format_value(info['value'], depth + 1)}"
            )
        elif status == "modified":
            lines.append(
                f"{indent}  - {key}:"
                f"{format_value(info['old_value'], depth + 1)}"
            )
            lines.append(
                f"{indent}  + {key}:"
                f"{format_value(info['new_value'], depth + 1)}"
            )
        else:  # unchanged
            lines.append(
                f"{indent}    {key}: {format_value(info['value'], depth + 1)}"
            )

    lines.append(indent + "}")
    return "\n".join(lines)
