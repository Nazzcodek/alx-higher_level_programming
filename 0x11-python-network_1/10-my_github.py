#!/usr/bin/python3
"""
Python script to get my github credential
"""

import requests
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    pswd = sys.argv[2]
    auth_data = (username, pswd)

    try:
        request = requests.get(url, auth=auth_data)
        if request.status_code == 200:
            user_data = request.json()
            user_id = user_data.get('id')
            print(f"{user_id}")
        else:
            print(None)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
