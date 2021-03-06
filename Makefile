SHELL=/bin/bash

test: lint install
	coverage run --source=$$(python setup.py --name) -m unittest discover -v

lint:
	./setup.py flake8

version: jsongen/version.py

jsongen/version.py: setup.py
	echo "__version__ = '$$(python setup.py --version)'" > $@

install: clean version
	-rm -rf dist
	python setup.py bdist_wheel
	pip install --upgrade dist/*.whl

clean:
	-rm -rf build dist
	-rm -rf *.egg-info

.PHONY: test lint install clean
