install:
		uv sync

build:
		uv build
	
lint:
		uv run flake8 gendiff

test-coverage:
		uv run pytest --cov=gendiff --cov-report xml