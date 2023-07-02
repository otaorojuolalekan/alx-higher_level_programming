#!/usr/bin/bash
# print body size if response code is 200
curl -sI "$1" | grep "Content-Length" | awk '{print $2}'
