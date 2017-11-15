.PHONY: docs

PYTHON 	   ?= python
PYTHON3    ?= python3

BASEDIR     = $(realpath .)
DOCSDIR     = $(BASEDIR)/docs
GITHUBDIR   = $(BASEDIR)/.github
LOGO   	    = $(GITHUBDIR)/logo.png

PIP        ?= pip3
VIRTUALENV ?= virtualenv

venv:
	$(PIP) install virtualenv

	$(VIRTUALENV) .venv/py3 --python $(PYTHON3)

install:
	cat requirements/*.txt > requirements.txt
	pip install -r requirements.txt

	pip install tensorflow-gpu

	$(PYTHON) setup.py install

docs:
	cp $(LOGO) $(DOCSDIR)/_static/img
	cd docs && make html

tests:
	$(PYTHON) setup.py test

clean:
	$(PYTHON) setup.py clean

all:
	make install docs tests clean
