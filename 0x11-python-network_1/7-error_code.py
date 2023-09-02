#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL, and displays the body
of the response. If the HTTP status code is greater than or equal to 400, the
script prints an error message followed by the value of the HTTP status code.
"""
import sys
import requests


def fetch_url(url):
    """
    Takes in a URL, sends a request to the URL, and displays the body of the
    response. If the HTTP status code is greater than or equal to 400, the
    function prints an error message followed by the value of the HTTP status
    code.
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
