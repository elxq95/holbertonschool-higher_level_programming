#!/usr/bin/python3
""" This module is for listing all cities"""

# code to execute only when running directly
if __name__ =="__main__":
    import MySQLdb
    import sys
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    
    cursor = db_connection.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id = cities.state_id" \
    "ORDER BY cities.id ASC"
    cursor.execute(sql)
    n_cities = cursor.fetchall()

    for n in n_cities:
        print(n)

    cursor.close()
    db_connection.close()