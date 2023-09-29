#!/usr/bin/python3
"""
python script that fetches URLs response
"""

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(f"Body response:\n"
              f"\t- type: {type(html)}\n"
              f"\t- content: {repr(html)}\n"
              f"\t- utf8 content: {html.decode('utf-8')}")
