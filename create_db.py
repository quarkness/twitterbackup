#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

c.execute('''create table tweets (
    id INTEGER PRIMARY KEY,
    created_at TIMESTAMP,
    text TEXT,
    in_reply_to_screen_name TEXT,
    in_reply_to_status_id INTEGER,
    in_reply_to_user_id INTEGER,
    retweet_count INTEGER,
    retweeted BOOLEAN,
    favorited BOOLEAN,
    truncated BOOLEAN,
    source TEXT
    )
''')

conn.commit()
c.close()
