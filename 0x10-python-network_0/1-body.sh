#!/usr/bin/bash
# print body size # alt: curl -sfL $url
curl -s -o /dev/null -w "%{response_code}\n" "$1" | [ $(cat) = "200" ] && curl -s -X "GET" "$1"
