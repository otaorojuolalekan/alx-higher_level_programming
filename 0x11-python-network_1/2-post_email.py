#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
import urllib.parse as ulp
import urllib.request as ulb


def main():
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = ulp.urlencode(value).encode("ascii")

    request = ulb.Request(url, data)
    with ulb.urlopen(request) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()
