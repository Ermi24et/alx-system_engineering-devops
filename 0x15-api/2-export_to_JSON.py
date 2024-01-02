#!/usr/bin/python3
"""
a script that exports data in the CSV format
"""
import json
import requests
import sys


if __name__ == '__main__':
    api = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(api + 'users/{}'.format(sys.argv[1])).json()
    todo = requests.get(api + 'users/{}/todos'.format(sys.argv[1])).json()
    rows = {
        sys.argv[1]:
        [
            {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user['username']
            } for task in todo
        ]
    }
    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        json.dump(rows, f)
