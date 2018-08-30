#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    try:
        url = 'https://www.reddit.com/r/{}/hot/.json'.format(
            subreddit)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/39.0.2171.95 Safari/537.36',
            'accept': 'application/json'}
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False).json()
        list = response['data']['children']
        for val in list:
            print(val['data']['title'])
    except BaseException:
        print(None)
