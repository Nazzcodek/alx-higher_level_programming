#!/usr/bin/python3
"""
Python script that sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    try:
        request = requests.post(url, data=data)
        json_data = request.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(f"Error: {e}")
