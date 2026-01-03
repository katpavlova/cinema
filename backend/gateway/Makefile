.PHONY: check format

check:
	poetry run ruff check cinema_api_gateway
	poetry run mypy cinema_api_gateway

format:
	poetry run ruff format cinema_api_gateway
	poetry run ruff check cinema_api_gateway --fix
	poetry run mypy cinema_api_gateway
