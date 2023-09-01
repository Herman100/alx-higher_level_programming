#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL, and displays the value
of the variable X-Request-Id in the response header.
"""
import sys
import requests


def fetch_x_request_id(url):
    """
    Takes in a URL, sends a request to the URL, and displays the value of the
    variable X-Request-Id in the response header.
    """
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
