#!/usr/bin/python3
"""
This module fetches the contents of https://alx-intranet.hbtn.io/status
using the urllib package and displays the response in a specified format.
"""
import urllib.request


def fetch_status():
    """
    Fetches the contents of https://alx-intranet.hbtn.io/status using the
    urllib package and displays the response in a specified format.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    fetch_status()
