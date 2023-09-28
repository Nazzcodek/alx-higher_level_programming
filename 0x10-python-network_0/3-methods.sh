#!/bin/bash
# Bash script to display all the HTTP methods
curl -sI "$1" | awk -F ': ' '/^Allow:/ {print $2}'
