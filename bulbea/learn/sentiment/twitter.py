# imports - compatibility packages
from __future__ import absolute_import

# imports - third-party packages
import tweepy

# module imports
from bulbea import AppConfig
from bulbea._util import _validate_environment_variable

class Twitter(object):
    def __init__(self):
        api_key                  = AppConfig.ENVIRONMENT_VARIABLE['twitter_api_key']
        api_secret               = AppConfig.ENVIRONMENT_VARIABLE['twitter_api_secret']
        access_token             = AppConfig.ENVIRONMENT_VARIABLE['twitter_access_token']
        access_token_secret      = AppConfig.ENVIRONMENT_VARIABLE['twitter_access_token_secret']

        _validate_environment_variable(api_key, raise_err = True)
        _validate_environment_variable(api_secret, raise_err = True)
        _validate_environment_variable(access_token, raise_err = True)
        _validate_environment_variable(access_token_secret, raise_err = True)

        self.api_key             = api_key
        self.api_secret          = api_secret
        self.access_token        = access_token
        self.access_token_secret = access_token_secret

        self.auth_handler        = tweepy.OAuthHandler(self.api_key, self.api_secret)
        self.auth_handler.set_access_token(self.access_token, self.access_token_secret)

        self.api                 = tweepy.API(self.auth_handler)
