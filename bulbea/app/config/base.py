# imports - standard imports
import os
try:
	from urlparse import urljoin
except ImportError:
	from urllib.parse import urljoin

class BaseConfig(object):
	class Path(object):
		ABSPATH_ROOT   = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
		ABSPATH_VIEWS  = os.path.join(ABSPATH_ROOT, 'views')
		ABSPATH_ASSETS = os.path.join(ABSPATH_ROOT, 'assets')

	class URL(object):
		BASE   = '/'
