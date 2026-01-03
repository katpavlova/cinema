.PHONY: check format

check:
	poetry run ruff check .
	poetry run mypy .

format:
	poetry run ruff format .
	poetry run ruff check . --fix
	poetry run mypy .
