from __future__ import absolute_import

import textblob

from bulbea.learn.sentiment import twitter

def sentiment(share, *args, **kwargs):
    search = share.alias
    tweets = twitter.API.search(search, *args, **kwargs)
    score  = 0

    for tweet in tweets:
        blob   = textblob.TextBlob(tweet.text)
        score += blob.sentiment.polarity

    return (score / len(tweets))
