#!/usr/bin/python3
"""
python script that fetches URLs request and return error if any
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        request = requests.get(url)
        request.raise_for_status()
        print(request.text)
    except requests.exceptions.RequestException as e:
        print(f"Error code: {e.response.status_code}")
