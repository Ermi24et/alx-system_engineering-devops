#!/usr/bin/python3
"""
a script that exports data in the JSON format
"""
import json
import requests


if __name__ == '__main__':
    api = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(api).json()
    rows = {}
    for user in users:
        todo = requests.get(api + '{}/todos'.format(user['id'])).json()
        rows[user['id']] = [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user['username']
            } for task in todo]

        with open('todo_all_employees.json', 'w') as f:
            json.dump(rows, f)
