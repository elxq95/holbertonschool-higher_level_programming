#!/usr/bin/python3
""" This module is for filtering states where name matches the argument using MySQLdb"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    name_search = sys.argv[4]
    cursor = db_connection.cursor()
    sql = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
    cursor.execute(sql, (name_search,))
    n_states = cursor.fetchall()

    for n in n_states:
        print(n)

    cursor.close()
    db_connection.close()
