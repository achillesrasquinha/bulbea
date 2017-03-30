# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import argparse

# imports - module imports
from bulbea import AppConfig
from bulbea._util import _get_version_str
from bulbea._util.color import Color

import bulbea as bb

def create_main_parser():
    _logo        = Color.to_color_string(AppConfig.LOGO, AppConfig.COLOR_PRIMARY)
    _version     = _get_version_str()
    _description = '{logo} v{version}'.format(logo = _logo, version = _version)

    parser       = argparse.ArgumentParser(description     = _description,
                                           formatter_class = argparse.RawDescriptionHelpFormatter)
    parser.add_argument('SOURCE',
                        help    = 'source symbol for economic data')
    parser.add_argument('TICKER',
                        help    = 'ticker symbol of a company')
    parser.add_argument('-v', '--version',
                        action  = 'version',
                        version = 'v{version}'.format(version = _version),
                        help    = 'show the version information and exit')

    return parser

def main(args = None):
    parser = create_main_parser()
    args   = parser.parse_args()

    source = args.SOURCE
    ticker = args.TICKER

    share  = bb.Share(source, ticker)
