#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts listed
"""
import requests


def top_ten(subreddit):
    try:
        res = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                           format(subreddit),
                           headers={'User-Agent': 'custom'},
                           allow_redirects=False)
        res_json = res.json()
        for item in res_json['data']['children']:
            print(item['data']['title'])
    except:
        print('None')
