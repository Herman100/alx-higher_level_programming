#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL, and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request


def fetch_x_request_id(url):
    """
    Takes in a URL, sends a request to the URL, and displays the value of the
    X-Request-Id variable found in the header of the response.
    """
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
