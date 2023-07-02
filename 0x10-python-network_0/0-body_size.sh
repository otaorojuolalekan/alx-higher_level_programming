#!/usr/bin/env bash
# print body size if response code is 200

# map url to input
url=$1
# get response code
response=$(curl -s -o /dev/null -w %{response_code} "$url")
# get body size
body_size=$(curl -s -o /dev/null -w %{size_download} $url)

# print body_size if response is 200
if [ $response -eq 200 ];
then
    echo "$body_size";
fi
