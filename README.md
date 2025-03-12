### Hexlet tests and linter status:
[![Maintainability](https://api.codeclimate.com/v1/badges/b23c691de6b894bf85ac/maintainability)](https://codeclimate.com/github/Nurzhan2023/python-project-50/maintainability)

[![Actions Status](https://github.com/Nurzhan2023/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Nurzhan2023/python-project-50/actions)


[![Python CI](https://github.com/Nurzhan2023/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Nurzhan2023/python-project-50/actions/workflows/python-ci.yml)

[![Test Coverage](https://api.codeclimate.com/v1/badges/b23c691de6b894bf85ac/test_coverage)](https://codeclimate.com/github/Nurzhan2023/python-project-50/test_coverage)

## Description

Gendiff is a command line utility for comparing two configuration files. The tool analyzes the files and the differences in a human-readable format.

## Utility features:
- Supports different input formats: yaml, json
- Generating a report in the form of plain text, stylish and json

## Installation

To install, clone the ropository and install using uv:

```bash
git clone https://github.com/Nurzhan2023/python-project-50.git
cd python-project-50
make install
```

## Usage
To display usage information:

```bash
uv run gendiff -h
```

Command Line Options

```bash
- h, --help - display this help message and exit
- f FORMAT, --format FORMAT - set the output format(supported fotmats: plain, json, stylish)
```

Example of comparing two files:
 
```bash
gendiff gendiff/tests/file1.json gendiff/tests/file2.json
```

The output will appear in the following format:

```bash
{
 - follow: False
   host: hexlet.io
 - proxy: 123.124.53.22
 - timeout: 50
 + timeout: 20
 + verbose: True
}
```

## Development

TESTS
To run test, use the following command:
```bash
make test-coverage
```

LINTER
To check the code with the linter, execute:

```bash
make lint
```

## CI/CD

The project uses GitHub Actions for automated testing and linting. You can see status of the last commit at the top of this README

[![asciicast](https://asciinema.org/a/Pe196IZV1YWZEZojjxIbKHeU8.svg)](https://asciinema.org/a/Pe196IZV1YWZEZojjxIbKHeU8)

[![asciicast](https://asciinema.org/a/Hc7xhdtxCYwpHkDT0RCYTOhJ9.svg)](https://asciinema.org/a/Hc7xhdtxCYwpHkDT0RCYTOhJ9)