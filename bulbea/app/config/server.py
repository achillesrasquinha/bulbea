# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import os

# imports - module imports
from bulbea.app.config import BaseConfig

class ServerConfig(BaseConfig):
	class Path(BaseConfig.Path):
		ABSPATH_TEMPLATES = os.path.join(BaseConfig.Path.ABSPATH_VIEWS, 'templates')

	HOST = '0.0.0.0'
	PORT = int(os.getenv('PORT', 3000))
