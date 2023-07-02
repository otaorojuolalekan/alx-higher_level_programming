#!/bin/bash
# send options request
curl -sIX OPTIONS "$1" | grep "Allow: " | awk -F ': ' '{print $2}'
