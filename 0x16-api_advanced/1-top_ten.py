#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    try:
        url = 'https://api.reddit.com/r/{}/hot'.format(
            subreddit)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers,
                                allow_redirects=False).json()

        data = response['data']['children']
        for i, value in enumerate(data):
            if i < 10:
                    print(value['data']['title'])
    except BaseException:
        print(None)
