import pytest
from gendiff.diff_generator import generate_diff


@pytest.mark.parametrize("file1, file2, expected_file", [
    ("gendiff/tests/file1.json", "gendiff/tests/file2.json", "gendiff/tests/expected_result_json.txt"),
    ("gendiff/tests/file1.yaml", "gendiff/tests/file2.yaml", "gendiff/tests/expected_result_yaml.txt")
])
def test_generate_diff(file1, file2, expected_file):
    actual_result = generate_diff(file1, file2, format_name="stylish")

    # Читаем ожидаемый результат из файла
    with open(expected_file, "r") as f:
        expected_result = f.read()

    # Сравниваем результаты, игнорируя лишние пробелы и переносы строк
    assert " ".join(actual_result.split()) == " ".join(expected_result.split())
