# gendiff/scripts/read.py

import json
import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)