#!/bin/bash
# send options request
curl -sX OPTIONS "$1" | grep "Allow: " | awk -F ': ' '{print $2}
