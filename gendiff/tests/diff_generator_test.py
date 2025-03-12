import pytest
from gendiff.diff_generator import generate_diff


@pytest.mark.parametrize("file1, file2, expected_result", [
    ("gendiff/tests/file1.json", "gendiff/tests/file2.json", """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}""")
])
def test_generate_diff(file1, file2, expected_result):
    actual_result = generate_diff(file1, file2, format_name="stylish")
    assert actual_result.strip() == expected_result.strip()
