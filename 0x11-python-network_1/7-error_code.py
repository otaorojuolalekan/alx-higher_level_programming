#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the body of the response.
"""
import sys
import requests


def main():
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)


if __name__ == "__main__":
    main()
