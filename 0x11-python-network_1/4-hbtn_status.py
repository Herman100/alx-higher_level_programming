#!/usr/bin/python3
"""
This module fetches the contents of https://alx-intranet.hbtn.io/status
using the requests package and displays the response in a specified format.
"""
import requests


def fetch_status():
    """
    Fetches the contents of https://alx-intranet.hbtn.io/status using the
    requests package and displays the response in a specified format.
    """
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    fetch_status()
