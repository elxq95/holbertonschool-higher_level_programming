#!/usr/bin/python3
""" This module is for filtering states starts witn 'n' using MySQLdb"""

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
    sql = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC".format(name_search)
    # Pass 'name_search' as a single-item tuple
    cursor.execute(sql, (name_search,))
    n_states = cursor.fetchall()

    for n in n_states:
        print(n)

    cursor.close()
    db_connection.close()
