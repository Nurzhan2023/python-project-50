# gendiff/formaters/json.py
import json


def format_json(diff):
    return json.dumps(diff, indent=4)
