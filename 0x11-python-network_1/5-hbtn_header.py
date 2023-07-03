#!/usr/bin/python3
"""Displays the X-Request-Id header variable of
    request in header response
"""
import sys
import requests


def main():
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
