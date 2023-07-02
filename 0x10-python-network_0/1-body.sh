#!/bin/bash
# print body size # alt: curl -sfL $url
curl -sL -o /dev/null -w "%{response_code}\n" "$1" | [ $(cat) = "200" ] && curl -sL -X "GET" "$1"
