#!/usr/bin/python3
"""
script that lists all cities in a state from the database hbtn_0e_0_usa
script should take 4 arguments:
    mysql username,
    mysql password,
    database name,
    state name
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * \
                    FROM `cities` `c` \
                    INNER JOIN `states` `s` \
                    ON `c`.`state_id` = `s`.`id` \
                    ORDER BY `c`.`id`")
    cities = (cursor.fetchall())
    city_name = []
    for city in cities:
        if city[4] == sys.argv[4]:
            city_name.append(city[2])

    print(", ".join(city_name))
