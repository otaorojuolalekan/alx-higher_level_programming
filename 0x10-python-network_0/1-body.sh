#!/bin/bash
# print body if response code is 200
curl -sI "$1" | grep "Content-Length" | awk '{print $2}'
