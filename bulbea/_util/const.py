# imports - compatibility imports
from __future__ import absolute_import

# imports - module imports
from bulbea._util.file import File


ABSURL_QUANDL               = 'https://www.quandl.com'
QUANDL_MAX_DAILY_CALLS      = 50000

SHARE_ACCEPTED_FILE_FORMATS = tuple(list(File.Extension.CSV) + list(File.Extension.PICKLE))