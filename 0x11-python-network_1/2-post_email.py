#!/usr/bin/python3
"""
python script that fetches URLs request
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as request:
        body = request.read().decode('utf-8')
        print(body)
