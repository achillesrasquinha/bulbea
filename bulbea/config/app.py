from __future__ import absolute_import

from bulbea.config      import BaseConfig
from bulbea._util.color import Color

class AppConfig(BaseConfig):
    NAME          = 'bulbea'
    VERSION       = (0,1,0)
    LOGO          = \
"""
888               888 888
888               888 888
888               888 888
88888b.  888  888 888 88888b.   .d88b.   8888b.
888 "88b 888  888 888 888 "88b d8P  Y8b     "88b
888  888 888  888 888 888  888 88888888 .d888888
888 d88P Y88b 888 888 888 d88P Y8b.     888  888
88888P"   "Y88888 888 88888P"   "Y8888  "Y888888"""
    COLOR_PRIMARY = Color.YELLOW

    WINDOW_WIDTH  = 640
    WINDOW_HEIGHT = 480
