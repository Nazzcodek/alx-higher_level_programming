#!/usr/bin/python3
"""
a script that lists all states cities from the database hbtn_0e_0_usa
script should take 3 arguments:
    mysql username,
    mysql password,
    database name
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                    FROM `cities` `c` \
                    INNER JOIN `states` `s` \
                    ON `c`.`state_id` = `s`.`id` \
                    ORDER BY `c`.`state_id`")
    cities = (cursor.fetchall())
    for city in cities:
        print(city)
