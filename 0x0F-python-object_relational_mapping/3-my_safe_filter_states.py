#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Access to the database
    """
connection = MySQLdb.connect(host="localhost", port=3306,
                             user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': sys.argv[4]})

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
connection.close()
