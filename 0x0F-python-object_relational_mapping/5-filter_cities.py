#!/usr/bin/python3
"""This script takes in the name of a state
and lists all cities of that state, in hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    "Access the database and get cities"

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': sys.argv[4]
        })

    results = cursor.fetchall()

    if results is not None:
        print(", ".join([row[1] for row in results]))
