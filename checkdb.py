import sqlite3

def fetch_and_print_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('child_proj.db')
    
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    
    # Execute a query to retrieve all data from the register table
    cursor.execute('SELECT * FROM register')
    
    # Fetch all rows from the result of the query
    rows = cursor.fetchall()
    
    # Print the column names
    print("email, username, password, phone, address")
    print("-" * 50)
    
    # Loop through the rows and print each one
    for row in rows:
        print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}")
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    fetch_and_print_data()
    print("Data fetched successfully.")
