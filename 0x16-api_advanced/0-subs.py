#!/usr/bin/python3
"""
a queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    try:
        res = requests.get('https://reddit.com/r/{}/about.json'.
                           format(subreddit),
                           headers={'User-Agent': 'custom'},
                           allow_redirects=False)
        return res.json().get('data').get('subscribers')
    except:
        return 0
