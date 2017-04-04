.PHONY: docs

PYTHON = python

install:
	cat requirements/*.txt > requirements.txt
	pip install -r requirements.txt

	pip install tensorflow

	$(PYTHON) setup.py install

clean:
	$(PYTHON) setup.py clean

docs:
	cd docs && make html

tests:
	$(PYTHON) setup.py test

app:
	$(PYTHON) -m bulbea.app

all:
	make install docs tests clean
