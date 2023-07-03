#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request as ulb


def main():
    url = sys.argv[1]

    request = ulb.Request(url)
    with ulb.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))


if __name__ == "__main__":
    main()
