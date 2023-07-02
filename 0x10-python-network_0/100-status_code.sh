#!/bin/bash
# print status code only
curl -sL -o /dev/null -w "%{response_code}" "$1"
