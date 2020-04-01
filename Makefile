.PHONY: develop test comply format docs clean dist

help:
	@echo "usage: make <rule>"
	@echo
	@echo "Spiral Makefile containing useful rules for developers."
	@echo
	@echo "rules:"
	@echo "  develop        install development version"
	@echo "  test           run the full test suite"
	@echo "  docs           build documentation"
	@echo "  themes         build themes"
	@echo "  clean          clean the package"
	@echo "  dist           build distribution"

develop:
	python3 -m venv .venv --without-pip
	curl -s -N https://bootstrap.pypa.io/get-pip.py | .venv/bin/python3
	.venv/bin/pip3 install -r requirements-dev.txt
	.venv/bin/pip3 install -e .
	.venv/bin/pre-commit install
	@echo
	@echo "Setup complete. Now run: source .venv/bin/activate"
	@echo

test:
	python3 -m pytest -v --cov=spiral --cov-report=term --cov-report=html:coverage tests/

docs:
	python3 setup.py build_sphinx
	@echo
	@echo DOC: "file://"$$(echo `pwd`/docs/build/html/index.html)
	@echo

themes:
	python3 -m scripts.plotly_theme_builder

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

	rm -f .coverage
	rm -rf coverage*/
	rm -rf .pytest_cache
	rm -rf build/
	rm -rf dist/
	rm -rf docs/build/

dist: clean
	python3 setup.py clean
	python3 setup.py sdist bdist_wheel
