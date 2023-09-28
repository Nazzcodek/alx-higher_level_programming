#!/bin/bash
# Bash script to display all the HTTP methods
curl -s -I "$1" | awk -F ': ' '/^Allow:/ {print $2}'
