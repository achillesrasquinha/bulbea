# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import argparse

# imports - module imports
from bulbea.config      import AppConfig
from bulbea._util       import _get_version_str
from bulbea._util.color import Color

class BaseParser(object):
    def __init__(self):
        self._build_parser()

    def _build_parser(self):
        logo        = Color.to_color_string(AppConfig.LOGO, AppConfig.COLOR_PRIMARY)
        version     = _get_version_str()
        description = '{logo} v{version}'.format(logo = logo, version = version)

        self.parser = argparse.ArgumentParser(description     = description,
                                              formatter_class = argparse.RawDescriptionHelpFormatter)
