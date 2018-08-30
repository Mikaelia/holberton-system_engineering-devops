#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""
import requests
import json


def recurse(subreddit, after='', hot_list=[]):

    try:
        url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/39.0.2171.95 Safari/537.36',
            'accept': 'application/json',
        }
        payload = {'after': after}

        response = requests.get(url, headers=headers, params=payload,
                                allow_redirects=False).json()

        posts = response['data']['children']
        for item in posts:
            hot_list.append(item['data']['title'])

        after = response['data']['after']
        if after is None:
            return hot_list

        return recurse(subreddit, after, hot_list)

    except BaseException:
        return None
