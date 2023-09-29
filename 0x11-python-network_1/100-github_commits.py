#!/usr/bin/python3
"""
Python script to get my github credential
"""

import requests
import sys


if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    try:
        request = requests.get(url)
        commits = request.json()
        for i in range(10):
            sha = commits[i].get('sha')
            author = commits[i].get('commit').get('author').get('name')
            print(f"{sha}, {author}")
    except Exception as e:
        pass
