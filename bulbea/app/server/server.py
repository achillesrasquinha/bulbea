# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
try:
	from urlparse import urljoin
except ImportError:
	from urllib.parse import urljoin

# imports - third-party imports
from flask import Flask, render_template

# imports - module imports
from bulbea.app.config import ServerConfig

app = Flask(__name__,
	static_folder   = ServerConfig.Path.ABSPATH_ASSETS,
	template_folder = ServerConfig.Path.ABSPATH_TEMPLATES
)

@app.route(ServerConfig.URL.BASE)
@app.route(urljoin(ServerConfig.URL.BASE, 'index'))
def index(title = 'Home', navbar = True):
	template = render_template('pages/index.html', title = title, has_navbar = navbar)

	return template

@app.route(ServerConfig.URL.SIGNIN)
def signin(title = 'Sign In', navbar = False):
	template = render_template('pages/signin.html', title = title, has_navbar = navbar)

	return template