#!/usr/bin/python3
"""
This module lists all states with a name starting with N from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    cursor = db_connection.cursor()
    
    # Execute the SQL query
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)
    
    # Fetch all results that match the query
    states = cursor.fetchall()
    
    # Print each state in the required format
    for state in states:
        print(state)
    
    # Close the cursor and database connection
    cursor.close()
    db_connection.close()