import pytest
import re
from gendiff.diff_generator import generate_diff


@pytest.mark.parametrize(
    "file1, file2, format_name, expected_file",
    [
        ("gendiff/tests/file1.json", "gendiff/tests/file2.json", "stylish",
         "gendiff/tests/expected_result_stylish.txt"),
        ("gendiff/tests/file1.yaml", "gendiff/tests/file2.yaml", "stylish",
         "gendiff/tests/expected_result_stylish.txt"),
        ("gendiff/tests/file1.yml", "gendiff/tests/file2.yml", "stylish",
         "gendiff/tests/expected_result_stylish.txt"),
        ("gendiff/tests/file1.json", "gendiff/tests/file2.json", "plain",
         "gendiff/tests/expected_result_plain.txt"),
        ("gendiff/tests/file1.yaml", "gendiff/tests/file2.yaml", "plain",
         "gendiff/tests/expected_result_plain.txt"),
        ("gendiff/tests/file1.yml", "gendiff/tests/file2.yml", "plain",
         "gendiff/tests/expected_result_plain.txt"),
        ("gendiff/tests/file1.json", "gendiff/tests/file2.json", "json",
         "gendiff/tests/expected_result_json_format.txt"),
        ("gendiff/tests/file1.yaml", "gendiff/tests/file2.yaml", "json",
         "gendiff/tests/expected_result_json_format.txt"),
        ("gendiff/tests/file1.yml", "gendiff/tests/file2.yml", "json",
         "gendiff/tests/expected_result_json_format.txt"),
    ]

)
def test_generate_diff(file1, file2, format_name, expected_file):
    actual_result = generate_diff(file1, file2, format_name=format_name).strip()

    with open(expected_file, "r") as f:
        expected_result = f.read().strip()

    def normalize_text(text):
        text = re.sub(r'\s*:\s*', ': ', text)
        text = re.sub(r'\s*{\s*', ' { ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    actual_result = normalize_text(actual_result)
    expected_result = normalize_text(expected_result)

    assert actual_result == expected_result, (
        f"\nExpected:\n{expected_result}\n\n"
        f"Got:\n{actual_result}"
    )
