import sqlite3

try:
    # Connect to an in-memory SQLite database
    # For a file-based database, use: conn = sqlite3.connect('my_database.db')
    conn = sqlite3.connect(':memory:')
    print("Successfully connected to SQLite database.")
    
    # You can now use the 'conn' object to create cursors, execute queries, etc.
    # Example:
    # cursor = conn.cursor()
    # cursor.execute("SELECT SQLITE_VERSION()")
    # version = cursor.fetchone()
    # print(f"SQLite version: {version[0]}")

except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()
        print("Database connection closed.")