#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    try:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(
            subreddit)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers,
                                allow_redirects=False).json()

        data = response['data']['children']
        for val in data:
            print(val['data']['title'])
    except BaseException:
        print(None)
