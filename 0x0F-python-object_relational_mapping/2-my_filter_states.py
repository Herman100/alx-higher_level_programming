#!/usr/bin/python3

"""A python script that employs the module MySQLdb to list
the data in a database
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    username, password, database, state_name = sys.argv[1:]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id".
                format(state_name))
    table = cur.fetchall()

    for row in table:
        print(row)

    cur.close()
    conn.close()
