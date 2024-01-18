#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all hot
articles, prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, dict_count={}, after=None):
    """ prints counts of given keywords """
    params = {"limit": 50}
    if after:
        params["after"] = after
    res = requests.get("https://www.reddit.com/r/{}/hot.json".
                       format(subreddit),
                       headers={'User-Agent': 'custom'},
                       params=params,
                       allow_redirects=False)
    if res.status_code == 200:
        res_json = res.json().get('data').get('children')
        for item in res_json:
            title = item.get('data').get('title')
            word_list = [word.lower() for word in word_list]
            for word in word_list:
                count_word = title.split().count(word)
                if dict_count.get(word):
                    dict_count[word] += count_word
                else:
                    dict_count[word] = count_word
        if res.json().get('data').get('after'):
            count_words(subreddit,
                        word_list=word_list,
                        dict_count=dict_count,
                        after=res.json().get('data').get('after'))
        else:
            for pair in sorted(dict_count.items(),
                               key=lambda kv: (kv[1], kv[0]),
                               reverse=True):
                if pair[1]:
                    print('{}: {}'.format(pair[0].strip(), pair[1]))

