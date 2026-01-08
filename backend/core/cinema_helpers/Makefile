.PHONY: build clean publish

build:
	python3 -m build --wheel --outdir dist

clean:
	rm -rf dist *.egg-info


publish: build
	python3 -m twine upload --repository pypi-private dist/*