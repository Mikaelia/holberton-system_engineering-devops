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

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quoting=csv.QUOTE_ALL, quotechar='"')
        for task in tasks:
            writer.writerow([user_id, username, task.get(
                'completed'), task.get('title')])
