# imports - compatibility packages
from __future__ import absolute_import

# imports - third-party packages
import tweepy

# module imports
from bulbea import AppConfig
from bulbea._util import _check_environment_variable_set

class Twitter(object):
    def __init__(self):
        api_key                  = AppConfig.ENVIRONMENT_VARIABLE['twitter_api_key']
        api_secret               = AppConfig.ENVIRONMENT_VARIABLE['twitter_api_secret']
        access_token             = AppConfig.ENVIRONMENT_VARIABLE['twitter_access_token']
        access_token_secret      = AppConfig.ENVIRONMENT_VARIABLE['twitter_access_token_secret']

        _check_environment_variable_set(api_key, raise_err = True)
        _check_environment_variable_set(api_secret, raise_err = True)
        _check_environment_variable_set(access_token, raise_err = True)
        _check_environment_variable_set(access_token_secret, raise_err = True)

        self.api_key             = api_key
        self.api_secret          = api_secret
        self.access_token        = access_token
        self.access_token_secret = access_token_secret

        self.auth_handler        = tweepy.OAuthHandler(self.api_key, self.api_secret)
        self.auth_handler.set_access_token(self.access_token, self.access_token_secret)

        self.api                 = tweepy.API(self.auth_handler)
