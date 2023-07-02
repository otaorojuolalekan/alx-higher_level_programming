#!/bin/bash
# post JSON file
curl -sLH "Content-Type: application/json" -d @"$2" -X POST "$1"
