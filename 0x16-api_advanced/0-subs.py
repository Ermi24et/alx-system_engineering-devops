#!/usr/bin/python3
"""
a queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    try:
        res = requests.get('https://www.reddit.com/r/{}/about.json'.
                           format(subreddit),
                           headers={'User-Agent': 'custom'},
                           allow_redirects=False)
        outp = res.json()
        return outp['data']['subscribers']
    except Exception:
        return 0
