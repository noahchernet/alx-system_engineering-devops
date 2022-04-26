#!/usr/bin/python3
"""Module 1-top_ten
Contains function top_ten(subreddit)
"""
import requests


def top_ten(subreddit):
    """ Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit. Prints None if the subreddit is not
    found."""
    r = requests.get(
        'https://www.reddit.com/r/{}/top.json'.format(subreddit),
        headers={'user-agent': 'Mozilla/5.0' +
                 '(X11; Ubuntu; Linux x86_64; rv:99.0)' +
                 'Gecko/20100101 Firefox/99.0'})
    if r.json().get('data') is None:
        print('None')
        return

    top_posts = r.json().get('data').get('children')

    i = 0
    for post in top_posts:
        i += 1
        print(post.get('data').get('title'))

        if (i == 10):
            return
