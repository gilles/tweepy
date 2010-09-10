# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

class TweepError(Exception):
    """Tweepy exception"""

    def __init__(self, reason, response=None):
        self.reason = str(reason)
        self.response = response

    def __str__(self):
        return self.reason

class CachedRateLimit(TweepError):
    """Still in rate limit exception"""
    def __init__(self, reason):
        super(CachedRateLimit, self).__init__(reason)
