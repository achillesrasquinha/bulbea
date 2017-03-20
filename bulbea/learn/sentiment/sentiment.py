# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
import textblob

# imports - module imports
from bulbea.learn.sentiment.twitter import Twitter

def sentiment(share):
    twitter = Twitter()
