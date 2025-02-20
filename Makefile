install:
		uv sync

build:
		uv build
	
lint:
		uv run flake8 gendiff