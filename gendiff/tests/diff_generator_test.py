import pytest
from gendiff.diff_generator import generate_diff


def normalize_indentation(text):
    return "\n".join(line.strip() for line in text.strip().splitlines())


@pytest.mark.parametrize("file1, file2, expected_result", [
    ("gendiff/tests/file1.json", "gendiff/tests/file2.json", """{
      - follow: False
        host: hexlet.io
      - proxy: 123.124.53.22
      - timeout: 50
      + timeout: 20
      + verbose: True
    }"""),
    ("gendiff/tests/file1.yaml", "gendiff/tests/file2.yaml", """{
      - follow: False
        host: hexlet.io
      - proxy: 123.124.53.22
      - timeout: 50
      + timeout: 20
      + verbose: True
    }"""),
])
def test_generate_diff(file1, file2, expected_result):
    actual_result = generate_diff(file1, file2)

    normalized_expected = normalize_indentation(expected_result)
    normalized_actual = normalize_indentation(actual_result)

    assert normalized_actual == normalized_expected
