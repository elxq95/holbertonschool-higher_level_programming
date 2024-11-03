#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    # Create a cursor to execute SQL queries
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch and print each row
    for row in cursor.fetchall():
        print(row)
    # Close cursor and connection
    cursor.close()
    db_connection.close()
