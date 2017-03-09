from __future__ import absolute_import

import quandl

class Share(object):
    def __init__(self, source, symbol, alias = '', *args, **kwargs):
        self.data   = quandl.get('{database}/{code}'.format(database = source, code = symbol), *args, **kwargs)

        self.source = source
        self.symbol = symbol
        self.alias  = alias
