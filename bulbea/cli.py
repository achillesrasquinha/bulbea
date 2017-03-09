from __future__ import absolute_import

import argparse

from bulbea import AppConfig
from bulbea._util.color import Color

import bulbea as bb

_description = '{logo} v{version}'.format(logo = Color.to_color_string(AppConfig.LOGO, AppConfig.COLOR_PRIMARY), version = '.'.join(map(str, AppConfig.VERSION)))
parser       = argparse.ArgumentParser(description     = _description,
                                       formatter_class = argparse.RawDescriptionHelpFormatter)
parser.add_argument('SOURCE',
                    help    = 'source code for economic data')
parser.add_argument('SYMBOL',
                    help    = 'ticker symbol of a company')
parser.add_argument('-a', '--alias',
                    help    = 'alias name for a company (e.g. APPL - Apple)')
parser.add_argument('-v', '--version',
                    action  = 'version',
                    version = 'v{version}'.format(version = '.'.join(map(str, AppConfig.VERSION))),
                    help    = 'show the version information and exit')

def main():
    args   = parser.parse_args()
    source = args.SOURCE
    symbol = args.SYMBOL
    alias  = args.alias

    share  = bb.Share(source, symbol, alias = alias)
