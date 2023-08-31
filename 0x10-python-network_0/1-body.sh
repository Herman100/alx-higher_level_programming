#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL -w "%{http_code}" "$1" -o /tmp/output | grep -q "200" && cat /tmp/output
