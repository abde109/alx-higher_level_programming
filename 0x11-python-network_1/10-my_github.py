#!/usr/bin/python3
"""
Python script to display GitHub ID using GitHub API
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, token))
    try:
        print(r.json().get('id'))
    except ValueError:
        print("None")
