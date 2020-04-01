.PHONY: develop test clean dist

develop:
	python3 -m venv env --without-pip
	curl -s -N https://bootstrap.pypa.io/get-pip.py | env/bin/python3
	env/bin/pip3 install -r requirements-dev.txt
	env/bin/pip3 install -e .
	@echo
	@echo "Setup complete. Now run: source env/bin/activate"
	@echo

test:
	python3 -m pytest -v --cov={{ label }} --cov-report=term --cov-report=html:coverage tests/

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

	rm -f .coverage
	rm -rf coverage*/
	rm -rf .pytest_cache
	rm -rf build/
	rm -rf dist/

dist: clean
	env/bin/python3 setup.py clean
	env/bin/python3 setup.py sdist bdist_wheel
