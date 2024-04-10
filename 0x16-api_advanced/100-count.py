#!/usr/bin/python3
"""
 a recursive function that queries the Reddit API, parses the title of
 all hot articles, and prints a sorted count of given
 keywords (case-insensitive, delimited by spaces
"""
import re
import requests


def add_title(dictionary, ,hot_posts):
    """ A func that adds items into a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for words in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(words):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ this queries the Reddit API """
    usr_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': usr_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)

def count_words(subreddit, word_list, dictionary=None):
    """ Init function """
    if dictionary is None:
        dictionary = {}

    for word in word_list:
        word = word.lower()
        if word not in dictionary:
            dictionary[word] = 0

    recurse(subreddit, dictionary)

    sorted_items = sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0]))
    for item in sorted_items:
        if item[1] > 0:
            print("{}: {}".format(item[0], item[1]))
