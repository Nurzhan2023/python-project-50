import pytest
from gendiff.diff_generator import generate_diff
import re

@pytest.mark.parametrize(
    "file1, file2, expected_file",
    [
        ("gendiff/tests/file1.json", "gendiff/tests/file2.json",
         "gendiff/tests/expected_result_json.txt"),
        ("gendiff/tests/file1.yaml", "gendiff/tests/file2.yaml",
         "gendiff/tests/expected_result_yaml.txt")
    ]
)
def test_generate_diff(file1, file2, expected_file):
    actual_result = generate_diff(file1, file2, format_name="stylish").strip()

    with open(expected_file, "r") as f:
        expected_result = f.read().strip()

    # Нормализация пробелов перед сравнением
    def normalize_whitespace(text):
        return re.sub(r'\s+', ' ', text).strip()

    actual_result = normalize_whitespace(actual_result)
    expected_result = normalize_whitespace(expected_result)

    assert actual_result == expected_result, (
        f"\nExpected:\n{expected_result}\n\nGot:\n{actual_result}"
    )
