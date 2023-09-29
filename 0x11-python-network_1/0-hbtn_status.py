#!/usr/bin/python3
"""
python script that fetches URLs response
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    html = response.read()
    print(f"Body response:\n"
          f"    - type: {type(html)}\n"
          f"    - content: {repr(html)}\n"
          f"    - utf8 content: {html.decode('utf-8')}")
