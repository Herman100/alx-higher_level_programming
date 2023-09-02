#!/usr/bin/python3
"""
This module takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


def search_user(url, q):
    """
    Takes in a URL and a letter, sends a POST request to
    the passed URL with the letter as a parameter,
    and finally displays the body of the response.
    """
    data = {'q': q}
    response = requests.post(url, data=data)
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                  json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    search_user(url, q)
