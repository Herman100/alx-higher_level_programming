#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL, and displays the body
of the response (decoded in utf-8). The script also handles
urllib.error.HTTPError exceptions and prints the HTTP status code.
"""
import sys
import urllib.request
import urllib.error


def fetch_url(url):
    """
    Takes in a URL, sends a request to the URL, and displays the body of the
    response (decoded in utf-8). The function also handles
    urllib.error.HTTPError exceptions and prints the HTTP status code.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
