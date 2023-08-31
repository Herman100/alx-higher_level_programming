#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL with a header variable, and displays the body
curl -sH "X-School-User-Id: 98" "$1"
