#!/usr/bin/python3
"""
python script that fetches URLs request and return error if any
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as request:
            body = request.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(f"Error code: {e.code}")
