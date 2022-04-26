#!/usr/bin/python3
"""Module 0-subs
Contains function number_of_subscribers()
"""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers for the subreddit.
    If the subreddit is not found, the function returns 0"""
    r = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={'user-agent': 'Mozilla/5.0' +
                 '(X11; Ubuntu; Linux x86_64; rv:99.0)' +
                 'Gecko/20100101 Firefox/99.0'})

    subs = r.json().get('data').get('subscribers')

    if subs == '' or subs is None:
        return 0
    return subs
