# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
try:
	from urlparse import urljoin
except ImportError:
	from urllib.parse import urljoin
import json

# imports - third-party imports
from flask import Flask, render_template, request

# imports - module imports
from bulbea.app.config import ServerConfig
from bulbea.app.server.response import Response

app = Flask(__name__,
	static_folder   = ServerConfig.Path.ABSPATH_ASSETS,
	template_folder = ServerConfig.Path.ABSPATH_TEMPLATES
)

@app.route(ServerConfig.URL.BASE)
@app.route(urljoin(ServerConfig.URL.BASE, 'index'))
def index(title = 'Home', navbar = True):
	template = render_template('pages/index.html', title = title, has_navbar = navbar)

	return template

# <stub>
def _axes_to_base64_string(axes):
	import io
	import base64

	figure = axes.get_figure()
	data   = io.BytesIO()
	figure.savefig(data, format = 'png')
	data.seek(0)

	buffer_ = data.read()
	base64  = base64.b64encode(buffer_)
	string  = base64.decode('utf-8')

	return string
# </stub>

@app.route(ServerConfig.URL.PREDICT, methods = ['POST'])
def predict():
	source   = request.form['source']
	ticker   = request.form['ticker']

	# <stub>
	import bulbea as bb

	share    = bb.Share(source, ticker)
	data     = share.data
	data     = data.reset_index()

	tail     = data.tail(1)

	open_    = tail.iloc[0]['Open']
	high     = tail.iloc[0]['High']
	low      = tail.iloc[0]['Low']

	axes     = share.plot(['Adjusted Close'], figsize = (20, 15))
	base64   = 'data:image/png;base64,' + _axes_to_base64_string(axes)

	data     = \
	{
		"open": open_,
		"high": high,
		 "low": low,
		"plot": base64
	}
	# </stub>

	response = Response()
	response.set_data(data)

	dict_    = response.todict()
	json_    = json.dumps(dict_)

	return json_