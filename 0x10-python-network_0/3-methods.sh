#!/bin/bash
# send options request
curl -sI "$1" | grep "Allow: " | awk -F ': ' '{print $2}
