#/usr/bin/python3

""" THis module is for filtering states starts with'n' using MYSQLdb"""

if __name__ = "__main__":
    import MySQLdb
    import sys
    # The MySQLdb.connect() function is used to establish a 
    # connection between your Python script and the MySQL database.
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    name_search = sys.argv[4]
    cursor = db_connection.cursor()
    # The line cursor = db_connection.cursor() initializes this cursor object, 
    # which is now connected to the MySQL server through db_connection.
    # A cursor is a database access mechanism that 
    # enables you to execute SQL commands and retrieve data from the database.
    sql = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
    cursor.execute(sql, (name_search,))
    #This line executes the SQL query stored in sql. 
    # The name_search value is passed as a parameter to the query to avoid SQL injection vulnerabilities.
    n_states = cursor.fetchall()
    
    for n in n_states:
        print(n)
    
    cursor.close()
    db_connection.close()