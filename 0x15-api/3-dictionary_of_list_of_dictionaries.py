#!/usr/bin/python3
"""
Exports json of all tasks owned by employees
"""
import csv
import json
import requests
import sys


if __name__ == '__main__':

    users = requests.get('https://jsonplaceholder.typicode.com/users')
    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    tasks = response.json()
    user_list = users.json()

    with open("todo_all_employees.json", 'w') as outfile:
        task_list = []
        full_dict = {}

        for user in user_list:
            username = user.get('username')
            user_id = user.get('id')
            for task in tasks:
                if task.get('userId') == user_id:
                    task_dict = {
                        "task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": username
                    }
            task_list.append(task_dict)
            full_dict.update({user_id: task_list})
        json.dump(full_dict, outfile)
