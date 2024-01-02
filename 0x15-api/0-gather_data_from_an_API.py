#!/usr/bin/python3
"""
a script that using some REST API for a given employee ID returns information
about his/her TODO list progress
"""
import sys
import requests


if __name__ == '__main__':
    api = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(api + 'users/{}'.format(sys.argv[1])).json()
    todo = requests.get(api + 'users/{}/todos'.format(sys.argv[1])).json()
    tasks = [task.get('title') for task in todo if task.get('completed')]

    print('Employee {} is done with tasks({}/{}):'
          .format(user['name'], len(tasks), len(todo)))
    [print('\t {}'.format(task)) for task in tasks]
