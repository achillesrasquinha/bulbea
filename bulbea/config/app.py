from __future__ import absolute_import

from bulbea.config      import BaseConfig
from bulbea._util.color import Color

class AppConfig(BaseConfig):
    NAME                 = 'bulbea'
    VERSION              = (0,1,0)
    LOGO                 = \
"""
888               888 888
888               888 888
888               888 888
88888b.  888  888 888 88888b.   .d88b.   8888b.
888 "88b 888  888 888 888 "88b d8P  Y8b     "88b
888  888 888  888 888 888  888 88888888 .d888888
888 d88P Y88b 888 888 888 d88P Y8b.     888  888
88888P"   "Y88888 888 88888P"   "Y8888  "Y888888"""
    COLOR_PRIMARY        = Color.YELLOW

    WINDOW_ASPECT_RATIO  = 3 / 2
    WINDOW_WIDTH         = 320
    WINDOW_HEIGHT        = int(WINDOW_WIDTH * WINDOW_ASPECT_RATIO)

    PLOT_STYLE           = 'seaborn'

    ENVIRONMENT_VARIABLE = {
        'quandl_api_key': 'BULBEA_QUANDL_API_KEY',
        'twitter_api_key': 'BULBEA_TWITTER_API_KEY',
        'twitter_api_secret': 'BULBEA_TWITTER_API_SECRET',
        'twitter_access_token': 'BULBEA_TWITTER_ACCESS_TOKEN',
        'twitter_access_token_secret': 'BULBEA_TWITTER_ACCESS_TOKEN_SECRET'
    }
