#! /usr/bin/env python
import twitter
import simplejson
import pickle
import sqlite3
from dateutil.parser import parse


consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

from settings import consumer_key, consumer_secret, access_token_key, access_token_secret, database_fn, twitter_username

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)

conn = sqlite3.connect(database_fn)
c = conn.cursor()

count = 40
start_page = 1
end_page = 1

for page in range(start_page, end_page+1):

    statuses = api.GetUserTimeline(twitter_username, count=count, page=page)

    for t in statuses:
        s = t.AsDict()
        del s['user']

        s['created_at'] = parse(s['created_at'])
        tweet = {
            'in_reply_to_status_id': None, 
            'in_reply_to_screen_name': None, 
            'in_reply_to_user_id': None,
            'retweet_count': 0, 
            'favorited': False, 
            'truncated': False,
            'retweeted': False,
            }
        tweet.update(s)
        # print tweet

        c.execute('''
            REPLACE INTO tweets (id, created_at, in_reply_to_screen_name, in_reply_to_status_id, in_reply_to_user_id, text, favorited, truncated, retweeted, retweet_count)
                  VALUES (:id, :created_at, :in_reply_to_screen_name, :in_reply_to_status_id, :in_reply_to_user_id, :text, :favorited, :truncated, :retweeted, :retweet_count)
        ''', tweet)

    conn.commit()
    #     print "%s - %s\n" % (s.created_at, s.text)

    # print "page %s" % page
    # print "tweets on page %s" % len(statuses)

