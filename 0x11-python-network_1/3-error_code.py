#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""


def main():
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)


if __name__ == "__main__":
    main()
