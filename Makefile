.PHONY: docs

PYTHON = python

install:
	cat requirements/*.txt > requirements.txt
	pip install -r requirements.txt

	pip install tensorflow-gpu

	$(PYTHON) setup.py install

	bash twitter.sh

docs:
	cd docs && make html

tests:
	$(PYTHON) setup.py test

clean:
	$(PYTHON) setup.py clean

all:
	make install docs tests clean
