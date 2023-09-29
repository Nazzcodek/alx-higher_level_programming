#!/usr/bin/python3
"""
python script that fetches URLs request using requests
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    request = requests.post(url, data=data)
    print(request.text)
