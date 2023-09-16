#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * \
                    FROM `states` \
                    WHERE `name` = '{}' \
                    ORDER BY `id`".format(sys.argv[4]))
    states = (cursor.fetchall())
    for state in states:
        print(state)
