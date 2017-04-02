# imports - compatibility imports
from __future__ import absolute_import

# imports - module imports
from bulbea._util.const import SHARE_ACCEPTED_FILE_FORMATS

TYPE_ERROR_STRING             = 'Expected {expected_type_name}, got {recieved_type_name} instead.'
VALUE_ERROR_SHARE_FILE_FORMAT = 'Unknown format {format_}. Accepted format are %s.' % (str(SHARE_ACCEPTED_FILE_FORMATS))
