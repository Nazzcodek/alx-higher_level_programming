#!/usr/bin/python3
"""
python script that fetches URLs response using requests
"""

import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    request = requests.get(url)
    print(f"Body response:\n"
          f"\t- type: {type(request.text)}\n"
          f"\t- content: {request.text}")
