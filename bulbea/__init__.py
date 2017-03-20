# imports - compatibility imports
from __future__ import absolute_import

# module imports
from bulbea.entity import Share
from bulbea.config import AppConfig
from bulbea.app import app
from bulbea.learn import sentiment
from bulbea._util import _get_version_str

__version__ = _get_version_str(AppConfig.VERSION)