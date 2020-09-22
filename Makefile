all: install

black:
	black -l 90 lib/fdiff/*.py

clean:
	- rm dist/*.whl dist/*.tar.gz dist/*.zip

dist-build: clean
	python3 setup.py sdist bdist_wheel

dist-push:
	twine upload dist/*.whl dist/*.tar.gz

install:
	pip3 install --ignore-installed -r requirements.txt .

install-dev:
	pip3 install --ignore-installed -r requirements.txt -e ".[dev]"

install-user:
	pip3 install --ignore-installed --user .

test: test-lint test-type-check test-unit

test-coverage:
	coverage run --source fdiff -m py.test
	coverage report -m
#	coverage html

test-lint:
	flake8 --ignore=W50 lib/fdiff

test-type-check:
	mypy lib/fdiff

test-unit:
	tox

uninstall:
	pip3 uninstall --yes fdiff

.PHONY: all black clean dist-build dist-push install install-dev install-user test test-lint test-type-check test-unit uninstall