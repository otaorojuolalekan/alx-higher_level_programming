#!/bin/bash
# Send a POST request with a custom header to the catch_me endpoint
curl -sX POST -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
