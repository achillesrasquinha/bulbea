# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import argparse

# imports - module imports
from bulbea.cli.parser import BaseParser

class AppParser(BaseParser):
    def __init__(self):
        self.super = super(AppParser, self)
        self.super.__init__()
