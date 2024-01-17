#!/usr/bin/python3
"""
queries the reddit api and returns a list containing the titles of all hot
articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    try:
        res = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                           format(subreddit, after),
                           headers={'User-Agent': 'custom'},
                           allow_redirects=False)
        if after is None:
            return hot_list
        res_json = res.json()
        for item in res_json.get('data').get('children'):
            hot_list += [item.get('data').get('title')]
        after = res_json['data']['after']
        recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
