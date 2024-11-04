#!/usr/bin/python3
""" This module is for taking in the name of a state as an argument
and lists all cities of that state"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        # sys.argv[1], sys.argv[2], and sys.argv[3] are 
        # command-line arguments that represent the MySQL username, password, and database name, respectively
        )

    state_name = sys.argv[4]
    # state_name is set to the fourth command-line argument, 
    # which is the name of the state whose cities you want to list.
    cursor = db_connection.cursor()
    sql = "SELECT cities.name FROM cities JOIN states " \
        "ON cities.state_id = states.id WHERE states.name = %s" \
        "ORDER BY cities.id ASC"
    # SELECT cities.name
    # FROM cities
    # JOIN states
    # ON cities.state_id = states.id
    # WHERE states.name = %s
    # ORDER BY cities.id ASC
    cursor.execute(sql, (state_name,))
    n_cities = cursor.fetchall()

    print(", ".join(n[0] for n in n_cities))
    # n[0] means “give me the first item in each tuple.”
    # Since each tuple contains only the city name as 
    # its first item, n[0] will just be the city name.
    cursor.close()
    db_connection.close()