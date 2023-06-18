#!/usr/bin/python3
"""
This script displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys


def list_states_arg(username, password, database, state_name):
    """connection to MySQL server"""
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()
    """connect  to the MySQL server"""

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC",
        {'name': sys.argv[4]})

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    """Gets arguents from the command line"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_states_arg(username, password, database, state_name)
