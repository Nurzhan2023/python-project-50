import pytest
import re
from gendiff.diff_generator import generate_diff


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

    # Улучшенная нормализация пробелов
    def normalize_text(text):
        text = re.sub(r'\s*:\s*', ': ', text)  # Ровный пробел перед двоеточием
        text = re.sub(r'\s*{\s*', ' { ', text)  # Ровный пробел перед `{`
        text = re.sub(r'\s+', ' ', text).strip()  # Убираем лишние пробелы
        return text

    actual_result = normalize_text(actual_result)
    expected_result = normalize_text(expected_result)

    assert actual_result == expected_result, (
        f"\nExpected:\n{expected_result}\n\n"
        f"Got:\n{actual_result}"
    )
