# imports - compatibility packages
from __future__ import absolute_import

# imports - third-party packages
from flask import Flask

# module imports
from bulbea.app.config import ServerConfig

app = Flask(__name__)

@app.route(ServerConfig.URL.BASE)
def index():
    pass
