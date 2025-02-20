from gendiff.diff_generator import generate_diff


def normalize_indentation(text):
    return "\n".join(line.strip() for line in text.strip().splitlines())


def test_generate_diff():
    file1 = "gendiff/tests/file1.json"
    file2 = "gendiff/tests/file2.json"

    expected_result = """{
      - follow: False
        host: hexlet.io
      - proxy: 123.124.53.22
      - timeout: 50
      + timeout: 20
      + verbose: True
    }"""

    actual_result = generate_diff(file1, file2)

    normalized_expected = normalize_indentation(expected_result)
    normalized_actual = normalize_indentation(actual_result)

    assert normalized_actual == normalized_expected
