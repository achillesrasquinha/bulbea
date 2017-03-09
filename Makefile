.PHONY: docs

PYTHON = python

install:
	cat requirements/*.txt > requirements.txt
	pip install -r requirements.txt --no-cache-dir

	$(PYTHON) setup.py install

	bash twitter.sh

docs:
	cd docs && make html

test:
	$(PYTHON) setup.py test

clean:
	$(PYTHON) setup.py clean
