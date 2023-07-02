#!/bin/bash
# send options request
curl -sI "$1" | grep -i "Allow" | cut -d " " -f 2-
