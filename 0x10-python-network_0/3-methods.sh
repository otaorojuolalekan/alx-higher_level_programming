#!/bin/bash
# send options request
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
