#!/bin/bash

# Make a request to 0.0.0.0:5000/catch_me and send the required data
curl -s -X PUT -d "user_id=98" -L 0.0.0.0:5000/catch_me
