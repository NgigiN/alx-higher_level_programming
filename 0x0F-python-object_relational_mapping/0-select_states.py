#!/usr/bin/python3
"""
this script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """connect to the MySQL server"""
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = connection.cursor()
    """query the database for all states"""
    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    results = cursor.fetchall()

    """iterate over the results and print each state"""
    for row in results:
        print(row)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    """Gets arguments from the command line"""
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        """List all states"""
        list_states(username, password, database)
