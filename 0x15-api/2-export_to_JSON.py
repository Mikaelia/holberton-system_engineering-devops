#!/usr/bin/python3
"""
Exports data to csv file
"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]

    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={'id': user_id})
    response = requests.get('https://jsonplaceholder.typicode.com/todos',
                            params={'userId': user_id})

    tasks = response.json()
    username = user.json()[0].get('username')

    with open("{}.json".format(user_id), 'w') as outfile:
        task_list = []
        for task in tasks:
            task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            task_list.append(task_dict)
        data = {user_id: task_list}
        json.dump(data, outfile)
