#!/bin/bash
# Sends a JSON POST request to a URL as argument and displays response
curl -s -H "Content-Type: application/json" -d "@$2" "$1"
