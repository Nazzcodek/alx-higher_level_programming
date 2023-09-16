#!/usr/bin/python3
# a script that lists all states with a name starting with N
# script should take 3 arguments: mysql username, mysql password database name

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    states = (cursor.fetchall())
    for state in states:
        if state[1][0] == "N":
            print(state)
