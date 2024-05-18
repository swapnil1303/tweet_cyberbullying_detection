import sqlite3

def create_table():
    # Connect to the SQLite database
    # If the database does not exist, it will be created
    conn = sqlite3.connect('child_proj.db')
    
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    
    # Create the register table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS register (
            email TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Table created successfully.")
