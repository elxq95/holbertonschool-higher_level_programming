import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')  # This will create products.db in the current directory
    cursor = conn.cursor()
    
    # Create the Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insert example data into Products table
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

# Run the function to create the database
create_database()
