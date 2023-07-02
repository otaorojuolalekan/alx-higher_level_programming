#!/bin/bash
# send options request
curl -sI "$1" | grep -i "Allow" | awk -F ': ' '{print $2}'
