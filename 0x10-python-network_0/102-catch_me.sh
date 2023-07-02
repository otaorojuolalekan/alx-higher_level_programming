#!/bin/bash
# Send a POST request with a custom header to the catch_me endpoint
curl -sX PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
