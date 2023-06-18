#!/usr/bin/python3
"""
Script that lists all cities from the database
`hbtn_0e_4_usa`
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """Access the database safely"""

    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")

        results = cursor.fetchall()

        if results is not None:
            for row in results:
                print(row)
