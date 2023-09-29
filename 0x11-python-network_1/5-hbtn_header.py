#!/usr/bin/python3
"""
python script that fetches URLs request using requests
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    request = requests.get(url)
    x_request_id = request.headers['X-Request-Id']
    print(f"{x_request_id}")
