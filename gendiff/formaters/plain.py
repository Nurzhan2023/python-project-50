def format_plain(diff, path=""):
    lines = []

    for key, value in diff.items():
        property_path = f"{path}.{key}" if path else key
        status = value["status"]

        if status == "added":
            formatted_value = format_value(value["value"])
            lines.append(f"Property '{property_path}'"
                         f"was added with value: {formatted_value}")
        elif status == "removed":
            lines.append(f"Property '{property_path}' was removed")
        elif status == "modified":
            old_value = format_value(value["old_value"])
            new_value = format_value(value["new_value"])
            lines.append(f"Property '{property_path}'"
                         f" was updated. From {old_value} to {new_value}")
        elif status == "nested":
            lines.append(format_plain(value["children"], property_path))

    return "\n".join(lines)


def format_value(value):
    """Форматирует значение для plain-вывода."""
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
