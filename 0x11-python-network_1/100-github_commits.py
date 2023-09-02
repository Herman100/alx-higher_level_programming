#!/usr/bin/python3
"""
This module takes in a repository name and owner name as arguments, and uses
the GitHub API to display the most recent commits to the specified repository
"""
import sys
import requests


def fetch_commits(repo, owner):
    """
    Takes in a repository name and owner name arguments, and uses the GitHub
    API to display the 10 most recent commits to the specified repository.
    """
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author_name))


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    fetch_commits(repo, owner)
