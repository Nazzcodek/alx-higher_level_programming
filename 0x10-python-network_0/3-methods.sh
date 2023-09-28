#!/bin/bash
# Bash script to display all the HTTP methods
curl -sX OPTIONS "$1" | tr '\n' ','
