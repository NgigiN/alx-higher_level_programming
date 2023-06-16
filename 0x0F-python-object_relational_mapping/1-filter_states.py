#!/usr/bin/python3

import MySQLdb
import sys

def list_states_N(username, password, database):

    connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            db='hbtn_0e_0_usa'
            )

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM states WHERE name LIKE "N%"')

    results = cursor.fetchall()

    for row in results:
        print('({}, \'{}\')'.format(row[0], row[1]))

    cursor.close()
    connection.close()

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states_N(username, password, database)
