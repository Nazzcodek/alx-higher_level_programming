#!/bin/bash
# Bash script for http status code
curl -s -w "%{http_code}" -o /dev/null "$1"
