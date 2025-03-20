# gendiff/read.py
import json
import yaml
import os


def read_file(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Ошибка: файл не найден: {file_path}")

    extension = os.path.splitext(file_path)[1].lower()

    parsers = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }

    if extension not in parsers:
        raise ValueError(f"Ошибка: неподдерживаемый формат файла {extension}")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return parsers[extension](file) or {}
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка в JSON-файле {file_path}: {e}")
    except yaml.YAMLError as e:
        raise ValueError(f"Ошибка в YAML-файле {file_path}: {e}")
