#!/usr/bin/python3
"""
Python script to send a POST request and display the JSON response
"""
import requests
import sys

if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        jr = r.json()
        if jr:
            print("[{}] {}".format(jr.get('id'), jr.get('name')))

        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
