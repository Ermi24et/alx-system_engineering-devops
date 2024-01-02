#!/usr/bin/python3
"""
a script that exports data in the CSV format
"""
import csv
import requests
import sys


if __name__ == '__main__':
    api = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(api + 'users/{}'.format(sys.argv[1])).json()
    todo = requests.get(api + 'users/{}/todos'.format(sys.argv[1])).json()
    rows = [
        [
            sys.argv[1],
            user['username'],
            task.get('completed'),
            task.get('title')
        ] for task in todo
    ]
    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)
