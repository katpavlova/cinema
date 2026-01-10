.PHONY: build clean publish

PYPI_REPOSITORY_URL := https://nexus-dev.cinema.me/repository/pypi-private/

build:
	python3 -m build --wheel --outdir dist


publish:
	poetry run python3 -m twine upload --repository-url $(PYPI_REPOSITORY_URL) dist/*