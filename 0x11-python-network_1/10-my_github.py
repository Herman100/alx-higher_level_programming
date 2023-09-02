#!/usr/bin/python3
"""
This module takes your GitHub credentials (username and password) and uses the
GitHub API to display your id.
"""
import sys
import requests


def fetch_github_id(username, password):
    """
    Takes your GitHub credentials (username and password) and uses the GitHub
    API to display your id.
    """
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    try:
        print(response.json().get('id'))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    fetch_github_id(username, password)
